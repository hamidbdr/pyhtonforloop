import pandas as pd

for index in range(3):
    df = pd.read_excel(f"data_{index}.xlsx")
    df.to_excel(f"data_{index}_processed.xlsx")

    print("*" * 30)
    print(df.head(2))
