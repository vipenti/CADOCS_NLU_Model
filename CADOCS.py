import logging, json, warnings

logging.basicConfig(level="INFO")
warnings.filterwarnings('ignore')
import os
import pandas as pd

from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer, Interpreter
from rasa_nlu import config

# Path were the dataset is stored
DATASET_PATH = "dataset.csv"
# Path were the project is located
PROJECT_PATH = os.getcwd()
# Creation of the DataFrame containing the dataset
df = pd.read_csv(DATASET_PATH, sep=";", header=None)


# Function that indents the printing of a JSON object
def pprint(o):
    print(json.dumps(o, indent=2))


# This class represents the logic of the ML model
class CADOCSModel:
    # Defines the number of the dataset updates required to perform a re-train of the model
    TO_RETRAIN = 10
    # Number of updates performed. It resets when it reaches the value specified by TO_RETRAIN
    UPDATE_COUNT = 0

    # Created an MarkDown file containing the training data
    def create_training_data_md(self):

        int1 = []
        int2 = []
        int3 = []
        int4 = []

        for row in df.iterrows():
            if row[1][1] == "get_smells":
                int1.append(row[1][0])
            if row[1][1] == "get_smells_date":
                int2.append(row[1][0])
            if row[1][1] == "report":
                int3.append(row[1][0])
            if row[1][1] == "info":
                int4.append(row[1][0])

        with open(os.path.join(PROJECT_PATH, "nlu.md"), "wt", encoding="utf-8") as f:
            f.write("## intent: get_smells\n")
            for q in int1:
                f.write(f"- {q}\n")
            f.write("## intent: get_smells_date\n")
            for q in int2:
                f.write(f"- {q}\n")
            f.write("## intent: report\n")
            for q in int3:
                f.write(f"- {q}\n")
            f.write("## intent: info\n")
            for q in int4:
                f.write(f"- {q}\n")

    '''# Created an MarkDown file containing the testing data
    def create_test_data_md(self):
        qs1 = df[2][27:]
        qs2 = df[3][27:]
        qs3 = df[4][27:]
        qs4 = df[5][27:]
        with open(os.path.join(PROJECT_PATH, "nlu_test.md"), "wt", encoding="utf-8") as f:
            f.write("## intent: get_smells\n")
            for q in qs1:
                f.write(f"- {q}\n")
            f.write("## intent: get_smells_date\n")
            for q in qs2:
                f.write(f"- {q}\n")
            f.write("## intent: report\n")
            for q in qs3:
                f.write(f"- {q}\n")
            f.write("## intent: info\n")
            for q in qs4:
                f.write(f"- {q}\n")
    '''
    # This function it is where the training of the model takes place
    def train_model(self):
        # It creates the training and the testing data from the dataset
        self.create_training_data_md()
        # self.create_test_data_md()
        print("MD files created")

        training_data = load_data(os.path.join(PROJECT_PATH, "nlu.md"))

        # A Trainer object is created and the model is trained
        trainer = Trainer(config.load(os.path.join(PROJECT_PATH, "config.yml")))

        print("Starting training...")
        trainer.train(training_data)

        # The model is saved and stored in the specified path, so it can be used again in the future
        print("Storing...")
        trainer.persist(PROJECT_PATH, fixed_model_name="current")
        print("Stored!")

    # This function uses the generated model to make predictions on a given message
    # The message is the sentence of the user from which you want to extract the intent
    def give_prediction(self, message):
        # An interpreter is created and it's used to load the pre-trained model
        print("Loading interpreter...")
        interpreter = Interpreter.load(model_dir="default/current")

        # The interpreter parses the message and causes the model to provide its prediction
        return interpreter.parse(message)

    # This function updates the existing dataset
    # When new question are asked to the Conversational Agent and a correct prediction is provided, that entry is added to the dataset
    # After a number of updates specified by TO_RETRAIN has been performed, Active Learning is performed
    def update_dataset(self, message, intent):

        df = pd.read_csv(DATASET_PATH, sep=";", header=None)
        # A new row for the dataset is created with the given message and intent
        new_row = {0: [message],
                  1: [intent]}
        df_tmp = pd.DataFrame(new_row)

        # The new row is added to the existing dataset
        df = df.append(df_tmp)
        pd.DataFrame(df).to_csv(os.path.join(PROJECT_PATH, "dataset.csv"), sep=";", header=None, index=False)

        # Since an updated has been performed, the counter is increased
        self.UPDATE_COUNT += 1

        # This is where the Active Learning is performed
        # When the value of TO_RETRAIN is equal to the UPDATE_COUNT one, the latter is reset and the model is trained again
        if (self.TO_RETRAIN == self.UPDATE_COUNT):
            self.UPDATE_COUNT = 0
            self.train_model()
        return


if __name__ == "__main__":
    model = CADOCSModel()
    res = model.give_prediction("hello CADOCS, show me the community smells in the repository https://github.com/tensorflow/ranking from 21/05/2020")
    print(res)
