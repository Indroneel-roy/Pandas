import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    df = students.dropna(subset = "name")
    return df
if __name__ == "__main__":
    # Example usage
    data = {'student_id': [101, 102, 103, 104], 'name': ['Alice', None, 'Charlie', None], 'age': [20, 21, 22, 23]}
    df = pd.DataFrame(data)
    cleaned_df = dropMissingData(df)
    print(cleaned_df)