from CNN_Classifier import logger
from CNN_Classifier.pipeline.data_ingegstion_01 import DataIngestionTrainingPipeline
from CNN_Classifier.pipeline.base_model_prep_02 import PrepareBaseModelTrainingPipeline
from CNN_Classifier.pipeline.training_03 import ModelTrainingPipeline
from CNN_Classifier.pipeline.evaluation_04 import EvaluationPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f">>>>>>{STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>{STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Training Stage"
try:
        logger.info(f"*******************")
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Evaluation Stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e