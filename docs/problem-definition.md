# Problem Definition

## Business Problem

A large US bank wants to reduce the investment advice gap by providing retail customers with accessible, personalised, and regulated investment guidance.

Customers may have questions such as:

- Should I increase my pension contribution?
- Should I invest in stocks?
- What factors should I consider before making an investment decision?

Traditional support channels may not provide timely and consistent guidance at the scale required for millions of customers.

The proposed solution uses agentic AI to analyse customer investment queries, retrieve relevant knowledge, perform specialised checks, and generate a controlled response.

## Target Users

The primary users are:

- Retail investors
- Existing bank customers seeking investment guidance
- Customer-service or financial-support teams reviewing AI-generated responses

The system is designed to provide informational investment guidance and should not make unsupported or guaranteed investment claims.

## Key Requirements

### Personalisation

The system should analyse the customer's investment query and generate guidance relevant to the stated question and available context.

### Regulatory Compliance

Investment-related responses must be controlled to reduce the risk of:

- Unsupported regulatory claims
- Guaranteed returns
- Risk-free investment claims
- Definitive personalised investment recommendations

Regulatory information should be grounded in approved knowledge sources.

### Fairness

The system should avoid making investment-related decisions or recommendations based on sensitive characteristics such as:

- Race
- Religion
- Gender
- Ethnicity
- Nationality

Fairness checks are performed before the final response is generated.

### Explainability

The system should provide an explanation describing how the response was produced, including the use of retrieved knowledge and compliance/fairness validation.

### Accuracy

Responses should be grounded in relevant knowledge and should avoid introducing unsupported financial or regulatory facts.

### Scalability

The solution should be capable of supporting a large retail customer population through scalable API services, model infrastructure, retrieval infrastructure, monitoring, and persistent data services.

### Monitoring

The system should monitor operational and AI-related metrics including:

- Response latency
- Compliance review requirements
- Fairness review requirements
- Knowledge retrieval
- Workflow completion
- Evaluation metrics

### Feedback

Customers or reviewers should be able to provide feedback on generated responses.

Feedback should support future:

- Evaluation
- Prompt refinement
- Knowledge-base improvement
- Human review

## Solution Objective

The objective is to build an agentic AI investment guidance system that combines:

- Multi-agent orchestration
- Retrieval-Augmented Generation (RAG)
- Prompt lifecycle management
- Compliance validation
- Fairness validation
- Explainable responses
- Evaluation
- Monitoring and alerting
- Continuous feedback

The prototype demonstrates the technical approach while maintaining a design that can be extended toward a production banking environment.

## License

This project is for educational and portfolio purposes.
