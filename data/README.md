## How to use this folder & readme
This folder can be used in different ways. If the dataset's license permits it, you can upload the data here e.g., `raw_data.txt` and `clean_data.txt`. 

You can also use this README within the data folder to provide instructions on how to download the data and place it here. You would also place it here, but ignore the file using `gitignore`.

[Example](#data-folder-readme-example) of how this could look is below. 

### Note: If your data is not freely available for download
1. You can also write in your exam that the dataset is sent as "extra material" to the examiners (if you are allowed to share but not distribute widely on GitHub). 

2. A final alternative is to provide some fake "dummy data" that makes your code able to run.

## DATA FOLDER README EXAMPLE
Download the *Indo fashion* [Kaggle dataset](https://www.kaggle.com/datasets/validmodel/indo-fashion-dataset) dataset from kaggle and place it in this folder ! 

The data should be structured with subdirectories as such: 
```
└── images
    ├── README.md
    ├── metadata      <--- JSON files containing metadata for each set of data (test_data.json, train_data.json, val_data.json)     
    ├── test          <--- JPEG files as test set
    ├── train         <--- JPEG files as train set
    └── val           <--- JPEG files as validation set
```

### Note: Use this folder but place everything but .README in gitignore!
If you do it as the example above, remember to *actually* use the folder for your data, so that your paths from your scripts match this. 

**To avoid pushing the data, you should place everything in the folder but this README in `.gitignore`.** For the example above, this would be: 
```
# ignore data folder, but not the readme within !
images/*
!images/README.md 

# ignore models
models/*
!models/README.md
```