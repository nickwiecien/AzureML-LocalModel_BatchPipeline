from azureml.core import Run, Workspace, Datastore, Dataset
from azureml.data.datapath import DataPath
import pandas as pd
import os
import argparse
from sklearn.datasets import load_iris
import snowflake.connector

#Parse input arguments
parser = argparse.ArgumentParser("Get Inferencing Data")
parser.add_argument('--get_data_param_1', type=str, required=True)
parser.add_argument('--get_data_param_2', type=str, required=True)
parser.add_argument('--get_data_param_3', type=str, required=True)
parser.add_argument('--inferencing_dataset', dest='inferencing_dataset', required=True)

# Note: the get_data_param args below are included only as an example of argument passing.
# They are not consumed in the code sample shown here.
args, _ = parser.parse_known_args()
get_data_param_1 = args.get_data_param_1
get_data_param_2 = args.get_data_param_2
get_data_param_3 = args.get_data_param_3
inferencing_dataset = args.inferencing_dataset

#Get current run
current_run = Run.get_context()

#Get associated AML workspace
ws = current_run.experiment.workspace

#Get default datastore
ds = ws.get_default_datastore()

# Load data from Snowflake
# See example here: https://docs.snowflake.com/en/user-guide/python-connector-pandas.html#writing-data-from-a-pandas-dataframe-to-a-snowflake-database

# Here we are using the iris dataset from sklearn solely for demonstration purposes
data = load_iris(as_frame=True)
df = data.data

# Save dataset for consumption in next pipeline step
os.makedirs(inferencing_dataset, exist_ok=True)
df.to_csv(os.path.join(inferencing_dataset, 'inferencing_data.csv'), index=False)
