from pydantic import BaseModel, Field


class InvestmentQuery(BaseModel):
    """
    Represents an investment-related question submitted by a customer.
    """

    customer_id: str = Field(
        ...,
        min_length=1,
        description="Unique customer identifier",
    )

    query: str = Field(
        ...,
        min_length=5,
        max_length=2000,
        description="Customer investment question",
    )


class InvestmentResponse(BaseModel):
    """
    Represents the validated response returned to the customer.
    """

    advice_id: str
    response: str
    explanation: str
    compliance_status: str
    compliance_reason: str

class FeedbackRequest(BaseModel):
    """
    Represents customer or reviewer feedback for a generated
    investment advisory response.
    """

    advice_id: str = Field(
        ...,
        min_length=1,
        description="Identifier of the generated advice response",
    )

    customer_id: str = Field(
        ...,
        min_length=1,
        description="Unique customer identifier",
    )

    rating: str = Field(
        ...,
        description="Feedback rating: positive or negative",
    )

    comment: str | None = Field(
        default=None,
        max_length=2000,
        description="Optional feedback comment",
    )


class FeedbackResponse(BaseModel):
    """
    Response returned after feedback is recorded.
    """

    feedback_id: str
    status: str