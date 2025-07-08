import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV (make sure sales_data.csv is in the same folder)
df = pd.read_csv("sales_data.csv")

# Show first few rows
print(df.head())

# Simple barplot
sns.barplot(x="Product", y="Sales", data=df)
plt.title("Sales by Product")
plt.show()
