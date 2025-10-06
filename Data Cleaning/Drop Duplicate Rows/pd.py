import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    df = customers.drop_duplicates(subset = "email")
    return df

if __name__ == "__main__":
    data = {
        'customer_id': [1, 2, 3, 4, 5, 6],
        'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
        'email': [
            'emily@example.com',
            'michael@example.com',
            'sarah@example.com',
            'john@example.com',
            'john@example.com',
            'alice@example.com'
        ]
    }
    customers_df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(customers_df)
    print("\nDataFrame after dropping duplicate emails:")
    print(dropDuplicateEmails(customers_df))



