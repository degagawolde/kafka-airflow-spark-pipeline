import re
import pandas as pd
import seaborn as sns  
import matplotlib.pyplot as plt 
sns.set_style("darkgrid")

from logger import get_logger

_logger = get_logger("FileHandler")
_logger.debug("Loaded successfully!")

class FileHandler():

    def __init__(self):
        pass
    
    def save_csv(self, df, csv_path, index=False):
        try:
            df.to_csv(csv_path, index=index)
            _logger.info("File saved as csv")

        except Exception:
            _logger.exception("File saving failed")

    def read_csv(self, csv_path):
        try:
            df = pd.read_csv(csv_path)
            _logger.debug("File is read as csv")
            return df

        except FileNotFoundError:
            _logger.exception("File is not found")

    def article_category_partition(self, df, start, end): 
        """Split the articles and associate them with their category
        Parameters
        ----------
            df: DataFrame
                - a pandas DataFrame which represent the total dataset to be partitioned
                
            start: int
                - a DataFrame starting index to start the partition 
                
            end: int
                - a DataFrame ending index to partition the DataFrame upto 
            
        Return
        ------
            pandas DataFrame
            - a pandas DataFrame which combine the article with its category
        """
        try:
            combined = []
            for i in range(start, end): 
                txt_map = [*map(lambda s: s.strip(), re.split(pattern=r'[።"?]', string=df['article'][i]))] 
                txt_map = filter(lambda x: len(x) > 0 and len(x.split()) > 2 and len(x.split()) < 15, txt_map)
                combined.extend([{"category":df['category'][i], 'text': sen} for sen in txt_map])
            
            _logger.info("Article splitted and combined with its category successfully")

        except Exception:
            _logger.exception("Partition failed")
                                
        return pd.DataFrame(combined)