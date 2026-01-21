import sys
import os
from src.logger import logger
from src.exception import CustomException
import pandas as pd
from src.utils import load_object

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            data_scaled = preprocessor.transform(features)

            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            logger.error("Error occurred in prediction pipeline")
            raise CustomException(e, sys)
        
        
        
        