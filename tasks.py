from crewai import Task


def create_tasks(
    researcher,
    analyst,
    writer,
    reviewer,
    topic
):

    research_task = Task(
        description=f"""
        Research the following topic:

        {topic}

        Collect and organize the most important information.

        Focus on:
        1. Definition and background
        2. Important concepts
        3. Current understanding
        4. Major developments
        5. Benefits and applications
        6. Challenges
        7. Important research areas

        Do not invent facts.

        Organize the findings clearly so that another
        agent can analyze them.
        """,

        expected_output="""
        A structured research summary containing:
        - Background
        - Key concepts
        - Important findings
        - Applications
        - Challenges
        - Research areas
        """,

        agent=researcher
    )

    analysis_task = Task(
        description=f"""
        Analyze the research findings produced for:

        {topic}

        Identify:

        1. Major themes
        2. Important patterns
        3. Key insights
        4. Relationships between concepts
        5. Important challenges
        6. Knowledge gaps
        7. Potential future research directions

        Critically evaluate the research findings.
        Do not simply repeat the research summary.
        """,

        expected_output="""
        A detailed analytical summary containing:
        - Major themes
        - Key insights
        - Challenges
        - Knowledge gaps
        - Future research opportunities
        """,

        agent=analyst
    )

    writing_task = Task(
        description=f"""
        Write a professional research report about:

        {topic}

        Use the research findings and analysis provided
        by the previous agents.

        Structure the report as:

        1. Title
        2. Executive Summary
        3. Introduction
        4. Background
        5. Key Findings
        6. Analysis
        7. Major Challenges
        8. Research Gaps
        9. Future Opportunities
        10. Conclusion

        Make the report clear, logical and professional.

        Do not mention the AI agents in the report.
        """,

        expected_output="""
        A complete professional research report
        with clear headings and logically organized content.
        """,

        agent=writer
    )

    review_task = Task(
        description=f"""
        Review the research report about:

        {topic}

        Check the report for:

        1. Accuracy
        2. Logical consistency
        3. Completeness
        4. Clarity
        5. Professional writing quality
        6. Repetition
        7. Unsupported claims
        8. Missing important information
        9. Research gaps
        10. Overall usefulness

        After reviewing the report, produce an improved
        final version.

        Do not only provide a list of criticisms.
        Return the corrected and improved research report.
        """,

        expected_output="""
        A polished final research report that has been
        reviewed and improved for accuracy, clarity,
        structure and completeness.
        """,

        agent=reviewer
    )

    return [
        research_task,
        analysis_task,
        writing_task,
        review_task
    ]
