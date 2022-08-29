from pandas import read_csv


def get_train_valid():
    train = read_csv("input/train.csv")
    valid = read_csv("input/test.csv")
    # sub = read_csv("/input/sample_submission.csv")
    
    return train, valid#, sub


