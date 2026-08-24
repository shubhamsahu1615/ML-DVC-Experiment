import pandas as pd
import os

data = {
    "Name": ["A", "B", "C"],
    "Marks": [80, 85, 90]
}

df = pd.DataFrame(data)

os.makedirs("data", exist_ok=True)

df.to_csv("data/student.csv", index=False)

print("Dataset created successfully.")