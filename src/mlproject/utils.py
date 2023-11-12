import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd 
from dotenv import load_dotenv
import pymysql
import pickle
import numpy as np 
import pandas as pd

load_dotenv()
host = os.getenv('host')
user=os.getenv('user')
password=os.getenv('password')
db=os.getenv('db')

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("connection established %s", mydb)
        df=pd.read_sql_query('select * from students', mydb)
        print(df.head())

        return df

    except Exception as ex:
        raise CustomException(ex)

def save_object(file_path, obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path,'wb') as fiel_obj:
            pickle.dump(obj,fiel_obj)
    
    except Exception as e:
        raise CustomException(e)