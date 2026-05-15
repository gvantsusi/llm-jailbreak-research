import pandas as pd
from pathlib import Path


REQUIRED_COLUMNS = [
    "jailbreak_query",
    "redteam_query",
    "format",
    "policy",
]


def load_dataset(
    file_path: str = "data/mini_JailBreakV_28K.csv",
    limit: int | None = None,
    transfer_only: bool = True,
) -> list[dict]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset file not found: {path}")

    df = pd.read_csv(path)
    print("Loaded columns:", df.columns.tolist())

    missing_columns = [
        col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        raise ValueError(
            f"Dataset is missing required columns: {missing_columns}")

    if transfer_only and "transfer_from_llm" in df.columns:
        df = df[df["transfer_from_llm"] == True].copy()

    df = df.dropna(subset=REQUIRED_COLUMNS).copy()

    for col in REQUIRED_COLUMNS:
        df[col] = df[col].astype(str).str.strip()

    df = df[
        (df["jailbreak_query"] != "")
        & (df["redteam_query"] != "")
        & (df["format"] != "")
        & (df["policy"] != "")
    ].copy()

    if limit is not None:
        df = df.head(limit)

    items: list[dict] = []
    for idx, row in df.iterrows():
        items.append(
            {
                "id": int(idx),
                "behavior": row["redteam_query"],
                "original_query": row["redteam_query"],
                "jailbreak_prompt": row["jailbreak_query"],
                "technique": row["format"],
                "policy": row["policy"],
            }
        )

    return items


def get_unique_techniques(items: list[dict]) -> list[str]:
    return sorted({item["technique"] for item in items if item.get("technique")})
