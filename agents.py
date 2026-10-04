```python
import os

from dotenv import load_dotenv
from crewai import Agent, LLM


# ---------------------------------------------------------
# Load environment variables
# ---------------------------------------------------------

load_dotenv()


# ---------------------------------------------------------
# Create LLM
# ---------------------------------------------------------

def get_llm():

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:

        raise ValueError(
            "GROQ_API_KEY is missing. "
            "Add it to your .env file locally "
            "or Streamlit Secrets in deployment."
        )

    return LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=api_key,
        temperature=0.2
    )


# ---------------------------------------------------------
# Create Agents
# ---------------------------------------------------------

def create_agents():

    llm = get_llm()


    # -----------------------------------------------------
    # Researcher
    # -----------------------------------------------------

    researcher = Agent(
        role="Research Specialist",

        goal=(
            "Gather accurate, relevant and well-organized "
            "information about the research topic."
        ),

        backstory=(
            "You are an experienced research specialist. "
            "You collect important information, identify "
            "key concepts and organize research findings "
            "for further analysis."
        ),

        llm=llm,

        verbose=True,

        allow_delegation=False
    )


    # -----------------------------------------------------
    # Analyst
    # -----------------------------------------------------

    analyst = Agent(
        role="Research Analyst",

        goal=(
            "Analyze research findings and identify "
            "important themes, insights and research gaps."
        ),

        backstory=(
            "You are a critical research analyst. "
            "You examine research findings carefully, "
            "identify patterns and discover knowledge gaps."
        ),

        llm=llm,

        verbose=True,

        allow_delegation=False
    )


    # -----------------------------------------------------
    # Writer
    # -----------------------------------------------------

    writer = Agent(
        role="Research Report Writer",

        goal=(
            "Create a clear, structured and professional "
            "research report."
        ),

        backstory=(
            "You are an expert technical writer. "
            "You transform research findings and analysis "
            "into a professional research report."
        ),

        llm=llm,

        verbose=True,

        allow_delegation=False
    )


    # -----------------------------------------------------
    # Reviewer
    # -----------------------------------------------------

    reviewer = Agent(
        role="Research Quality Reviewer",

        goal=(
            "Review and improve the research report "
            "for clarity, accuracy and completeness."
        ),

        backstory=(
            "You are a senior research reviewer. "
            "You identify weaknesses, remove unnecessary "
            "repetition and improve the quality of reports."
        ),

        llm=llm,

        verbose=True,

        allow_delegation=False
    )


    return (
        researcher,
        analyst,
        writer,
        reviewer
    )
```
