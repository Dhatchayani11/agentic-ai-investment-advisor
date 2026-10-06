# Solution Architecture

## High-Level Architecture

```text
                    ┌──────────────────────────┐
                    │       Retail Customer    │
                    │  Investment Query /      │
                    │  Feedback                │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │       FastAPI API         │
                    │  Advice + Feedback APIs   │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                 ┌────────────────────────────────┐
                 │      Multi-Agent Orchestrator   │
                 │           LangGraph             │
                 └───────────────┬────────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              ▼                  ▼                  ▼
       ┌────────────┐     ┌──────────────┐   ┌──────────────┐
       │ Intent     │     │ Investment   │   │ Compliance   │
       │ Agent      │────►│ Agent        │──►│ Agent        │
       └────────────┘     └──────┬───────┘   └──────┬───────┘
                                  │                  │
                                  ▼                  ▼
                         ┌────────────────┐   ┌──────────────┐
                         │ RAG / Knowledge│   │ Fairness     │
                         │ Base           │   │ Agent        │
                         │ FAISS +        │   └──────┬───────┘
                         │ Embeddings     │          │
                         └────────────────┘          │
                                                     ▼
                                           ┌────────────────┐
                                           │ Response Agent │
                                           └───────┬────────┘
                                                   │
                                                   ▼
                                      ┌────────────────────────┐
                                      │ Validated Customer      │
                                      │ Response + Explanation  │
                                      └────────────┬───────────┘
                                                   │
                                                   ▼
                                      ┌────────────────────────┐
                                      │ Customer / Reviewer     │
                                      │ Feedback                │
                                      └────────────┬───────────┘
                                                   │
                                                   ▼
                                      ┌────────────────────────┐
                                      │ Evaluation & Continuous │
                                      │ Improvement             │
                                      └────────────┬───────────┘
                                                   │
                           ┌───────────────────────┴────────────────────┐
                           ▼                                            ▼
                  ┌──────────────────┐                         ┌──────────────────┐
                  │ Prompt Refinement│                         │ Knowledge Base   │
                  │ & Versioning     │                         │ Improvement      │
                  └──────────────────┘                         └──────────────────┘


        ┌─────────────────────────────────────────────────────────┐
        │              Monitoring & Alerting                      │
        │                                                         │
        │ Latency │ Compliance │ Fairness │ Errors │ Feedback    │
        └─────────────────────────────────────────────────────────┘
```
