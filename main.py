import pandas as pd

# import openpyxl

excel_file_path = r"C:\Users\selik\Downloads\MOCK_DATA.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# print(df.tail(5))
# print(df.head(10))
# print(df.info)

# Display the DataFrame
print(df)

# ////////////////////////////////////////////// GETTING OUR ANALYSIS FROM THE DATA //////////////////////////////


# excel_file_path = r"C:\Users\selik\Downloads\MOCK_DATA.xlsx"
#
# # Read the Excel file into a DataFrame
# df = pd.read_excel(excel_file_path)
#
# # Display basic information about the DataFrame
# print("Basic Information about the DataFrame:")
# print(df.info())
#
# # Display descriptive statistics of numeric columns
# print("\nDescriptive Statistics of Numeric Columns:")
# print(df.describe())
#
# # Display the first 10 rows of the DataFrame
# print("\nFirst 10 rows of the DataFrame:")
# print(df.head(10))
#
# # Display the last 5 rows of the DataFrame
# print("\nLast 5 rows of the DataFrame:")
# print(df.tail(5))
#
# # Display the unique values in each column
# print("\nUnique values in each column:")
# for column in df.columns:
#     print(f"{column}: {df[column].unique()}")
#
# # Display the count of missing values in each column
# print("\nCount of Missing Values in Each Column:")
# print(df.isnull().sum())
#
# # Perform additional analysis or visualization as needed based on your specific requirements
# # For example, you can use matplotlib or seaborn for visualization.
#
#
# # more examples
# # pd.merge(): Used to merge multiple DataFrames
#
# # .sum(), .mean(), .min(), .max()
#
# df[['column1', 'column2']]: Used to select specific columns
