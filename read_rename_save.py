import pandas as pd

index = 0

input_file_name = f"data_{index}.xlsx"
df = pd.read_excel(input_file_name)

input_file_name = f"data_{index}_processed.xlsx"
df.to_excel(input_file_name)

print("*" * 50)
print(df.head(2))
