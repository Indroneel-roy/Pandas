import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    new_df = animals[animals["weight"] > 100]
    return new_df.sort_values("weight", ascending=False)[["name"]]
if __name__ == "__main__":
    # Example usage
    data = {'name': ['Elephant', 'Tiger', 'Dog', 'Cat'], 'weight': [1200, 220, 50, 10]}
    df = pd.DataFrame(data)
    heavy_animals = findHeavyAnimals(df)
    print(heavy_animals)