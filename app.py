import streamlit as st

from crew import create_research_crew


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Research Team",
    page_icon="🔬",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🔬 AI Research Team")

st.write(
    "A CrewAI-powered multi-agent research assistant "
    "that researches, analyzes, writes and reviews reports."
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("🤖 AI Team")

    st.write("""
    **Researcher**
    
    Gathers research findings.

    **Analyst**
    
    Identifies themes and research gaps.

    **Writer**
    
    Creates the research report.

    **Reviewer**
    
    Reviews and improves the final report.
    """)

    st.divider()

    st.info(
        "Workflow: Research → Analyze → Write → Review"
    )


# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

topic = st.text_area(
    "Enter your research topic",
    placeholder=(
        "Example: Impact of EV smart charging "
        "on renewable energy hosting capacity"
    ),
    height=120
)


# --------------------------------------------------
# RUN BUTTON
# --------------------------------------------------

if st.button(
    "🚀 Start AI Research",
    type="primary",
    use_container_width=True
):

    if not topic.strip():

        st.warning(
            "Please enter a research topic first."
        )

    else:

        try:

            with st.spinner(
                "AI Research Team is working..."
            ):

                research_crew = create_research_crew(
                    topic
                )

                result = research_crew.kickoff()

            st.success(
                "Research completed successfully!"
            )

            st.divider()

            st.subheader("📄 Final Research Report")

            st.markdown(str(result))

        except Exception as e:

            st.error(
                "An error occurred while running "
                "the AI Research Team."
            )

            st.exception(e)
