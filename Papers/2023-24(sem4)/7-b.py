import pandas as pd
data = {"Name" : ["A","B","C","D","E"],
        "MARKS-OF-COA":[56,56,34,45,62],
        "MARKS-OF-DS":[63,68,56,32,53],
        "MARKS-OF-PYTHON":[43,42,32,5,33]
        }
df = pd.DataFrame(data)
print(df)

# print(df.sort_values("MARKS-OF-COA"))