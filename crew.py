from crewai import Crew, Process

from agents import create_agents
from tasks import create_tasks


def create_research_crew(topic):

    # Create agents
    researcher, analyst, writer, reviewer = create_agents()

    # Create tasks
    tasks = create_tasks(
        researcher,
        analyst,
        writer,
        reviewer,
        topic
    )

    # Create Crew
    crew = Crew(
        agents=[
            researcher,
            analyst,
            writer,
            reviewer
        ],

        tasks=tasks,

        process=Process.sequential,

        verbose=True
    )

    return crew
