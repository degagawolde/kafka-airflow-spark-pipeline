import pandas as pd


class DataManipulator:
    def __init__(self, df: pd.DataFrame):
        """
            Returns a DataManipulator Object with the passed DataFrame Data set as its own DataFrame
            Parameters
            ----------
            df:
                Type: pd.DataFrame
            Returns
            -------
            None
        """
        self.df = df
        
    def add_word_len(self, df, col) -> pd.DataFrame:
        df['word_len'] = self.df[col].str.split().str.len()
        return df
    
