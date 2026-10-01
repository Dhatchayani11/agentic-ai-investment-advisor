from pydantic import BaseModel, Field


class InvestmentQuery(BaseModel):
    """
    Represents an investment-related question submitted by a customer.
    """

    customer_id: str = Field(..., description="Unique customer identifier")
    query: str = Field(..., min_length=5, description="Customer investment question")


class InvestmentResponse(BaseModel):
    """
    Represents the validated response returned to the customer.
    """

    response: str
    explanation: str
    compliance_status: str