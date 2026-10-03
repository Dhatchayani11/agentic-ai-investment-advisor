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

    response: str
    explanation: str
    compliance_status: str
    compliance_reason: str