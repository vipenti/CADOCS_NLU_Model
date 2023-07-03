[![Created Badge](https://badges.pufler.dev/created/vipenti/CADOCS_NLU_Model)](https://badges.pufler.dev)
[![Visits Badge](https://badges.pufler.dev/visits/vipenti/CADOCS_NLU_Model)](https://badges.pufler.dev)

<p align = "center">
  <img src = "https://github.com/vipenti/CADOCS_NLU_Model/blob/main/cadocs_logo.png?raw=true" width = "400" heigth = "200">
</p>

# CADOCS: Natual Language Understanding Module

## Introduction

**CADOCS** is a conversational agent working on the Slack platform and able to use third-party tools to identify and manage _community smells_ in software development communities on GitHub.

Specifically, this is the repository containing the Natural Language Understanding service module to interpret users' intent. The main [CADOCS](https://github.com/gianwario/CADOCS) app communicates with this module through an API call.

## Content of the Repository

The main elements of the repository are described below:

- CADOCS.py: This module is responsible to load the NLU models and give predictions
- cadocs_service.py: This is the web services that exposes the model functionalities through HTTP requests
- dataset folder: This is the folder which contains all the datasets used in the project
- jupiter folder: All the Python notebooks created for the project
- requirements.txt: The dependencies needed to execute the module

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

## How to Install _CADOCS: Natural Language Understanding Module_ Locally

#### Requirements

- Python version 3.7+

#### Installation Steps

- Step 1: Local installation of the NLU service (Recommended, using Anaconda)

  - Clone the current repository on your system
  - In our repository, find the _requirements.txt_ file which contains the dependencies needed
  - Create the virtual environment and run the following command: _pip install -r requirements.txt_

- Step 2: Use our Model!

  - Open the project on your system with the IDE you prefer (**We suggest using Visual Studio Code or PyCharm**)
  - Activate the python environment created in the Step 1 and run the module _cadocs_service.py_

- (Optional) Step 3: Test it
  - Open your browser
  - Make a GET request like follows: http://localhost:5000/predict?message=YOUR_MESSAGE

## Contributors

[![Contributors Display](https://badges.pufler.dev/contributors/alfcan/CADOCS_NLU_Model?size=75&padding=5&bots=true)](https://badges.pufler.dev)

<!--
## References

Please, if you want to cite our work use the following *bibtex* code:

```bibtex

```
-->
