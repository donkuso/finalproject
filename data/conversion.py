import pandas as pd

# Read the XPT file
df = pd.read_sas('data/xpt/RXQ_DRUG.xpt', format='xport')

# Convert to CSV
df.to_csv('data/csv/rxq_drug.csv', index=False)

print("Conversion complete!")