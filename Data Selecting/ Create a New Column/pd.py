import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees
    df['bonus'] = df['salary'] * 2
    return df
if __name__ == "__main__":
    # Example usage
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'salary': [50000, 60000, 70000]}
    df = pd.DataFrame(data)
    df_with_bonus = createBonusColumn(df)
    print(df_with_bonus)