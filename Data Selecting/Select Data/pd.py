import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df = students
    return df.loc[df['student_id'] == 101, ["name", "age"]]
if __name__ == "__main__":
    # Example usage
    data = {'student_id': [101, 102, 103], 'name': ['Alice', 'Bob', 'Charlie'], 'age': [20, 21, 22]}
    df = pd.DataFrame(data)
    selected_data = selectData(df)
    print(selected_data)