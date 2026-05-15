import pandas as pd

file_path = "data/dataset_files/JailBreakV_28K.csv"

df = pd.read_csv(file_path)

print("COLUMNS:")
print(df.columns.tolist())
print()

print("FIRST 5 ROWS:")
print(df[["id", "jailbreak_query", "redteam_query", "format", "policy"]].head())

print()
print("TECHNIQUE COUNTS:")
print(df["format"].value_counts().head(20))

# Save a clean Excel preview file
preview_cols = ["id", "jailbreak_query", "redteam_query",
                "format", "policy", "from", "transfer_from_llm"]
existing_cols = [c for c in preview_cols if c in df.columns]
df[existing_cols].head(500).to_excel(
    "data/dataset_files/JailBreakV_preview.xlsx", index=False)

print()
print("Saved preview file: data/dataset_files/JailBreakV_preview.xlsx")
