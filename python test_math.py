import numpy as np
import pandas as pd

# Create a small dataset (like a mini-Excel sheet)
data = {
    'Hours_Studied': [2, 5, 8, 10],
    'Test_Score': [50, 70, 85, 95]
}

df = pd.DataFrame(data)

# Calculate the average score using NumPy
average = np.mean(df['Test_Score'])

print("--- MIAR Data Analysis ---+++++")
print(df)
print(f"\nThe average test score is: {average}")