from azureml.core import Run, Workspace, Datastore, Dataset
from azureml.core.model import Model
from azureml.data.datapath import DataPath
import pandas as pd
import os

# Parse input arguments
parser = argparse.ArgumentParser("Register File Dataset")
parser.add_argument('--sample_file_dataset', dest='sample_file_dataset', required=True)

args, _ = parser.parse_known_args()
sample_file_dataset = args.sample_file_dataset

# Get current run
current_run = Run.get_context()

# Get associated AML workspace
ws = current_run.experiment.workspace

# Get default datastore
ds = ws.get_default_datastore()

# Generate random sample data
random_df = pd.util.testing.makeDataFrame()
print(random_df)

random_df2 = pd.util.testing.makeDataFrame()
print(random_df2)

# Save file dataset
os.makedirs(sample_file_dataset, exist_ok=True)
random_df.to_csv(os.path.join(sample_file_dataset, 'sample_data.csv'))
random_df2.to_csv(os.path.join(sample_file_dataset, 'sample_data_2.csv'))