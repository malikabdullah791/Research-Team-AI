```python
# ---------------------------------------------------------
# IMPORTANT: CrewAI + Groq compatibility patch
# ---------------------------------------------------------
# CrewAI currently adds "cache_breakpoint" to messages.
# Groq does not accept this field.
# This patch disables that marker before CrewAI agents run.

try:
    import crewai.llms.cache as crew_cache

    crew_cache.mark_cache_breakpoint = lambda message: message

except Exception:
    pass


# ---------------------------------------------------------
# Imports
# ---------------------------------------------------------

import streamlit as st

from crew import create_research_crew


# ---------------------------------------------------------
# Streamlit Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Research Team",
    page_icon="🔬",
    layout="wide"
)


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("🔬 AI Research Team")

st.write(
    "A CrewAI-powered multi-agent research assistant "
    "that researches, analyzes, writes and reviews reports."
)


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

with st.sidebar:

    st.header("🤖 AI Research Team")

    st.write("""
    **1. Researcher**

    Gathers and organizes research findings.

    **2. Analyst**

    Analyzes findings and identifies themes and gaps.

    **3. Writer**

    Creates a structured research report.

    **4. Reviewer**

    Reviews and improves the final report.
    """)

    st.divider()

    st.info(
        "Workflow:\n\n"
        "Research → Analyze → Write → Review"
    )


# ---------------------------------------------------------
# Topic Input
# ---------------------------------------------------------

topic = st.text_area(
    "Enter your research topic",
    placeholder=(
        "Example: Impact of EV smart charging "
        "on renewable energy hosting capacity"
    ),
    height=120
)


# ---------------------------------------------------------
# Research Button
# ---------------------------------------------------------

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
                "🤖 AI Research Team is working..."
            ):

                # Create the Crew
                research_crew = create_research_crew(
                    topic.strip()
                )

                # Run the Crew
                result = research_crew.kickoff()

            # -------------------------------------------------
            # Success
            # -------------------------------------------------

            st.success(
                "✅ Research completed successfully!"
            )

            st.divider()

            st.subheader(
                "📄 Final Research Report"
            )

            st.markdown(str(result))


        except Exception as e:

            st.error(
                "❌ An error occurred while running "
                "the AI Research Team."
            )

            st.exception(e)
```
