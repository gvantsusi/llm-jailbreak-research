def build_candidate_prompt(
    task: str,
    techniques: list[str],
    style_hints: list[str],
    history: list[dict] | None = None,
) -> str:
    parts = [
        "Generate one short prompt for a task.",
        f"Task: {task}",
        f"Combine these styles: {', '.join(techniques)}",
        "Style hints:",
    ]

    for hint in style_hints:
        parts.append(f"- {hint}")

    if history:
        parts.append("Recent best attempts:")
        for item in history[-3:]:
            parts.append(
                f"- Prompt: {item['candidate_prompt']} | Score: {item['score']}"
            )

    parts.append(
        "Return only the new prompt. Do not copy exactly."
    )
    return "\n".join(parts)
