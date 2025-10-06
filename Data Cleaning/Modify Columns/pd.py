import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees
    df['salary'] = df['salary'] * 2
    return df
if __name__ == "__main__":
    # Example usage
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'salary': [50000, 60000, 70000]}
    df = pd.DataFrame(data)
    modified_df = modifySalaryColumn(df)
    print(modified_df)