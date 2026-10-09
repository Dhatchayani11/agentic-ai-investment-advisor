import os

import requests
import streamlit as st


API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "http://127.0.0.1:8000",
).rstrip("/")

ADVICE_ENDPOINT = f"{API_BASE_URL}/investment/advice"
FEEDBACK_ENDPOINT = f"{API_BASE_URL}/investment/feedback"

st.set_page_config(
    page_title="AI Investment Advisor",
    page_icon="📈",
    layout="centered",
)

st.title("📈 AI Investment Advisor")
st.caption(
    "AI-powered investment guidance with explanations "
    "and compliance checks."
)

st.info(
    "This application is a prototype for educational purposes. "
    "It does not replace advice from a qualified financial professional."
)

if "advice_result" not in st.session_state:
    st.session_state.advice_result = None

if "feedback_submitted" not in st.session_state:
    st.session_state.feedback_submitted = False


with st.form("investment_advice_form"):
    st.subheader("Ask your investment question")

    customer_id = st.text_input(
        "Customer ID",
        placeholder="Enter your customer ID",
    )

    query = st.text_area(
        "What would you like guidance on?",
        placeholder=(
            "Example: What factors should I consider "
            "when planning my retirement contributions?"
        ),
        height=130,
        max_chars=2000,
    )

    submitted = st.form_submit_button(
        "Get Guidance",
        type="primary",
        use_container_width=True,
    )


if submitted:
    if not customer_id.strip():
        st.error("Please enter a customer ID.")
    elif len(query.strip()) < 5:
        st.error("Please enter a question with at least 5 characters.")
    else:
        try:
            with st.spinner(
                "Analyzing your question. Please wait..."
            ):
                response = requests.post(
                    ADVICE_ENDPOINT,
                    json={
                        "customer_id": customer_id.strip(),
                        "query": query.strip(),
                    },
                    timeout=120,
                )

            if response.ok:
                st.session_state.advice_result = response.json()
                st.session_state.feedback_submitted = False
            else:
                try:
                    error_detail = response.json().get(
                        "detail",
                        "The request could not be processed.",
                    )
                except ValueError:
                    error_detail = "The request could not be processed."

                st.error(f"Request failed ({response.status_code}): {error_detail}")

        except requests.exceptions.Timeout:
            st.error(
                "The request took too long. Please try again."
            )
        except requests.exceptions.ConnectionError:
            st.error(
                "Cannot connect to the backend. "
                "Make sure the FastAPI server is running."
            )
        except requests.exceptions.RequestException:
            st.error(
                "A network error occurred. Please try again."
            )


result = st.session_state.advice_result

if result:
    st.divider()
    st.subheader("Your Guidance")

    st.markdown(result.get(
        "response",
        "No response was returned.",
    ))

    st.subheader("Explanation")
    st.write(result.get(
        "explanation",
        "No explanation was returned.",
    ))

    compliance_status = result.get(
        "compliance_status",
        "REQUIRES_REVIEW",
    )

    if compliance_status == "PASSED":
        st.success(f"Compliance status: {compliance_status}")
    else:
        st.warning(f"Compliance status: {compliance_status}")

    compliance_reason = result.get("compliance_reason")
    if compliance_reason:
        st.caption(f"Compliance details: {compliance_reason}")

    advice_id = result.get("advice_id")

    if advice_id and not st.session_state.feedback_submitted:
        st.divider()
        st.subheader("Was this response helpful?")

        col1, col2 = st.columns(2)

        with col1:
            if st.button(
                "👍 Helpful",
                use_container_width=True,
            ):
                st.session_state.feedback_choice = "positive"

        with col2:
            if st.button(
                "👎 Not helpful",
                use_container_width=True,
            ):
                st.session_state.feedback_choice = "negative"

        feedback_choice = st.session_state.get("feedback_choice")

        if feedback_choice:
            feedback_comment = st.text_area(
                "Optional feedback",
                key="feedback_comment",
                placeholder="Tell us what could be improved.",
                max_chars=2000,
            )

            if st.button(
                "Submit Feedback",
                type="primary",
            ):
                try:
                    feedback_response = requests.post(
                        FEEDBACK_ENDPOINT,
                        json={
                            "advice_id": advice_id,
                            "customer_id": customer_id.strip(),
                            "rating": feedback_choice,
                            "comment": feedback_comment.strip() or None,
                        },
                        timeout=15,
                    )

                    if feedback_response.ok:
                        st.session_state.feedback_submitted = True
                        st.session_state.pop("feedback_choice", None)
                        st.success("Thank you! Your feedback was recorded.")
                        st.rerun()
                    else:
                        st.error(
                            "Feedback could not be recorded. "
                            "Please try again."
                        )

                except requests.exceptions.RequestException:
                    st.error(
                        "Unable to connect to the backend "
                        "to submit feedback."
                    )
    elif advice_id and st.session_state.feedback_submitted:
        st.success("Feedback submitted. Thank you!")