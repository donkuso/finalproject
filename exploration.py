import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv('data/merged_nhanes.csv')

print("="*70)
print("NHANES DATA EXPLORATION")
print("="*70)

# Filter to women only (RIAGENDR: 2 = Female)
women = df[df['RIAGENDR'] == 2].copy()
print(f"\nTotal women in dataset: {len(women):,}")
print(f"Total variables: {len(women.columns)}")

# ============================================================================
# 1. EXPLORE MENOPAUSAL STATUS VARIABLES
# ============================================================================
print("\n" + "="*70)
print("MENOPAUSAL STATUS VARIABLES")
print("="*70)

# RHQ031: Had at least one period in past 12 months (1=Yes, 2=No, 7=Refused, 9=Don't know)
print("\nRHQ031 - Had period in past 12 months:")
print(women['RHQ031'].value_counts(dropna=False).sort_index())
print(f"Missing: {women['RHQ031'].isna().sum()}")

# RHQ060: Age when had last menstrual period
print("\nRHQ060 - Age at last period:")
rhq060_valid = women[women['RHQ060'] > 0]['RHQ060']
print(f"Valid responses: {len(rhq060_valid)}")
if len(rhq060_valid) > 0:
    print(f"Range: {rhq060_valid.min():.0f} to {rhq060_valid.max():.0f}")
    print(f"Mean: {rhq060_valid.mean():.1f}")

# RHQ074: Reason stopped having periods (1=Pregnancy, 2=Menopause, etc.)
print("\nRHQ074 - Reason stopped having periods:")
print(women['RHQ074'].value_counts(dropna=False).sort_index())

# ============================================================================
# 2. EXPLORE PHQ-9 DEPRESSION VARIABLES
# ============================================================================
print("\n" + "="*70)
print("PHQ-9 DEPRESSION VARIABLES (DPQ)")
print("="*70)

dpq_vars = ['DPQ010', 'DPQ020', 'DPQ030', 'DPQ040', 'DPQ050', 
            'DPQ060', 'DPQ070', 'DPQ080', 'DPQ090']

print("\nMissing data by PHQ-9 item:")
for var in dpq_vars:
    n_valid = women[var].notna().sum()
    n_missing = women[var].isna().sum()
    print(f"  {var}: {n_valid:,} valid, {n_missing:,} missing")

# Check DPQ010 values (should be 0-3: Not at all, Several days, More than half, Nearly every day)
print("\nDPQ010 value distribution:")
print(women['DPQ010'].value_counts(dropna=False).sort_index())

# ============================================================================
# 3. EXPLORE DEMOGRAPHIC VARIABLES
# ============================================================================
print("\n" + "="*70)
print("DEMOGRAPHIC VARIABLES")
print("="*70)

# Age
print("\nRIDAGEYR - Age in years:")
age_valid = women[women['RIDAGEYR'] > 0]['RIDAGEYR']
print(f"Valid ages: {len(age_valid):,}")
print(f"Range: {age_valid.min():.0f} to {age_valid.max():.0f}")
print(f"Mean: {age_valid.mean():.1f}")

# Race/ethnicity (RIDRETH3)
print("\nRIDRETH3 - Race/ethnicity:")
print(women['RIDRETH3'].value_counts(dropna=False).sort_index())

# Education (DMDEDUC2)
print("\nDMDEDUC2 - Education level:")
print(women['DMDEDUC2'].value_counts(dropna=False).sort_index())

# Poverty income ratio
print("\nINDFMPIR - Poverty income ratio:")
pir_valid = women[women['INDFMPIR'] > 0]['INDFMPIR']
print(f"Valid responses: {len(pir_valid):,}")
if len(pir_valid) > 0:
    print(f"Range: {pir_valid.min():.2f} to {pir_valid.max():.2f}")
    print(f"Mean: {pir_valid.mean():.2f}")

# ============================================================================
# 4. AGE DISTRIBUTION BY MENOPAUSAL STATUS
# ============================================================================
print("\n" + "="*70)
print("AGE BY MENOPAUSAL STATUS")
print("="*70)

# Women who had period in past 12 months
had_period = women[(women['RHQ031'] == 1) & (women['RIDAGEYR'] > 0)]
print(f"\nWomen with period in past 12 months (RHQ031=1): {len(had_period):,}")
if len(had_period) > 0:
    print(f"  Age range: {had_period['RIDAGEYR'].min():.0f} to {had_period['RIDAGEYR'].max():.0f}")
    print(f"  Mean age: {had_period['RIDAGEYR'].mean():.1f}")

# Women who did NOT have period in past 12 months
no_period = women[(women['RHQ031'] == 2) & (women['RIDAGEYR'] > 0)]
print(f"\nWomen WITHOUT period in past 12 months (RHQ031=2): {len(no_period):,}")
if len(no_period) > 0:
    print(f"  Age range: {no_period['RIDAGEYR'].min():.0f} to {no_period['RIDAGEYR'].max():.0f}")
    print(f"  Mean age: {no_period['RIDAGEYR'].mean():.1f}")

print("\n" + "="*70)
print("EXPLORATION COMPLETE")
print("="*70)