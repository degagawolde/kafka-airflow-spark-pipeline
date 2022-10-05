import unittest
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join("./scripts")))
from scripts.data_extractor import DataExtractor

class TestDataExtraction(unittest.TestCase):
    
    def setUp(self) -> None:
        self.dataext = DataExtractor()
        self.csv_file = './data/original_test_data.csv'
        self.csv_save = './data/saved_test_data.csv'
        self.df = pd.DataFrame({'a':[1,2,3],'b':['a','b','c']})
   
    def test_read_csv(self):
        self.assertIsNotNone(
            self.dataext.read_csv(self.csv_file))

    def test_save_df(self):
        self.assertIsNone(self.dataext.save_df(self.df,self.csv_save))
    
    def test_extract_columns(self):
        self.assertIsInstance(list(self.dataext.extract_columns(self.df)),list)

if __name__ == "__main__":
    unittest.main()