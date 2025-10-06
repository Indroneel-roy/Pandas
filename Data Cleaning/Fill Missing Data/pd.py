import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    df = products
    df['quantity'] = df['quantity'].fillna(0)
    return df
if __name__ == "__main__":
    # Example usage with provided products DataFrame
    data = {
        'product_id': [1, 2, 3, 4],
        'product_name': ['Apple', 'Banana', 'Orange', 'Grapes'],
        'quantity': [10, None, 5, None]
    }
    products_df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(products_df)
    filled_df = fillMissingValues(products_df)
    print("\nDataFrame after filling missing 'quantity' values with 0:")
    print(filled_df)    