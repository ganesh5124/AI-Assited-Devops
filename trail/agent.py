from google.adk.agents.llm_agent import Agent
import datetime
from zoneinfo import ZoneInfo

def get_weather(city: str) -> dict:
    return {
        "city": city,
        "temperature": 30,
        "condition": "Sunny"
    }



def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[get_current_time],
)

log = get_weather("london")
print(log)