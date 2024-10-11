import pandas as pd


def read_data(path = "spam_ham_dataset.csv") -> (pd.DataFrame, pd.DataFrame):
    # read csv local file
    df = pd.read_csv(path).head(400) # for train on my laptop
    # drop usless columns 
    df = df.drop(columns=["Unnamed: 0", "label_num"])
    # split X | y
    X = df.drop(columns=["label"])
    y = df["label"]
    
    return [X, y]
    
    
read_data()