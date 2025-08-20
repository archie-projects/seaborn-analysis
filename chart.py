import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set style and context for professional look
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1.2)

# Generate synthetic data
np.random.seed(42)  # For reproducibility
n_samples = 200
acquisition_cost = np.random.uniform(50, 500, n_samples)
# Create lifetime value somewhat correlated with acquisition cost plus noise
lifetime_value = acquisition_cost * np.random.uniform(2, 5, n_samples) + np.random.normal(0, 200, n_samples)

# Build DataFrame
data = pd.DataFrame({
    'Acquisition Cost ($)': acquisition_cost,
    'Lifetime Value ($)': lifetime_value
})

# Create figure with exact size and dpi to get 512x512 pixels
plt.figure(figsize=(8, 8), dpi=64)

# Scatterplot with edge colors and a color palette
sns.scatterplot(
    data=data,
    x='Acquisition Cost ($)',
    y='Lifetime Value ($)',
    hue='Lifetime Value ($)',
    palette='viridis',
    legend=False,
    edgecolor='black',
    s=80  # marker size
)

# Titles and labels
plt.title('Customer Lifetime Value vs Acquisition Cost', fontsize=18, weight='bold')
plt.xlabel('Customer Acquisition Cost ($)', fontsize=14)
plt.ylabel('Customer Lifetime Value ($)', fontsize=14)

# Save the figure WITHOUT bbox_inches='tight' to preserve exact size
plt.savefig('chart.png')
plt.close()
