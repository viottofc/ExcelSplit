import pandas as pd

# Load the data from the Excel file into a pandas DataFrame
df = pd.read_excel('file.xlsx')

# Calculate the number of files that will be created
num_files = len(df) // 1000 + 1

# Split the DataFrame into multiple DataFrames, each with 1000 rows or less
for i in range(num_files):
    start = i * 1000
    end = (i + 1) * 1000
    df_chunk = df[start:end]
    df_chunk.to_excel(f'file_{i}.xlsx', index=False)
