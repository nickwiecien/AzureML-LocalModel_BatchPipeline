from azureml.core import Run, Workspace, Datastore, Dataset
import pandas as pd
import snowflake.connector

print('hello world')

#Get current run
current_run = Run.get_context()

#Get associated AML workspace
ws = current_run.experiment.workspace

#Print workspace details
print(ws)
