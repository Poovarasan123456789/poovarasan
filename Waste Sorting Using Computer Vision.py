# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HPTfM3trjrwJzc4rNDiYIzOhAVL7oXwo
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv('/content/waste_dataset (1) - Copy.csv')  # Replace with your actual file path

# Set the style
sns.set(style="whitegrid")

# Create subplots
fig, axes = plt.subplots(3, 1, figsize=(10, 18))

# 1. Count Plot - Waste Type Frequency
sns.countplot(data=df, x='label', ax=axes[0], palette='Set2')
axes[0].set_title('Count of Waste Types')
axes[0].set_xlabel('Waste Type')
axes[0].set_ylabel('Count')

# 2. Box Plot - Brightness Distribution by Waste Type
sns.boxplot(data=df, x='label', y='brightness', ax=axes[1], palette='Set3')
axes[1].set_title('Brightness Distribution by Waste Type')
axes[1].set_xlabel('Waste Type')
axes[1].set_ylabel('Brightness')

# 3. Scatter Plot - Brightness vs Sharpness
sns.scatterplot(data=df, x='brightness', y='sharpness', hue='label', style='label', ax=axes[2], palette='Set1', s=100)
axes[2].set_title('Brightness vs. Sharpness by Waste Type')
axes[2].set_xlabel('Brightness')
axes[2].set_ylabel('Sharpness')

# Layout adjustment
plt.tight_layout()
plt.show()