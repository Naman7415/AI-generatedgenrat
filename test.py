# # import unittest
# # from unittest.mock import MagicMock

# # # Example class to be tested
# # class MyClass:
# #     def my_method(self, value):
# #         return value * 2

# # # Test case for MyClass
# # class TestMyClass(unittest.TestCase):
# #     def test_my_method(self):
# #         # Create a MagicMock object
# #         mock_obj = MagicMock(spec=MyClass)

# #         # Set up the mock to return a specific value when my_method is called
# #         # mock_obj.my_method.return_value = 'mockedd value'

# #         # Call the mock method
# #         result = mock_obj.my_method('input value')

# #         # Assertions to test the expected behavior
# #         mock_obj.my_method.assert_called_once_with('input value')
# #         self.assertEqual(result, 2)

# # if __name__ == '__main__':
# #     unittest.main()


# # class ProductionClass:
# #     def first(a):
# #         return 4


# # import unittest
# # from unittest.mock import MagicMock


# # class TestMyClass(unittest.TestCase):
# #     def test_my_method(self):
# #         # thing = ProductionClass()

# #         thing = MagicMock(spec=ProductionClass)


# #         thing.method(4)

# #         thing.method.assert_called_with(4)

# # if __name__ == '__main__':
# #     unittest.main()


# # import pandas as pd
# # import unittest
# # from unittest.mock import patch

# # # Example processing function: Capitalize names
# # def process_data(df):
# #     df['name'] = df['name'].apply(lambda x: x.title())
# #     return df

# # class TestProcessData(unittest.TestCase):

# #     @patch('pandas.read_csv')
# #     def setUp(self, mock_read_csv):
# #         # Mock the DataFrame returned by read_csv
# #         mock_read_csv.return_value = pd.DataFrame({
# #             'name': ['naman', 'nikhil'],
# #             'age': [22, 25],
# #             'birth': [1, 3],
# #             'school': ['a', 'c']
# #         })
# #         self.df = pd.read_csv('your_file.csv')  # This now returns the mocked DataFrame

# #     def test_process_data(self):
# #         test_cases = [
# #             {
# #                 'input': {
# #                     'age': 22,
# #                     'name': 'naman',
# #                     'birth': 1,
# #                     'school': 'a'
# #                 },
# #                 'expected_output': {
# #                     'age': 22,
# #                     'name': 'Naman',
# #                     'birth': 1,
# #                     'school': 'a'
# #                 }
# #             },
# #             {
# #                 'input': {
# #                     'age': 25,
# #                     'name': 'nikhil',
# #                     'birth': 3,
# #                     'school': 'c'
# #                 },
# #                 'expected_output': {
# #                     'age': 25,
# #                     'name': 'Nikhil',
# #                     'birth': 3,
# #                     'school': 'c'
# #                 }
# #             }
# #         ]

# #         for case in test_cases:
# #             input_data = case['input']
# #             expected_output = case['expected_output']

# #             # Create a DataFrame from input_data
# #             input_df = pd.DataFrame([input_data])

# #             # Process the data
# #             result_df = process_data(input_df)

# #             # Convert result to a dictionary for comparison
# #             result = result_df.to_dict(orient='records')[0]

# #             # Assert equality
# #             self.assertEqual(result, expected_output)

# # if __name__ == "__main__":
# #     unittest.main()


# # import unittest
# # from unittest.mock import patch, MagicMock
# # import pandas as pd
# # import os

# # class TestDataFrameOperations(unittest.TestCase):

# #     @patch('pandas.DataFrame.to_csv')
# #     def test_save_dataframe(self, mock_to_csv):
# #         # Create a DataFrame as in the original code
# #         data = {
# #             'age': [22, 23, 25],
# #             'name': ['naman', 'raj', 'nikhil'],
# #             'birth': [1, 2, 3],
# #             'school': ['a', 'b', 'c']
# #         }
# #         df = pd.DataFrame(data)

# #         # Call the to_csv method
# #         df.to_csv('your_file.csv', index=False)

# #         # Check that to_csv was called with the correct parameters
# #         mock_to_csv.assert_called_once_with('your_file.csv', index=False)

# #     def test_add_column(self):
# #         # Create a DataFrame as in the original code
# #         data = {
# #             'age': [22, 23, 25],
# #             'name': ['naman', 'raj', 'nikhil'],
# #             'birth': [1, 2, 3],
# #             'school': ['a', 'b', 'c']
# #         }
# #         df = pd.DataFrame(data)

# #         # Check if the new column was added correctly
# #         expected_data = {
# #             'age': [22, 23, 25],
# #             'name': ['naman', 'raj', 'nikhil'],
# #             'birth': [1, 2, 3],
# #             'school': ['a', 'b', 'c'],
# #         }
# #         expected_df = pd.DataFrame(expected_data)

# #         pd.testing.assert_frame_equal(df, expected_df)


# # if __name__ == '__main__':
# #     unittest.main()


# import unittest
# import pandas as pd
# import tempfile
# import os
# from pandas.testing import assert_frame_equal

# class TestDataFrameOperations(unittest.TestCase):

#     def setUp(self):
#         # Create a temporary CSV file
#         self.test_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
#         self.test_file.write(b'age,name,birth,school\n22,naman,1,a\n23,raj,2,b\n25,nikhil,3,c\n')
#         self.test_file.close()

#     def tearDown(self):
#         # Remove the temporary file
#         os.remove(self.test_file.name)

#     def test_read_dataframe(self):
#         # Read from the temporary CSV file
#         df = pd.read_csv(self.test_file.name)

#         # Assert that the DataFrame returned is as expected
#         expected_df = pd.DataFrame({
#             'age': [22, 23, 25],
#             'name': ['naman', 'raj', 'nikhil'],
#             'birth': [1, 2, 3],
#             'school': ['a', 'b', 'c']
#         })
#         assert_frame_equal(df, expected_df)

# if __name__ == '__main__':
#     unittest.main()


import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from pandas.testing import assert_frame_equal
from cs import testnp


# class TestDataFrameOperations(unittest.TestCase):
#         # Load the actual data once
#         # self.actual_df = pd.read_csv("your1_file.csv")

#     @patch("pandas.read_csv")
#     def test_read_dataframe(self, mock_read_csv):
        
        
#         vv = testnp()
        # Create a mock DataFrame to be returned by read_csv

        # mock_df = self.actual_df

        # mock_df = pd.DataFrame({
        #     pd.read_csv('your1_file.csv')
        # })
        # mock_read_csv.return_value = mock_df

        # Read the actual CSV file
        # real_df = pd.read_csv('your1_file.csv')

        # Call the function that uses read_csv (this will use the mock)
        # df = pd.read_csv("your1_file.csv")

        # Check that read_csv was called with the correct parameters
        # mock_read_csv.assert_called_with("your1_file.csv")
        # import pdb;pdb.set_trace()

        # Assert that the columns of the real DataFrame are as expected
        # expected_columns = ['age', 'name', 'birth', 'school']
        # self.assertListEqual(list(real_df.columns), expected_columns)

        # Assert that the mock DataFrame returned is as expected
        
from cs import testnp
        
ejv = {
        'age': [8,6,1],
        'name': ['None','None',2222],
        'birth': ['1995-05-15','last','one'],
        'school': ['None','s','p']
    }

ejv_df = pd.DataFrame(ejv)


sybase = {
        'age': [8,6,3]
    }

sybase_df = pd.DataFrame(sybase)
        
        

        
        
class TestDataFrameOperations(unittest.TestCase):
    
    def test_read_dataframe(self):
        
        dff = testnp(ejv_df,sybase_df)
    
        
        expected_df = pd.DataFrame({
            'age': [8, 6],
            'name': [8 , 6],
            'birth': ['1995-05-15' , 'last'],
            'school': ['None' , 's']
        })
        
        
        
        assert_frame_equal(dff, expected_df)


if __name__ == "__main__":
    unittest.main()




