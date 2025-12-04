import pandas as pd
import os

print("Files found:", os.listdir("data/csv"))

# Path to CSV folder
DATA_PATH = "data/csv"

# Load each dataset
rhq = pd.read_csv(os.path.join(DATA_PATH, "p_rhq.csv"))
slq = pd.read_csv(os.path.join(DATA_PATH, "p_slq.csv"))
rx = pd.read_csv(os.path.join(DATA_PATH, "p_rxq_rx.csv"))
mcq = pd.read_csv(os.path.join(DATA_PATH, "p_mcq.csv"))
dpq = pd.read_csv(os.path.join(DATA_PATH, "p_dpq.csv"))
bmx = pd.read_csv(os.path.join(DATA_PATH, "p_bmx.csv"))
demo = pd.read_csv(os.path.join(DATA_PATH, "p_demo.csv"))   # if you have it

# Start merging — demographics first
merged = demo

merged = merged.merge(rhq, on="SEQN", how="left")
merged = merged.merge(slq, on="SEQN", how="left")
merged = merged.merge(dpq, on="SEQN", how="left")
merged = merged.merge(bmx, on="SEQN", how="left")
merged = merged.merge(mcq, on="SEQN", how="left")
merged = merged.merge(rx, on="SEQN", how="left")

# Save final combined dataset
merged.to_csv("data/merged_nhanes2.csv", index=False)