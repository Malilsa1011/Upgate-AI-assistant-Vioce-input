import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
n_samples = 1000

data = {
    "gender": np.random.choice([0, 1], n_samples),  # 0 = Female, 1 = Male
    "age": np.random.randint(1, 90, n_samples),    # Age 1-90
    "temperature": np.random.uniform(36.0, 41.0, n_samples),
    "bp_systolic": np.random.randint(90, 180, n_samples),
    "bp_diastolic": np.random.randint(60, 120, n_samples),
    "heart_rate": np.random.randint(60, 120, n_samples),
    "fever": np.random.choice([0, 1], n_samples),
    "cough": np.random.choice([0, 1], n_samples),
    "fatigue": np.random.choice([0, 1], n_samples),
    "diagnosis": np.random.choice(["Healthy", "Flu", "Hypertension", "Other"], n_samples),
}

# Create DataFrame
df = pd.DataFrame(data)
df.to_csv("synthetic_diagnosis_data_with_age_gender.csv", index=False)
print("Synthetic dataset created.")