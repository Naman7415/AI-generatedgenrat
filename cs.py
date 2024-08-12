# import pandas as pd

# # Create a dictionary with sample data
# data = {
#     'a': ["None", 3, 2, 5, 6, 8]
# }

# # # Create the DataFrame
# df = pd.DataFrame(data)

# # # Replace string 'None' with actual None
# # df = df.replace("None", None)
# print(df.dtypes())


# df=df.dropna(subset=['b','c','d'],how='all')


# # # Condition 1: Exclude rows where all of b, c, d are None
# # condition_1 = df[['b', 'c', 'd']].isna().all(axis=1)

# # # Condition 2: Include rows where at least one of b, c, d is None
# # condition_2 = df[['b', 'c', 'd']].isna().any(axis=1)

# # # Combine conditions: Exclude rows where condition_1 is True but include if condition_2 is True
# # filtered_df = df[condition_2 & ~condition_1]

# # # Save the filtered DataFrame to a CSV file if it contains any rows
# # if not filtered_df.empty:
# #     filtered_df.to_csv('sss.csv', index=False)

# import pdb; pdb.set_trace()

# # Print the filtered DataFrame
# print(filtered_df)



# import pandas as pd

# # Create a dictionary with sample data
# data = {
#             'age': [22, 23, 25],
#             'name': ['naman', 'raj', 'nikhil']
#             # 'birth': [1, 2, 3],
#             # 'school': ['a', 'b', 'bust']
#         }
# df = pd.DataFrame(data)
# df.to_csv('your1_file.csv', index=False)
# print(df)

# Fill NaN values in column 'a' with corresponding values from column 'b




# import pdb;pdb.set_trace()

# Print the updated DataFrame
# print(df)



# import threading

# import time

# def print_numbers():
#     for i in range(1, 6):
#         print("Th", i)
#         time.sleep(1)

# def print_letters():
#     for letter in ['A', 'B', 'C', 'D', 'E']:
#         print("Thread 2:", letter)
#         time.sleep(1)

# # Create two threads
# thread1 = threading.Thread(target=print_numbers)
# # thread  = print_numbers()
# thread2 = threading.Thread(target=print_letters)
# # print(thread1)

# # Start the threads
# thread1.start()
# thread2.start()

# # Wait for the threads to complete
# thread1.join()
# thread2.join()

# print("Execution completed.")




import pandas as pd

ejv = {
        'age': [25,44,1],
        'name': ['None','None',2222],
        'birth': ['1995-05-15','last','one'],
        'school': ['None','s','p']
    }

ejv_df = pd.DataFrame(ejv)


sybase = {
        'age': [25,4,1]
    }
sybase_df = pd.DataFrame(sybase)




def testnp(ejv_df,sybase_df):
    
    # import pdb;pdb.set_trace()
    
    
    ejv_df['name'] = ejv_df.apply(lambda row: row['age'] if row['name'] == 'None' else row['name'], axis=1)
    
    new_ejv =  ejv_df[ejv_df['age'].isin(sybase_df['age'])]
    
    return new_ejv

    
    
    














# import pdb;pdb.set_trace()

# Check data types of columns
# print(df.dtypes)
