import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    column_mapping = {
        "id": "student_id",
        "first": "first_name", 
        "last": "last_name",
        "age": "age_in_years"
    }

    students.rename(columns=column_mapping, inplace=True)
    return students
if __name__ == "__main__":
    # Example usage
    data = {'id': [1, 2, 3], 'first': ['Alice', 'Bob', 'Charlie'], 'last': ['Smith', 'Jones', 'Brown'], 'age': [20, 21, 22]}
    df = pd.DataFrame(data)
    renamed_df = renameColumns(df)
    print(renamed_df)