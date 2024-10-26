import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Set your working directory
work_dir = "/Users/michaelkokorudz/Desktop/McGill-FIAM Asset Management Hackathon"  # Update to your path
sample_file_path = os.path.join(work_dir, "hackathon_sample_v2.csv")
factor_file_path = os.path.join(work_dir, "factor_char_list.csv")

# Load the dataset and stock variable list
raw = pd.read_csv(sample_file_path, parse_dates=["date"], low_memory=False)
stock_vars = list(pd.read_csv(factor_file_path)["variable"].values)

# Data cleaning: Remove rows where target variable is missing
ret_var = "stock_exret"
new_set = raw[raw[ret_var].notna()].copy()

# Group the data by month and perform rank transformation on stock variables
monthly = new_set.groupby("date")
data = pd.DataFrame()

for date, monthly_raw in monthly:
    group = monthly_raw.copy()
    for var in stock_vars:
        var_median = group[var].median(skipna=True)
        group[var] = group[var].fillna(var_median)
        group[var] = group[var].rank(method="dense") - 1
        group_max = group[var].max()
        if group_max > 0:
            group[var] = (group[var] / group_max) * 2 - 1
        else:
            group[var] = 0
    data = data._append(group, ignore_index=True)

# Use only the stock variables for PCA
X = data[stock_vars]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform PCA
pca = PCA()
pca.fit(X_scaled)

# Calculate explained variance ratio
explained_variance_ratio = pca.explained_variance_ratio_

# Create a scree plot
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio.cumsum(), marker='o', linestyle='--')
plt.title('Scree Plot')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance')
plt.grid(True)
plt.show()
