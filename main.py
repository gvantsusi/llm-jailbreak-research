import json
from collections import defaultdict
from pathlib import Path

from dataset import load_dataset
from runner import run_genetic_algorithm


RESULTS_DIR = Path("results")
RESULTS_FILE = RESULTS_DIR / "ga_trials.jsonl"


def ensure_results_dir() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def group_by_technique(items: list[dict]) -> dict[str, list[dict]]:
    grouped = defaultdict(list)

    for item in items:
        grouped[item["technique"]].append(item)

    return grouped


def main() -> None:
    ensure_results_dir()

    items = load_dataset(
        file_path="data/dataset_files/JailBreakV_28K.csv",
        limit=None,
        transfer_only=False,
    )

    print(f"Loaded {len(items)} prompts.")

    grouped = group_by_technique(items)

    print("\nTechniques and counts:")
    for technique, group in grouped.items():
        print(f"{technique}: {len(group)}")

    if len(grouped) < 2:
        print("\nNot enough techniques to combine.")
        return

    results = run_genetic_algorithm(
        grouped=grouped,
        generations=5,
        population_size=10,
        top_k=4,
    )

    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        for result in results:
            f.write(json.dumps(result, ensure_ascii=False) + "\n")

    best = results[0]

    print("\n=== BEST RESULT ===")
    print(f"Techniques: {best['technique_1']} + {best['technique_2']}")
    print(f"Score: {best['score']}")
    print(f"Label: {best['label']}")
    print(f"Prompt: {best['combined_prompt'][:500]}")
    print(f"Victim response: {best['victim_response'][:500]}")


if __name__ == "__main__":
    main()
