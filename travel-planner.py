from crewai import LLM, Agent,Task, Crew
from dotenv import load_dotenv

load_dotenv()

city = input("Which city? ")
llm = LLM(model = 'gpt-4o-mini')

travelAgent = Agent(
    role="Travel planner",
    goal="explain in simple words to understand users clearly",
    backstory="you are a 10 years exprienced travel guide in india across all the states you have travelled",
    llm=llm,
    verbose=False
)

planForThreeDaysTrip = Task(
    description="Give me a three days travel plan in {city}, sites should be most popular places",
    expected_output="Give me in short list format 3 places per day",
    agent=travelAgent
)
crew = Crew(agents=[travelAgent], tasks=[planForThreeDaysTrip], verbose=False)
result = crew.kickoff(inputs={"city": city})
print(result)