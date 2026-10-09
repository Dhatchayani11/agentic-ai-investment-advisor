# Agentic AI Investment Advisor

An agentic AI prototype designed to provide explainable, compliance-aware investment guidance for retail banking customers. The application uses a multi-agent workflow, Retrieval-Augmented Generation (RAG), and a user-friendly Streamlit interface.

> **Disclaimer:** This project is an educational prototype and does not provide personalized financial advice or replace a qualified financial professional.

## Key Features

- **Multi-agent orchestration:** Uses LangGraph to coordinate intent classification, investment analysis, compliance checks, fairness checks, and response generation.
- **LLM integration:** Uses Groq to generate investment-related responses.
- **Retrieval-Augmented Generation (RAG):** Retrieves relevant information from a local investment guidance knowledge base.
- **Compliance validation:** Checks generated responses before presenting them to users.
- **Fairness checks:** Includes basic fairness validation in the agent workflow.
- **Explainability:** Provides explanations alongside generated guidance.
- **Prompt lifecycle management:** Maintains prompt versions, status, and hashes.
- **Streamlit UI:** Provides a simple interface for asking questions, viewing guidance, and submitting feedback.
- **FastAPI backend:** Exposes APIs for investment guidance, health checks, and feedback.
- **Monitoring and alerting:** Records relevant execution metrics and flags selected conditions.
- **Evaluation and testing:** Includes evaluation scripts and automated tests.

## Technology Stack

- Python
- FastAPI
- Streamlit
- LangGraph
- Groq LLM
- Retrieval-Augmented Generation (RAG)
- Sentence Transformers
- FAISS
- Pydantic
- Pytest

## Architecture

```text
User
 |
 v
Streamlit Frontend
 |
 v
FastAPI Backend
 |
 v
LangGraph Orchestration
 |
 +--> Intent Agent
 |
 +--> Investment Agent
 |       |
 |       v
 |   RAG Knowledge Base
 |       |
 |       v
 |     Groq LLM
 |
 +--> Compliance Agent
 |
 +--> Fairness Agent
 |
 +--> Response Agent
 |
 v
Guidance + Explanation + Status
 |
 v
Streamlit Frontend
 |
 v
User Feedback
```

## Project Structure

```text
agentic-ai-investment-advisor/
├── app/
│   ├── agents/
│   ├── knowledge/
│   │   └── documents/
│   ├── monitoring/
│   ├── orchestration/
│   ├── prompts/
│   ├── config.py
│   ├── llm_service.py
│   ├── main.py
│   └── models.py
├── frontend/
│   └── streamlit_app.py
├── evaluation/
│   ├── test_cases.py
│   └── run_evaluation.py
├── tests/
├── docs/
│   ├── architecture.md
│   └── problem-definition.md
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.10
- Git
- A Groq API key

## Setup

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd agentic-ai-investment-advisor
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

Ensure `streamlit` and `requests` are included in `requirements.txt` for the frontend.

### 4. Configure environment variables

Create a `.env` file in the project root using `.env.example` as a reference.

Configure your Groq API key and model:

```env
LLM_API_KEY=your_groq_api_key
LLM_MODEL=your_configured_groq_model
```

Use the model name supported by your Groq account and application configuration. Never commit your `.env` file or expose your API key.

## Running the Application

The application has two components: a FastAPI backend and a Streamlit frontend. Run them in separate VS Code terminals.

### Terminal 1: Start the FastAPI backend

Activate the virtual environment and run:

```bash
uvicorn app.main:app --reload
```

Backend URL: `http://127.0.0.1:8000`

FastAPI Swagger documentation: `http://127.0.0.1:8000/docs`

Health endpoint: `http://127.0.0.1:8000/health`

### Terminal 2: Start the Streamlit frontend

Activate the same virtual environment, navigate to the project root, and run:

```bash
streamlit run frontend/streamlit_app.py
```

Streamlit will display the local URL in the terminal, usually:

`http://localhost:8501`

Open that URL in your browser to use the application.

**Note:** Keep the FastAPI backend running while using Streamlit. The frontend sends API requests to the backend.

## Using the Application

1. Open the Streamlit application.
2. Enter a customer ID.
3. Submit an investment-related question.
4. Review the generated guidance and explanation.
5. Check the compliance status.
6. Submit positive or negative feedback, optionally with a comment.

Example question:

> What factors should I consider when deciding how much of my salary to contribute to my retirement savings, considering my age, risk tolerance, and long-term financial goals?

## API Endpoints

| Method | Endpoint               | Purpose                       |
| ------ | ---------------------- | ----------------------------- |
| GET    | `/health`              | Check backend health          |
| POST   | `/investment/advice`   | Generate investment guidance  |
| POST   | `/investment/feedback` | Submit feedback on a response |

You can explore the API schemas and test the endpoints directly using `/docs`.

## Evaluation

The project includes an evaluation script for assessing intent classification, compliance, regulatory fact safety, fairness, explanation coverage, response coverage, latency, context relevance, groundedness, and answer relevance.

Run the evaluation from the project root:

```bash
python -m evaluation.run_evaluation
```

Evaluation results depend on the test cases, model responses, and environment. Small test datasets are useful for development but do not establish production readiness.

## Testing

Run the automated test suite:

```bash
python -m pytest -q
```

## Monitoring and Feedback

The monitoring components capture selected execution details, including latency, intent classification, compliance outcomes, fairness outcomes, prompt versions, and knowledge retrieval.

The feedback API records user feedback for later analysis. The current monitoring, alerting, and feedback components are prototype implementations and should be extended and validated before production use.

## Production Considerations

Before deploying in a real banking environment, additional work would be required, including:

- Strong authentication and authorization
- Secure handling of customer information
- Validated regulatory and compliance policies
- More comprehensive fairness, safety, and hallucination evaluations
- Reliable observability and operational alerting
- Secure secrets management
- Load, resilience, and performance testing
- Human review and appropriate financial-advice governance

The project demonstrates an architectural prototype; it is not a production banking deployment.

## Documentation

- [Architecture](docs/architecture.md)
- [Problem Definition](docs/problem-definition.md)
