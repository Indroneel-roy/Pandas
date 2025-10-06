import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)


if __name__ == "__main__":
    # Example usage
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [85, 90, 95]}
    df = pd.DataFrame(data)
    size = getDataframeSize(df)
    print(f"DataFrame size: {size}")