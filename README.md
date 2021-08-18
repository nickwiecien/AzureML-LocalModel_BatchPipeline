# AzureML-LocalModel_BatchPipeline

Sample code across 3 notebooks demonstrating how to train and export a model locally, register that model in an Azure Machine Learning workspace, and create a reusable batch prediction pipeline to leverage your model to make predictions on new data.

For demonstration purposes, we leverage the [Iris Setosa dataset from Scikit-Learn](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) to train a basic classification model and make predictions. The sample here can be extended to models trained on significantly more complex data for more advanced use cases. The third notebook located in `./03_BatchPredictionPipeline_AML` demonstrates how to load data dynamically to use for inferencing, and how to register these scored/unscored datasets. This code can be modified to pull from additional datastores/sources.

## Environment Setup
<b>Note:</b> Recommend running these notebooks on an Azure Machine Learning Compute Instance using the preconfigured `Python 3.6 - AzureML` environment.

To build and run the sample pipeline contained in `SamplePipeline.ipynb` the following resources are required:
* Azure Machine Learning Workspace