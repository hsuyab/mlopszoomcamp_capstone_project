# MLOps Zoomcamp Final Project
- This repository contains the final project for [mlops zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) project

## Problem Statement
- Here we have used a very popular case study by Darden School of Business, published in [Harvard Business](https://hbsp.harvard.edu/product/UV0869-PDF-ENG). 
- This is regarding the story of two people who are going to be married in the future. The guy named Greg wanted to buy a ring to propose to a girl named Sarah. 
- The problem is to find the ring Sarah will like, but after a suggestion from his close friend, Greg decides to buy a diamond stone instead so that Sarah can decide her choice. 
- Greg then collects data of 6000 diamonds with their price and attributes like cut, color, shape, etc.
- The final objective is to predict the `Price` using attributes like cut, color, shape, etc.

## Approach

- To start with create a conda environment with:
```
conda env create -f environment.yml
```
or you can use the requirements.txt
```
pip install -r requirements.txt
```
- Then you can implement the `model.ipynb` notebook to train the model and get the best model for prediction.

- The best model has been saved as a pickle file `model_pipeline_final.pkl`

- The experiment tracking details have been stored in images mlflow which shows runs using different model types with the best model being `CatBoostRegressor` with an mean absolute percentage error of **4.41%**.

- Since most of the features are categorical.

- In the [feature importance plot](https://github.com/hsuyab/project_final/blob/master/feature_importance_plot.png), we see that most important feature is the `Carat Weight` which makes sense from modeling perspective.

- The webserver folder contains the [Dockerfile](https://github.com/hsuyab/project_final/blob/master/webserver/Dockerfile) as well as code to run the flask api.

- This work was done on *AWS Cloud* on a `t2.xlarge` instance.

## Future Work
- Including monitoring and model orchestration.
- Using IaaC, terraform to automate the instance creation.

# Acknowledgement
- I would like to thank the [DataTalkClub](https://datatalks.club/) - Alexey and the entire team for such and amazing learning experience. Thanks a lot.



