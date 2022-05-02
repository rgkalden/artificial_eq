# Artificial EQ

Welcome to Artificial EQ, the Sentiment Analysis Web App to help predict emotions!

## Quick Start
To run the Flask Web App, clone this repository, open a terminal and enter the following command:
```
python app.py
```

## 1. Introduction
In this project, a NLP deep learning model is developed to classify the emotion associated with a comment. The model is based on the GoEmotions dataset that is available from the TensorFlow data sets collection. More information on the dataset can be found at the following links:
* [Google GoEmotion GitHub Page](https://github.com/google-research/google-research/tree/master/goemotions)
* [TensorFlow Datasets catalog page](https://www.tensorflow.org/datasets/catalog/goemotions)

The emotion categories are: admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire, disappointment, disapproval, disgust, embarrassment, excitement, fear, gratitude, grief, joy, love, nervousness, optimism, pride, realization, relief, remorse, sadness, surprise, and neutral.

Some of the web app and Flask aspects of this project have been borrowed from a tutorial which can be found [here.](https://towardsdatascience.com/how-to-easily-deploy-machine-learning-models-using-flask-b95af8fe34d4).


## 2. Objectives

This project has the following objectives:

1. Train NLP classification model using TensorFlow
2. Create inference script
3. Create Web App using Flask
4. Dockerize model

## 3. Getting Started

Once this repository has been cloned, a virtual environment can be created with the Python package requirements in `requirements.txt`.

### 3.1 Background Information on Model Development

In order to develop and train the model, a Google Colab notebook has been used to take advantage of GPU access, and the file is `artificial_eq_model.ipynb`. There are two results saved from this notebook: the model, and the comment tokenizer object. The model file `*.h5` is saved so that it can be loaded in a new inferencing script to make predictions. The tokenizer object that has been fitted during model training is saved as `tokenizer.joblib` so that it can be used to preprocess new comments before predictions are made.

>**NOTE:** Currently, only a baseline model has been created that has an accuracy score of 0.5 on test data. Most of the time, predictions make sense subjectively however there are obviously comments that will not have a correct emotion associated with the comment that is submitted to the model for prediction. In the future a more accurate model will be developed. The code is designed in a way that a new model file can be substituted in, making updates easy.

### 3.2 Developing the App

The model file and tokenizer file saved from `artificial_eq_model.ipynb` are used in an inferencing script, `inference.py`, to make predictions. The inferencing script is used in two ways for this project:
1. As a library of functions for the Flask app script, `app.py`
2. Included in the Docker image to act as the inference pipeline used to make predictions

The `templates` folder holds the HTML file `index.html` which provides the UI for the Flask web app.

The `Dockerfile` builds an image based on the Python image from Docker Hub.

For this project, there are two versions of the same app: a Flask web app, and a Docker app. To run each version, see the instructions in the next section.

## 4. Running the App

### 4.1 Flask Web App
In order to run the app, enter the following command in a terminal (`cd` to this repo folder first):
```
python app.py
```

Note the URL displayed in the command line (for example http://127.0.0.1:5000) and open the URL in your browser. Follow the instructions on the webpage, and have fun predicting emotions!

### 4.2 Docker App

The Docker App runs in a terminal.

To run the Docker app, an image must first be created.
```
docker build -t artificial_eq -f Dockerfile .
```

Then, run a container in interactive mode, with container name specified:
```
docker run -it --name artificial_eq_app artificial_eq
```

Follow the instructions and and have fun predicting emotions!