import pandas as pd

# -----------------------------------------------------------------------------------
index = 0
input_file_name = f"data_{index}.xlsx"
df = pd.read_excel(input_file_name)
input_file_name = f"data_{index}_processed.xlsx"
df.to_excel(input_file_name)
print("*" * 50)
print(df.head(2))
# -----------------------------------------------------------------------------------
index = 1
df = pd.read_excel(f"data_{index}.xlsx")
df.to_excel(f"data_{index}_processed.xlsx")
print("*" * 50)
print(df.head(2))
# -----------------------------------------------------------------------------------
index = 2
df = pd.read_excel(f"data_{index}.xlsx")
df.to_excel(f"data_{index}_processed.xlsx")
print("*" * 50)
print(df.head(2))
# -----------------------------------------------------------------------------------
