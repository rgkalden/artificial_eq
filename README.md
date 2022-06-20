# Artificial EQ 😎

Welcome to Artificial EQ, the Sentiment Analysis Web App to help predict emotions!

To try the web app, go to [https://artificial-eq.herokuapp.com/](https://artificial-eq.herokuapp.com/) and have fun predicting emotions!

## 1. Introduction
In this project, a NLP deep learning model is developed to classify the emotion associated with a comment. The model is based on the GoEmotions dataset that is available from the TensorFlow data sets collection. More information on the dataset can be found at the following links:
* [Google GoEmotion GitHub Page](https://github.com/google-research/google-research/tree/master/goemotions)
* [TensorFlow Datasets catalog page](https://www.tensorflow.org/datasets/catalog/goemotions)

The emotion categories are: admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire, disappointment, disapproval, disgust, embarrassment, excitement, fear, gratitude, grief, joy, love, nervousness, optimism, pride, realization, relief, remorse, sadness, surprise, and neutral.

Some of the Flask aspects of this project have been borrowed from a tutorial which can be found [here.](https://towardsdatascience.com/how-to-easily-deploy-machine-learning-models-using-flask-b95af8fe34d4)

A helpful introduction to Heroku can be found [here.](https://www.codecademy.com/article/deploying-a-flask-app)


## 2. Objectives

This project has the following objectives:

1. Develop NLP classification model using TensorFlow
2. Create inference script
3. Create Web App using Flask
4. Deploy App on Heroku
5. BONUS: Create Docker version of App

## 3. Overview of Project

### 3.1 Environment Setup

Once this repository has been cloned, a virtual environment can be created with the Python package requirements in `requirements.txt`. These are also the requirements for the app deployment on Heroku. 

>**NOTE:** The `tensorflow` library is quite large and in this case causes deployments on Heroku to fail due to large file sizes. Since GPU's are not used either locally or when deployed, the smaller `tensorflow-cpu` library is used instead.

The notebook `artificial_eq_model.ipynb` was ran on Google Colab, if it is desired to run locally then additional requirements are found in `notebook_requirements.txt`. The requirements are split in this way to keep the Heroku deployment size minimal.

### 3.2 Background Information on Model Development

In order to develop and train the model, a Google Colab notebook has been used to take advantage of GPU access, and the file is `artificial_eq_model.ipynb`. There are two results saved from this notebook: the model, and the comment tokenizer object. The model file `model.h5` is saved so that it can be loaded in a new inferencing script to make predictions. The model file is saved without the optimizer to keep the file size minimal, since the model will only be used for inference. The tokenizer object that has been fitted during model training is saved as `tokenizer.joblib` so that it can be used to preprocess new comments before predictions are made.

>**NOTE:** Currently, only a baseline model has been created that has an accuracy score of 0.5 on test data. In the future a more accurate model will be developed. The code is designed in a way that a new model file can be substituted in, making updates easy.

>*Future Work: Update model to increase the accuracy metric*

### 3.3 Developing the App

To start, a config file `config.py` is used to store global variables and the file paths for the model and tokenizer files. Then, an inferencing script `inference.py` is created to make predictions. The inferencing script is used in two ways for this project:
1. As a library of functions for the Flask app script, `app.py`
2. Included in the Docker image to act as the inference pipeline used to make predictions

The Flask app `app.py` creates a web app based on the inference script `inference.py`, and can be run in a development environment by running the script in a terminal. The `templates` folder holds the HTML file `index.html` which provides the UI for the web app.

#### 3.3.1 Deploying on Heroku

To  deploy the app on Heroku, the `Procfile` defines the app to use, in this case `app.py`. A `.slugignore` file is used to ignore files in this repo that are unnecesary to add to the Heroku deployment.

Heroku conveniently works with an existing Git repository to deploy an app. As an example, to deploy on Heroku, the Heroku CLI an be installed and then the following terminal commands used:
```
heroku create
git push heroku master
```
For this project, CI/CD is achieved by connecting Git and Heroku so that whenever a commit is pushed to the `main` branch of this remote repository, the changes will automatically be deployed to Heroku.

#### 3.3.2 Deploying with Docker

The `Dockerfile` builds an image based on the Python image from Docker Hub.

## 4. Running the App

### 4.1 Flask Web App
To try out the app, simply go to:

[https://artificial-eq.herokuapp.com/](https://artificial-eq.herokuapp.com/)

In order to run the app locally, enter the following command in a terminal (`cd` to this repo folder first):
```
python app.py
```

Note the URL displayed in the terminal output (for example http://127.0.0.1:5000) and open the URL in your browser. The app will be opened in a local development server, which makes it easy to make changes to the app and then refresh to page to see the results. 

Follow the instructions on the webpage, and have fun predicting emotions!

### 4.2 BONUS: Docker App

If Docker Desktop is installed, then it is possible to build a docker image and run the app in a terminal. For example:

To run the Docker app, an image must first be created.
```
docker build -t artificial-eq -f Dockerfile .
```

Then, run a container in interactive mode, with container name specified:
```
docker run -it --name artificial-eq-app artificial-eq
```

Follow the instructions and and have fun predicting emotions!