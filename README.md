# Artificial EQ

Welcome to Artificial EQ, the Sentiment Analysis Web App to help predict emotions!

In this project, a NLP deep learning model will be developed to classify the emotion associated with a comment. The model is based on the GoEmotions dataset that is available from the TensorFlow data sets collection. More information on the dataset can be found [here.](https://github.com/google-research/google-research/tree/master/goemotions)

The web app and Flask aspects of this project have been based on a tutorial which can be found [here.](https://towardsdatascience.com/how-to-easily-deploy-machine-learning-models-using-flask-b95af8fe34d4).


**Objectives**

This project has the following objectives:

1. Train NLP classification model using TensorFlow
2. Create inference script
3. Create Web App using Flask
4. Dockerize model

## 1. Getting Started

To reproduce the virtual environment used for this project, Python package requirements can be found in `requirements.txt`.

In order to develop and train the model, a Google Colab notebook has been used to take advantage of GPU access, and the file is `artificial_eq_model.ipynb`. There are two results saved from this notebook: the model, and the comment tokenizer object. The model file `*.h5` is saved so that it can be loaded in a new script to make predictions. The tokenizer object that has been fitted during model training is saved as `tokenizer.joblib` so that it can be used to preprocess new comments before predictions are made.

>**NOTE:** Currently, only a baseline model has been created that has an accuracy score of 0.5 on test data. Most of the time, predictions make sense subjectively however there are obviously comments that will not have a correct emotion associated with the comment that is submitted to the model for prediction. In the future a more accurate model will be developed. The code is designed in a way that a new model file can be substituted in, making updates easy.

## 2. Running the App

### 2.1 Flask Web App
In order to run the app, enter the following command in a terminal:
```
python app.py
```

Note the URL displayed in the command line (for example http://127.0.0.1:5000) and open the URL in your browser. Follow the instructions on the webpage, and have fun predicting emotions!