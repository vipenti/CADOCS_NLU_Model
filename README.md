[![Created Badge](https://badges.pufler.dev/created/vipenti/CADOCS_NLU_Model)](https://badges.pufler.dev)
[![Visits Badge](https://badges.pufler.dev/visits/vipenti/CADOCS_NLU_Model)](https://badges.pufler.dev)

<p align = "center">
  <img src = "https://github.com/vipenti/CADOCS_NLU_Model/blob/main/cadocs_logo.png?raw=true" width = "400" heigth = "200">
</p>

# CADOCS: Natual Language Understanding Module

## Introduction

**CADOCS** is a conversational agent working on the Slack platform and able to use third-party tools to identify and manage *community smells* in software development communities on GitHub.

Specifically, this is the repository containing the Natural Language Understanding service module to interpret users' intent. The main [CADOCS](https://github.com/gianwario/CADOCS) app communicates with this module through an API call.


## Content of the Repository

The main elements of the repository are described below:

- CADOCS.py: This module is responsible to create the NLU model through the given dataset and to make predictions with it
- cadocs_service.py: This is the web services that exposes the model functionalities through HTTP requests
- dataset.csv: This is the dataset we used to train the model, built with a survey
- default/current: This is the actual model that CADOCS uses to make predictions

## Other Tools

The entire CADOCS tool is composed of three modules:
- **CADOCS** [link](https://github.com/gianwario/CADOCS): it is the Slack App used to interact with users.
- **CADOCS_NLU_Model** (this repository): it is the ML service used to interpret the users' intents.
- **csDetector** [link](https://github.com/gianwario/csDetector): the augmented and wrapped version of csDetector, used in our tool to detect community smells and other socio-technical metrics.

<!--
## Authors

List of authors:

- **Gianmario Voria** — *g.voria6@studenti.unisa.it* — University of Salerno, Salerno, Italy
- **Viviana Pentangelo** — *v.pentangelo4@studenti.unisa.it* — University of Salerno, Salerno, Italy
- **Antonio Della Porta** — *a.dellaporta26@studenti.unisa.it* — University of Salerno, Salerno, Italy
- **Stefano Lambiase** — *slambiase@unisa.it* — Software Engineering (SeSa) Lab, Department of Computer Science - University of Salerno, Salerno, Italy
- **Gemma Catolino** — *g.catolino@tilburguniversity.edu* — Jheronimus Academy of Data Science - Tilburg University, 's-Hertogenbosch, Netherlands
- **Fabio Palomba** — *fpalomba@unisa.it* — Software Engineering (SeSa) Lab, Department of Computer Science - University of Salerno, Salerno, Italy
- **Filomena Ferrucci** — *fferrucci@unisa.it* — Software Engineering (SeSa) Lab, Department of Computer Science - University of Salerno, Salerno, Italy
-->

## How to Install *CADOCS: Natural Language Understanding Module* Locally

#### Requirements

- Anaconda 3 - 2022.05 - 64bit
- Windows 10
- Microsoft Visual C++ Build Tools 14.0 or higher (In order to run Anaconda) 
- (Optional, if you won't use Anaconda to install it) Python 3.7.13 

#### Installation Steps

- Step 1: Local installation of the NLU service (Recommended, using Anaconda)
  - Clone the current repository on your system
  - In our repository, find the *cadocs_NLU_env.yaml* file which contains the environment and the dependencies needed
  - Through the Anaconda Powershell, run the following command: *conda env create -f ENV_FILE_NAME.yaml*

In case you faced some error installing the Anaconda environment, please proceed with the Step 1.1

- (Optional) Step 1.1: Local installation of the NLU service (Manual)
  - Clone the current repository on your system
  - In our repository, find the *cadocs_NLU_env.yaml* file which contains the environment and the dependencies needed
  - Create a new Python 3.7.13 environment
  - Within the previously mentioned file, you will find each of the dependencies needed to run the tool
  - Install by hand each of them in your env
 
- Step 2: Installation of the English dictionary
  - After having installed the environment, open an Anaconda Powershell with the admin privileges
  - Run the following commands
    - conda activate ENVIRONMENT_NAME
    - python -m spacy download en_core_web_md
    - python -m spacy link en_core_web_md en
 
- Step 3: Use our Model!
  - Open the project on your system with the IDE you prefer (__We suggest using Visual Studio Code or PyCharm__)
  - Activate the python environment created in the Step 1 and run the module *cadocs_service.py*

- (Optional) Step 4: Test it
  - Open your browser
  - Make a GET request like follows: http://localhost:5000/predict?message=YOUR_MESSAGE


## Contributors

[![Contributors Display](https://badges.pufler.dev/contributors/vipenti/CADOCS_NLU_Model?size=75&padding=5&bots=true)](https://badges.pufler.dev)

<!--
## References

Please, if you want to cite our work use the following *bibtex* code:

```bibtex

```
-->
