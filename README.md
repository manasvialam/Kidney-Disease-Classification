# Kidney-Disease-Classification
Using MLflow and DVC

## Workflow

1. Update config.yaml
2. Update secrets.yaml (optional)
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. Update app.py

# How to run?
...
### STEPS:

Clone the repository

```bash
https://github.com/manasvialam/Kidney-Disease-Classification
```
...
### STEP 01 - Create a conda environment after opening the repository

```bash
conda create -n kidney python=3.12.4 -y
```

``` bash
conda activate kidney
```

...
### STEP 02 - install the requirements
```bash
pip install -r requirements.txt
```

...
##### cmd
- mlflow ui

...
### Dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI = https://dagshub.com/Min/Kidney-Disease-Classification.mlflow
MLFLOW_TRACKING_USERNAME= Min
ML_TRACKING_PASSWORD = Personal token generated in dagshub
python script.py

Run this to export as env variables:


```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/Min/Kidney-Disease-Classification.mlflow
export MLFLOW_TRACKING_USERNAME=Min
export MLFLOW_TRACKING_PASSWORD= personal token from mlflow
```
