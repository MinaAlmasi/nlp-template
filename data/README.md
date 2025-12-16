## META EXPLANATION: How to use this folder & README
This folder can be used in different ways: 

1. You can use this README to provide instructions on how to download the data and place it here. While you work on the code, you would also place it in this folder, but ignore the file using `gitignore`. See [Example 1](#example-1-readme-without-pushing-data) and its meta explanation. 

2. You can upload files directly (e.g., `raw_data.txt` and `clean_data.txt`). It would still be a good idea to give a short overview of what the folder contains in README. See [Example 2](#example-2-readme-where-you-push-the-data).

### Note: If your data is not freely available for download
1. You can also write in your exam that the dataset is sent as "extra material" to the examiners (if you are allowed to share but not distribute widely on GitHub). 

2. A final alternative is to provide some fake "dummy data" that makes your code able to run.

## EXAMPLE 1: README without pushing data
Download the *Indo fashion* [Kaggle dataset](https://www.kaggle.com/datasets/validmodel/indo-fashion-dataset) dataset from kaggle and place it in this folder ! 

If downloaded and placed properly, this folder should be structured with subdirectories as such: 
```
└── data
    ├── README.md
    ├── metadata      <--- JSON files containing metadata for each set of data (test_data.json, train_data.json, val_data.json)     
    ├── test          <--- JPEG files as test set
    ├── train         <--- JPEG files as train set
    └── val           <--- JPEG files as validation set
```

### META 1: Use this folder but ignore everything but the README !
If you don't push your data, but instruct people to place it in this folder (as example 1 above), remember to *actually* use the folder for your data, so that your paths from your scripts match this. 

**To avoid pushing the data, you should place everything in the folder but this README in `.gitignore`.** For the example above, this would be: 
```
# ignore data folder, but not the readme within !
data/*
!data/README.md 
```

## EXAMPLE 2: README where you push the data
See this example repository: https://github.com/MinaAlmasi/aarhus-rentmapper/blob/main/data/README.md

### META 2: Always a good idea to give a short overview of the files!
As the example repository does above, even if you have uploaded your data to GitHub, give a description of the files in this data readme, and refer to it in the main README.