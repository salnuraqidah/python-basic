import pandas as pd
import numpy as np

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

df2

# https://colab.research.google.com/drive/1MbyUSpEpM-_dqgJHwQEJ_0htb-MOHEi9?usp=sharing