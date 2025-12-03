import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([df1, df2])
    return df
if __name__ == "__main__":
    # Example usage
    data1 = {'student_id': [101, 102], 'name': ['Alice', 'Bob'], 'age': [20, 21]}
    data2 = {'student_id': [103, 104], 'name': ['Charlie', 'David'], 'age': [22, 23]}
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    concatenated_df = concatenateTables(df1, df2)
    print(concatenated_df)
    print(data1)
