
import pandas as pd

# Load the data
data = {
    "APELIDO": [
        "RESP_8", "RESP_4", "RESP_13", "RESP_2", "RESP_14", "RESP_10", "RESP_5",
        "RESP_3", "RESP_12", "RESP_6", "RESP_1", "RESP_9", "RESP_7", "RESP_11"
    ],
    "RQ1_MESES": [60, 48, 104, 36, 120, 6, 60, 2, 19, 17, 12, 21, 1, 166],
    "RQ2_MESES": [144, 24, 32, 12, 8, 30, 22, 20, 33, 17, 4, 46, 21, 45],
    "RQ3_MESES": [48, 60, 96, 78, 60, 30, 60, 156, 108, 60, 78, 96, 48, 86]
}

df = pd.DataFrame(data)

# Convert months to years
df["RQ1_ANOS"] = df["RQ1_MESES"] / 12
df["RQ2_ANOS"] = df["RQ2_MESES"] / 12
df["RQ3_ANOS"] = df["RQ3_MESES"] / 12

# Summary statistics
print("Summary Statistics (in Years):")
print(df[["RQ1_ANOS", "RQ2_ANOS", "RQ3_ANOS"]].describe())
