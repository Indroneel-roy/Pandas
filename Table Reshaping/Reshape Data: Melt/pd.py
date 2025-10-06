import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(
        id_vars=["product"],
        value_vars=["quarter_1", "quarter_2", "quarter_3", "quarter_4"],
        var_name="quarter",
        value_name="sales"
    )
if __name__ == "__main__":
    # Example usage
    data = {
        'product': ['A', 'B', 'C'],
        'quarter_1': [150, 200, 250],
        'quarter_2': [160, 210, 260],
        'quarter_3': [170, 220, 270],
        'quarter_4': [180, 230, 280]
    }
    df = pd.DataFrame(data)
    melted_df = meltTable(df)
    print(melted_df)