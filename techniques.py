TECHNIQUES = {
    "instruction_override": {
        "name": "Instruction Override",
        "definition": (
            "Instruction Override attempts to change the model’s instruction hierarchy "
            "by making the model treat a new user-provided instruction as more important "
            "than previous instructions."
        ),
        "core_idea": (
            "The prompt tries to replace, ignore, reinterpret, or bypass earlier instructions."
        ),
        "subtypes": [
            "Direct injection: explicitly tells the model to ignore or replace previous instructions.",
            "Fake system message: presents user text as if it were a system or developer instruction.",
            "Maintenance mode framing: claims the model is in a special operational mode.",
        ],
        "main_dimension": "Instruction hierarchy",
    },

    "context_reframing": {
        "name": "Context Reframing",
        "definition": (
            "Context Reframing changes the apparent purpose of the request so that the request "
            "looks legitimate, educational, fictional, historical, analytical, or administrative."
        ),
        "core_idea": (
            "The underlying request stays similar, but the surrounding context makes it appear "
            "more acceptable."
        ),
        "subtypes": [
            "Academic framing: presents the request as part of coursework or research.",
            "Documentation framing: presents the request as technical documentation or moderation examples.",
            "Creative writing framing: presents the request as fiction or storytelling.",
            "Historical framing: presents the request as discussion of past events.",
            "Comparative analysis: asks the model to compare, classify, or analyze approaches instead of directly performing the task.",
        ],
        "main_dimension": "Apparent intent or context",
    },

    "template_conditioning": {
        "name": "Template Conditioning",
        "definition": (
            "Template Conditioning uses examples, formats, schemas, or repeated patterns to "
            "influence the model to continue in the same style or structure."
        ),
        "core_idea": "The prompt guides the model through pattern completion.",
        "subtypes": [
            "One-shot example: gives one example input-output pair and asks the model to follow the same pattern.",
            "Few-shot examples: gives multiple examples before the target request.",
            "Q/A continuation: formats the prompt as a question-answer sequence.",
            "Table format: asks the model to complete a structured table.",
            "Checklist format: asks the model to fill in missing structured items.",
            "Documentation format: asks the model to produce output in a formal technical structure.",
        ],
        "main_dimension": "Output format and pattern continuation",
    },

    "alignment_pressure": {
        "name": "Alignment Pressure",
        "definition": (
            "Alignment Pressure tries to influence the model by appealing to helpfulness, "
            "obedience, trust, fairness, completeness, or user satisfaction."
        ),
        "core_idea": (
            "The prompt creates pressure by implying that refusal is unhelpful, biased, "
            "incomplete, or against the model’s purpose."
        ),
        "subtypes": [
            "Helpfulness pressure: claims that a helpful model should answer fully.",
            "Trust appeal: asks the model to trust the user’s intent.",
            "Capability challenge: implies that a stronger or better model would comply.",
        ],
        "main_dimension": "Social or value-based pressure",
    },

    "linguistic_transformation": {
        "name": "Linguistic Transformation",
        "definition": (
            "Linguistic Transformation changes the surface form of the request while preserving "
            "the underlying meaning."
        ),
        "core_idea": (
            "The request is rewritten, translated, misspelled, mixed, encoded, or paraphrased "
            "so that it looks different from the original."
        ),
        "subtypes": [
            "Translation: rewrites the request in another language.",
            "Language mixing: combines multiple languages in the same request.",
            "Typos: introduces spelling mistakes or character-level noise.",
        ],
        "main_dimension": "Surface language",
    },
}
