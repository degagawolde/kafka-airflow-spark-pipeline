import json
import pandas as pd


class DataExtractor:
    """
    this class is used to extract csv files and load them to 
    pandas data frame
    """

    def __init__(self) -> None:
        pass

    def read_csv(self, csv_file):
        """
        opend and read csv_file
        Args:        
        csv_file: - path to the csv file

        Returns:
        dataframe conataining data extracted csv file

        """

        return pd.read_csv(csv_file)

    def save_df(self, df, filename):
        df.to_csv(filename)
        print('Successfuly saved!')
    
    def extract_columns(self, df):
        return df.columns