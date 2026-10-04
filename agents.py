import os

from dotenv import load_dotenv
from crewai import Agent, LLM

load_dotenv()


def get_llm():
    """
    Create the LLM used by all agents.
    The API key is loaded from the environment.
    """

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. "
            "Please add it to your .env file."
        )

    return LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=api_key,
        temperature=0.2
    )


def create_agents():

    llm = get_llm()

    # Agent 1
    researcher = Agent(
        role="Research Specialist",
        goal=(
            "Gather accurate, relevant and well-organized "
            "information about the research topic."
        ),
        backstory=(
            "You are an experienced research specialist. "
            "You collect important information, identify "
            "key facts, concepts and evidence, and organize "
            "your findings clearly for another analyst."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    # Agent 2
    analyst = Agent(
        role="Research Analyst",
        goal=(
            "Analyze research findings, identify important "
            "themes, relationships, trends and knowledge gaps."
        ),
        backstory=(
            "You are a critical research analyst. "
            "You examine research findings carefully and "
            "separate important insights from less useful information. "
            "You identify themes, contradictions and research gaps."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    # Agent 3
    writer = Agent(
        role="Research Report Writer",
        goal=(
            "Transform research findings and analysis into "
            "a clear, structured and professional research report."
        ),
        backstory=(
            "You are an expert technical writer. "
            "You convert complex research information into "
            "well-structured reports that are easy to understand "
            "while maintaining professional quality."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    # Agent 4
    reviewer = Agent(
        role="Research Quality Reviewer",
        goal=(
            "Review the research report for accuracy, clarity, "
            "structure, completeness and logical consistency."
        ),
        backstory=(
            "You are a senior research reviewer. "
            "You critically inspect reports, identify weaknesses "
            "and improve the final document so it is clear, "
            "professional and useful."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    return researcher, analyst, writer, reviewer
