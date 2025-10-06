import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees
    return df.head(3)
if __name__ == "__main__":
    # Example usage
    data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85, 90, 95, 88]}
    df = pd.DataFrame(data)
    first_three_rows = selectFirstRows(df)
    print(first_three_rows)