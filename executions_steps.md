1) we create required files such as requirement.txt,readme,gitigore and setup.py
2) setup.py file is used to create our whole ml project as a package
3) we write a code in setup file such that in whichever package or folder the __init__ is identified the folder is considered as  the package and the folder is build and we can import it any where just like other libraries like pandas ,numpy etc
4) Now we create a component folder in the src folder with init.py file
5) And inside the component folder we first create our 1st component called DATA INGESTION
which is nothing but import data from various sources such as web, dataset or other sources and using the data inside our coding env.writing a code in this data ingestion file to read the data from various sources 
6) Now also we create a data transformation file which is used for transforming the data such as label encoding, values conversion etc can be done in this file 
7) Creating model in model_trainer file which can be used to specify which model we are using and used to train our model same file can be used to push our model to sources
8) Now we create a pipeline folder which can be of 2 types :    
    a.Training pipeline:
    contains a set of instruction to train our model by calling the files inside the component folder 
    b.Predict pipeline:
    contains set of instruction for predicting model on new data.  
9) Now we create files such as exception.py, logger.py for tracking or logging each operation or to keep the track and utils.py that can be used to get the data from database online or upload our model to online database server etc
10) In this project we are using the dataset student and make model for student performace indicator. we choose this dataset because this dataset consist multiple errors or null values which can be removed using eda. which help us to learn and implement eda and also how to handle uncertain data
11) Now we perform eda and in eda.ipynb and we now start model training in model_training.ipynb file
12) So as our problem statement is regression problem we will try to use all the regression problem algos to see which performs best on this dataset 
13) After the model training we then do the data ingestion in which data from any source is collected and splitted into the raw, train and test data by creating there folders 

14) Now we do the data transformation in which we convert our data from categorical to numnerical or we also change the numerical value or scale it accordingly 
15) for this we use pipelines for numberical and categorical values which at once deals with both the columns, we create a seperate pipelines for numerical and categorical columns 
16) After data transformation we create a model trainer file in which we will test best regression model which will give best accuracy 
17) We trained our model by trying all the best possible models and we got the best model as linear regression with 87% accuracy 
18) We can tune our model based upon our model called as hyper parameter tuning 