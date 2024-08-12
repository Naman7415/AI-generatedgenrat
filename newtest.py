import unittest
import pandas as pd
from io import StringIO



class TestGetColumnNames(unittest.TestCase):
    
       
    
    def test_get_column_names(self):
        
        real_df = pd.read_csv("your1_file.csv")
        
        # Call the function to get column names
        
        # Define the expected columns
        expected_columns = ['age', 'name']
        
        # Check if the columns match
        self.assertListEqual(list(real_df.columns), expected_columns)

if __name__ == '__main__':
    unittest.main()
