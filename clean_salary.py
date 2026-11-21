from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent
IN_PATH = BASE / "Salary_Data.csv"
OUT_PATH = BASE / "Salary_Data_clean.csv"

df = pd.read_csv(IN_PATH)
print(f"Raw shape: {df.shape}")

# 1. Standardise column names -> snake_case
df.columns = (df.columns.str.strip().str.lower()
              .str.replace(r"\s+", "_", regex=True))

# 2. Strip whitespace in all text columns
text_cols = ["gender", "education_level", "job_title"]
for c in text_cols:
    df[c] = df[c].str.strip()

# 3. Fix inconsistent categories
df["education_level"] = df["education_level"].replace({
    "Bachelor's": "Bachelor's Degree",
    "Master's": "Master's Degree",
    "phD": "PhD",
})

df["job_title"] = df["job_title"].replace({
    "Juniour HR Coordinator": "Junior HR Coordinator",
    "Juniour HR Generalist": "Junior HR Generalist",
    "Front end Developer": "Front End Developer",
    "Back end Developer": "Back End Developer",
    "Social M": "Social Media Manager",        # truncated
    "Social Media Man": "Social Media Manager",  # truncated
    "Customer Service Rep": "Customer Service Representative",
})

# 4. Drop rows with missing values (only ~6 rows, so dropping is safe)
before = len(df)
df = df.dropna()
print(f"Dropped {before - len(df)} rows with missing values")

# 5. Remove exact duplicates (huge in this file)
before = len(df)
df = df.drop_duplicates()
print(f"Dropped {before - len(df)} duplicate rows")

# 6. Fix dtypes (floats -> ints where they are whole numbers)
df["age"] = df["age"].astype(int)
df["years_of_experience"] = df["years_of_experience"].astype(int)
df["salary"] = df["salary"].astype(int)

# 7. Remove impossible / suspicious values
before = len(df)
df = df[df["salary"] >= 10_000]                                # e.g. salary = 350
df = df[df["years_of_experience"] <= df["age"] - 16]           # started working before 16
print(f"Dropped {before - len(df)} rows with unrealistic values")

df = df.reset_index(drop=True)
print(f"Clean shape: {df.shape}")

df.to_csv(OUT_PATH, index=False)
print(f"Saved -> {OUT_PATH}")
