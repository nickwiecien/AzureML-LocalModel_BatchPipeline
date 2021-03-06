from azureml.core import Run, Workspace, Datastore, Dataset
from azureml.core.model import Model
from azureml.data.datapath import DataPath
import pandas as pd
import os
import argparse
from sklearn.datasets import load_iris
import joblib

# Parse input arguments
parser = argparse.ArgumentParser("Score Inferencing Data")
parser.add_argument('--model_name', type=str, required=True)
parser.add_argument('--scored_dataset', dest='scored_dataset', required=True)

args, _ = parser.parse_known_args()
model_name = args.model_name
scored_dataset = args.scored_dataset

# Get current run
current_run = Run.get_context()

# Get associated AML workspace
ws = current_run.experiment.workspace

# Get default datastore
ds = ws.get_default_datastore()

# Get inferencing dataset
inferencing_dataset = current_run.input_datasets['inferencing_data']
inferencing_data_df = inferencing_dataset.to_pandas_dataframe()

# Get model from workspace - the code below will always retrieve the latest version of the model; specific versions can be targeted.
model_list = Model.list(ws, name=model_name, latest=True)
model_path = model_list[0].download(exist_ok=True)
model = joblib.load(model_path)

# Make predictions with new dataframe
predictions = model.predict(inferencing_data_df)
inferencing_data_df['Predictions']=predictions

# Save scored dataset
os.makedirs(scored_dataset, exist_ok=True)
inferencing_data_df.to_csv(os.path.join(scored_dataset, 'scored_data.csv'), index=False)