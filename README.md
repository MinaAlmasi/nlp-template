# NlP TEMPLATE REPOSITORY
Created by Mina Almasi for the NLP course!

> Warning: All of this repository is either fake placeholder text or random code!

## 📖 About
This GitHub repository should be considered a *guiding* template for how to structure codebases for research projects with the aim to reproduce your code! 

> Please note this differs widely from production code for software packages!

Don't take the template too seriously - play with it and find your style! The most important thing is that you tell *us*:
1. What is your code, data and results? And where are your files located?
2. How do we reproduce your code?

### Project Overview
The repository is structured as such: 
| Folder/File               | Description |
|---------------------------|-------------|
| `data/`                   | Contains raw data and processed ... |
| `plots/`                  | Word distributions etc. |
| `results/`                | Evaluation results for the main analysis. |
| `src/`                    | Python code related to the project. |


For a greater overview of the Python code, see the [src/README.md](src/README.md)


## 💻 Technical Requirements 
Grid search and model training was run via Ubuntu 22.04.3, Python 3.10.12 (UCloud, Coder Python 1.87.2). Other analysis work such as plotting was done locally on a Macbook Pro ‘13 (2020, 2 GHz Intel i5, 16GB of ram). Python's `venv` need to be installed for the code to run as intended.

*Please also note that the advanced models were computionally intensive and were run on a 64 machine on UCloud*. 

## 🛠️ Setup
Prior to running the code, run the command below to create a virtual environment (`venv`) and install necessary packages within it: 
```bash
bash setup.sh
```

##  🚀 Usage 
To run any script in the `src` folder, you can type specify the script's path in the terminal (with the `.venv` active):
```bash
# activate env
source .venv/bin/activate

# run script
python src/get_paths.py

# quit env 
deactivate
```

Specifically to reproduce the results of the main analysis, run ....

## 🌟 Acknowledgements
If you want to thank a data provider or a package that you heavily relied on ;)

(Not strictly necessary)

## 💬 Contact
This repository was created by .... 

(Not strictly necessary section)