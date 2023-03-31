import os

for index in range(3):
    file_name = f"data_{index}_processed.xlsx"
    os.remove(file_name)

    print("*" * 30)
    print(f"{file_name} was deleted successfully ! ")
