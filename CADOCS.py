import logging, json, warnings
logging.basicConfig(level="INFO")
warnings.filterwarnings('ignore')
import os
import pandas as pd

from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer, Interpreter
from rasa_nlu import config

# Path were the dataset is stored
DATASET_PATH = "survey.csv"
# Path were the project is located
PROJECT_PATH = os.getcwd()
# Creation of the DataFrame containing the dataset
df = pd.read_csv(DATASET_PATH, sep=",", header=None)

# Function that indents the printing of a JSON object
def pprint(o):
    print(json.dumps(o, indent=2))

# This class represents the logic of the ML model
class CADOCSModel:

    # Created an MarkDown file containing the training data
    def create_training_data_md(self):
        qs1 = df[2][1:27]
        qs2 = df[3][1:27]
        qs3 = df[4][1:27]
        qs4 = df[5][1:27]
        with open(os.path.join(PROJECT_PATH, "nlu.md"), "wt", encoding="utf-8") as f:
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

    # Created an MarkDown file containing the testing data
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

    # This function it is where the training of the model takes place
    def train_model(self):
        # It creates the training and the testing data from the dataset
        self.create_training_data_md()
        self.create_test_data_md()
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


if __name__ == "__main__":
    model = CADOCSModel()
    model.train_model()
    pprint(model.give_prediction("hello CADOCS, show me the community smells in the repository https://github.com/tensorflow/ranking"))