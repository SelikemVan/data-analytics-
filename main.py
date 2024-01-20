import pandas as pd
# import openpyxl

excel_file_path = r"C:\Users\selik\Downloads\MOCK_DATA.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# print(df.tail(5))
# print(df.head(10))
print(df.info)

# Display the DataFrame
print(df)
