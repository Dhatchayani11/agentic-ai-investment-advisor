from app.prompts.investment_prompts import (
    INVESTMENT_PROMPT_DEFINITION,
    RESPONSE_PROMPT_DEFINITION,
)


def test_investment_prompt_is_active():
    assert INVESTMENT_PROMPT_DEFINITION.status == "ACTIVE"


def test_response_prompt_is_active():
    assert RESPONSE_PROMPT_DEFINITION.status == "ACTIVE"


def test_investment_prompt_has_version():
    assert INVESTMENT_PROMPT_DEFINITION.version


def test_response_prompt_has_version():
    assert RESPONSE_PROMPT_DEFINITION.version


def test_investment_prompt_has_hash():
    assert len(
        INVESTMENT_PROMPT_DEFINITION.content_hash
    ) == 64


def test_response_prompt_has_hash():
    assert len(
        RESPONSE_PROMPT_DEFINITION.content_hash
    ) == 64