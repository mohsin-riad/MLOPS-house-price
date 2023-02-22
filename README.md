<h1 align="center">End to End House Price Prediction</h1>
<div align="center">

![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) 	![Windows 11](https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white)

![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) 	![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

</div>

<h2><a href="https://california-house-price.onrender.com/">⚠️ Live Here</a></h2>

## ML-OPS
MLOps, or DevOps for machine learning, enables data science and IT teams to collaborate and increase the pace of model development and deployment by monitoring, validation, and governance of machine learning models. 

<img src="./assets/ml-ops-schema.png" width="600">

Here, we're going to ecxplore more with real life prediction scenerios.

## Dataset Overview
### [California Housing](https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html)
This dataset was derived from the 1990 United States Census, with one row for each census block group. The smallest geographic unit for which the U.S. Census Bureau releases sample data is a block group (a block group typically has a population of 600 to 3,000 people). A household is a collection of people who share a single residence. Since the average number of rooms and bedrooms in this dataset is given for each household, these columns may take very large values for block groups with few people and many vacant properties, such as resort communities.

<img src="./assets/data-cols.png" width="800">

The file contains all the the variables. Specifically, it contains median house value, median income, housing median age, total rooms, total bedrooms, population, households, latitude, and longitude in that order.

## Workflow

### Exploratory Data Analysis (EDA)

<code><b> 1. Univariate Target Density </b></code>

> <img src="./assets/kdeplot.png" width="500">

<code><b> 2. Correlation Analysis </b></code>

Correlation analysis examines the linear correlation between variable pairs.

> <img src="./assets/pairplot.png" width="500">

Observations:
- To fit a linear regression model, we select those features which have a high correlation with our target variable 'Target'. By looking at the correlation matrix we can see that 'MedInc' has a strong positive correlation with 'Target' (0.69) where as 'Latitude' has a high negative correlation with 'Target'(-0.14).

- An important point in selecting features for a linear regression model is to check for multi-co-linearity. The features 'AveRooms', 'AveBedrms' have a correlation of 0.85. These feature pairs are strongly correlated to each other. We should not select both these features together for training the model. Same goes for the features 'Latitude' and 'Longitude' which have a correlation of -0.92.

<code><b> Target v/s Lattitude & Target v/s Medinc </b></code>

> <img src="./assets/regplot.png" width="800">

### Data Preparation

- Splitting the data into training and testing sets.

- Normalization/Standard Scalling. 

- > <b>Note:</b>Why do we standardize data in Linear regression? Internally we use gradient descend algorithm, our main aim is to reach the global minima. To achieve that, we have to make sure that all our independent feature units should be on the same scale in order for convergence to happen.

### Model Overview 

Linear regression analysis is used to predict the value of a variable based on the value of another variable. The variable you want to predict is called the dependent variable. The variable you are using to predict the other variable's value is called the independent variable.

<img src="./assets/LR-model.png" width="300">

A simple linear regression, y = b0 + b1x, predicts relationship between one independent variable x and one dependent variable y, for instance, the classic height — weight correlation. As more features/independent variables are introduced, it evolves into multiple linear regression y = b0 + b1x1 + b2x2 + … + bnxn, which cannot be easily plotted using a line in a two dimensional space.

### Model Evaluation

Linear regression model can be qualitatively evaluated by visualizing error distribution. 

<code><b> Assumptions </b></code>

<img src="./assets/assumptions.png" width="700">

<code><b> Residuals </b></code>

<img src="./assets/residuals.png" width="400">

## Deployment

> Configure Dockerfile

> Configure CI/CD Pipeline

End to End Live Machine Learning Regression Inference 

<img src="./assets/deployed.png" width="1000">

## Important Commands
To create a virtual environment 
```
conda create -p venv python==3.8 -y
```
To Activate Virtual Environment
```
. venv/bin/activate
```
To Deactivate VENV
```
conda deactivate
```
To Install Required Libraries
```
pip install -r requirements.txt
```
