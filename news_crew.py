from crewai import Agent, Task, Crew, LLM, Process
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

llm = LLM(model="gpt-4o-mini")
search = SerperDevTool();

researcher = Agent(
    role="Researcher",
    goal="collect cricket news",
    backstory="you are a senior news researcher and passinate about sports specially cricket",
    # llm=llm,
    tools=[search],
    max_iter=5,
    verbose=True
)

cricket_news = Task(
    description="Collect news about latest international matches, scores, player of the match, key points about the match",
    expected_output="create a summary, text content as less, like POM=player name, result",
    agent=researcher
)

editor = Agent(
    role="writer",
    goal="Crisp newsletter about cricket news",
    backstory="you are a senior news writer, have enlarged experience about sports news letter",
    # llm=llm,
    
    verbose=True
)

cricket_news_letter = Task(
    description=" make a simple and intresting way to show as a news letter and easily readable to everyone, get news from researcher",
    expected_output="create a one line about each match, use your own experience to show news letter more attractive",
    agent=editor,
    context=[cricket_news]
)

crew = Crew(agents=[researcher,editor], tasks=[cricket_news, cricket_news_letter],process=Process.sequential, verbose=True)
result = crew.kickoff()
print(result)



