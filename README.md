# X-Ray Diagnosis for Covid-19 :brazil: 

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technologies Used](#technologies-used)
  * [Technical Aspect](#technical-aspect)
  * [Machine Learning Model](#machine-learning-model)
  * [Data Collection](#data-collection)
  * [Team](#team)
  * [Credits](#credits)

## Demo
Link: [https://xray-diagnosis.herokuapp.com/](https://xray-diagnosis.herokuapp.com/)

[![](https://i.imgur.com/OQtj3qX.png)](https://xray-diagnosis.herokuapp.com/)

## Overview
This is a classifation app build in the Django Framework. The CNN takes a x-ray image, and predict if the image belongs to 1 of 3 classes: Normal, Covid or Pneumonia.

## Motivation
Due to the context of the year 2020, the motivation is self-explanatory. As of November 23, 2020, the new coronavirus has already killed 1,395,649 people around the world, 
and any means of helping to detect the disease is of great help. 
That is why this application assists in the detection of covid 19 by analyzing x-ray images.

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://res-4.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/x3gdrogoamvuvjemehbr" width=200>](https://keras.io/) [<img target="_blank" src="https://cdn.iconscout.com/icon/free/png-512/django-2-282855.png" width=170>](https://www.djangoproject.com/) [<img target="_blank" src="https://rapids.ai/assets/images/xgboost_logo.png" width=280>](https://xgboost.readthedocs.io/en/latest/) [<img target="_blank" src="https://cdn.iconscout.com/icon/free/png-512/heroku-5-569467.png" width=200>](https://dashboard.heroku.com/apps) 


## Technical Aspect
This project is divided into two parts:
1. Training a machine learning model using Keras/Tensorflow.
2. Building and hosting a Django web app on Heroku.


## Machine Learning Model
In this classification problem, a convolutional neural network was used to train the model. The program receives a raw image, and then proceeds to clean it. After that, the 
cleaned image is fed into the CNN, that proceeds to train and in the end classify the image. 

## Data Collection



## Team
[![Leonardo França Bessa](https://avatars2.githubusercontent.com/u/22757584?s=460&u=34b2e3fde44b13d47ce00e372cf66db078a8e300&v=4)](https://www.linkedin.com/in/leonardo-fran%C3%A7a-2246641a3/) |
-|
[Leonardo França Bessa](https://www.linkedin.com/in/leonardo-fran%C3%A7a-2246641a3/) |)

## Credits
- [Creating a Machine Learning Based Web Application Using Django](https://towardsdatascience.com/creating-a-machine-learning-based-web-application-using-django-5444e0053a09): Withouth this amazing tutorial on how to build a app using Django, I wouldn't be able to develop this.
