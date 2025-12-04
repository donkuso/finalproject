

def classify_menopausal_status(row):
    age = row['RIDAGEYR']
    had_period = row['RHQ031']  # Had period in past 12 months
    age_last_period = row['RHQ060']  # Age at last period
    
    if had_period == 1 and age < 45:
        return 'Premenopausal'
    elif had_period == 1 and age >= 45:
        return 'Perimenopausal'
    elif had_period == 2 and (age - age_last_period) < 1:
        return 'Perimenopausal'  # Recently stopped (within 1 year)
    elif had_period == 2 and (age - age_last_period) >= 1:
        return 'Postmenopausal'
    else:
        return 'Unknown'

def classify_depression(row):
    dpq_vars = ['DPQ010', 'DPQ020', 'DPQ030', 'DPQ040', 'DPQ050', 
            'DPQ060', 'DPQ070', 'DPQ080', 'DPQ090']
    