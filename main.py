from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTraningPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTraningPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation_mlflow import EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base model"
try:
    logger.info(f"********************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    prepare_base_model= PrepareBaseModelTraningPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Training"
try:
    logger.info(f"********************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    prepare_base_model= ModelTraningPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Evaluation stage"
try:
    logger.info(f"********************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    prepare_base_model= EvaluationPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e