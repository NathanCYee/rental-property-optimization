# Housing Price and Rental Optimization

This repository contains notebooks for my CS 171 project to optimize property parameters to find ideal investment rental properties. The project consists of 4 folders.

- `/data_engineering` - This folder contains a notebook containing logic that utilizes Apache Spark to process and filter the data to a usable dataset. The parquet results of the data engineering are stored in the `/outputs` folder.
- `/model_creation` - This folder contains notebooks containing the traning and evaluation of machine learning models for the rent price prediction, sale price prediction, and city classification. `model_evaluation.ipynb` is a notebook that contains code to score the models and produce visualizations.
- `/optimization` - This folder contains the code for platypus to utilize multi-objective optimization algorithms to optimize on the problems stored in `problem.py`. The optimization algorithm is changed in the 6th cell of each notebook, where algorithm is defined. (e.g. `algorithm = SMPSO(problem, log_frequency=100)`). Changing `SMPSO` to `NSGAII` or `MOEAD` will result in the alternate algorithm being run.
- `/result_analysis` - This folder contains the code to analyze datasets produced by optimization or data engineering. `city_classifier.ipynb` utilizes the trained city classification model to classify the optimized points by income and density. `datadescribe.ipynb` contains the code to produce DBSCAN analysis and also describes statistics of the datasets.

## The Data
Datasets are stored in the `/data` folder that is not tracked by git. 
- ["USA Real Estate Dataset" by Ahmed Shahriar Sakib](https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset) - House sale data extracted from realtor.com during a period in 2022
- ["USA Housing Listings" by Austin Reese](https://www.kaggle.com/datasets/austinreese/usa-housing-listings) - Rental listing data extracted from craigslist during a period in 2020
- [uszipcode](https://pypi.org/project/uszipcode/) - reverse geocoding data

You have to extract the `simple_db.sqlite` database ([available here](https://github.com/MacHu-GWU/uszipcode-project/releases/download/1.0.1.db/simple_db.sqlite)) from the uszipcode library and place in the `/data` folder along with the datasets.

## Required Libraries
- [Apache Spark and PySpark](https://spark.apache.org/docs/latest/api/python/)
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [numpy](https://numpy.org/)
- [sklearn](https://scikit-learn.org/stable/)
- [tensorflow](https://www.tensorflow.org/)
- [platypus](https://platypus.readthedocs.io/en/latest/index.html)