import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(
        index = "month", 
        columns = "city",
        values = "temperature"

    )
if __name__ == "__main__":
    # Example usage
    data = {
        'month': ['Jan', 'Jan', 'Feb', 'Feb'],
        'city': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
        'temperature': [30, 60, 32, 62]
    }
    df = pd.DataFrame(data)
    pivoted_df = pivotTable(df)
    print(pivoted_df)