import numpy as np
import pandas as pd


def calculate(data):
    print(f"Length val: {len(data)}")

    if len(data) != 9:
        raise ValueError("List need 9 numbers")
    reshaped = np.reshape(data, (3, 3))
    calc = {
        "mean": [
            np.mean(reshaped, axis=0).tolist(),
            np.mean(reshaped, axis=1).tolist(),
            np.mean(reshaped),
        ],
        "variance": [
            np.var(reshaped, axis=0).tolist(),
            np.var(reshaped, axis=1).tolist(),
            np.var(reshaped),
        ],
        "standard deviation": [
            np.std(reshaped, axis=0).tolist(),
            np.std(reshaped, axis=1).tolist(),
            np.std(reshaped),
        ],
        "max": [
            np.max(reshaped, axis=0).tolist(),
            np.max(reshaped, axis=1).tolist(),
            np.max(reshaped),
        ],
        "min": [
            np.min(reshaped, axis=0).tolist(),
            np.min(reshaped, axis=1).tolist(),
            np.min(reshaped),
        ],
        "sum": [
            np.sum(reshaped, axis=0).tolist(),
            np.sum(reshaped, axis=1).tolist(),
            np.sum(reshaped),
        ],
    }
    return calc
