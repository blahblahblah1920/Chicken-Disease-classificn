from CNN_Classifier.constants import *
from CNN_Classifier.entity.config_entity import DataIngestionCongig
from CNN_Classifier.utilities.common import read_yaml, create_directories

class ConfigurationManager:
    def __init__(
        self, config_path = CONFIG_FILE_PATH, params_path = PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_path) # returns all the files from the yaml file
        self.params = read_yaml(params_path)
        
        create_directories([self.config.artifacts_root]) # since we used box type we can call the value using the "."
        
    def get_data_ingestion_config(self) -> DataIngestionCongig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionCongig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        
        return data_ingestion_config