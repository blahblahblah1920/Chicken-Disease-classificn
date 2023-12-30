from CNN_Classifier import logger
from CNN_Classifier.pipeline.data_ingegstion_01 import DataIngestionTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>{STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>{STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e