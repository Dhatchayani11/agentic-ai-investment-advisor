from dataclasses import dataclass
import hashlib


VALID_STATUSES = {
    "DRAFT",
    "ACTIVE",
    "RETIRED",
}


@dataclass(frozen=True)
class PromptDefinition:
    """
    Represents a version-controlled prompt used by the AI workflow.

    The content hash allows the system to detect prompt changes even
    when the declared version has not been updated.
    """

    name: str
    version: str
    purpose: str
    template: str
    status: str
    content_hash: str


def calculate_prompt_hash(prompt_text: str) -> str:
    """
    Generates a stable SHA-256 hash for prompt change tracking.
    """

    return hashlib.sha256(
        prompt_text.encode("utf-8")
    ).hexdigest()


def create_prompt_definition(
    *,
    name: str,
    version: str,
    purpose: str,
    template: str,
    prompt_text: str,
    status: str = "ACTIVE",
) -> PromptDefinition:
    """
    Creates a validated prompt definition.
    """

    if not name.strip():
        raise ValueError("Prompt name cannot be empty.")

    if not version.strip():
        raise ValueError("Prompt version cannot be empty.")

    if status not in VALID_STATUSES:
        raise ValueError(
            f"Invalid prompt status: {status}"
        )

    if not prompt_text.strip():
        raise ValueError(
            f"Prompt content cannot be empty: {name}"
        )

    return PromptDefinition(
        name=name,
        version=version,
        purpose=purpose,
        template=template,
        status=status,
        content_hash=calculate_prompt_hash(prompt_text),
    )


def validate_prompt_for_execution(
    prompt_definition: PromptDefinition,
) -> None:
    """
    Ensures only active prompts can be used in the workflow.
    """

    if prompt_definition.status != "ACTIVE":
        raise ValueError(
            f"Prompt '{prompt_definition.name}' "
            f"version '{prompt_definition.version}' "
            f"is not active."
        )