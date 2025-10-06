import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    df = students
    df['grade'] = df['grade'].astype(int)
    return df
if __name__ == "__main__":
    # Example usage with provided students DataFrame
    data = {
        'student_id': [1, 2],
        'name': ['Ava', 'Kate'],
        'age': [6, 15],
        'grade': [73.0, 87.0]
    }
    students_df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(students_df)
    changed_df = changeDatatype(students_df)
    print("\nDataFrame after changing 'grade' to int:")
    print(changed_df)