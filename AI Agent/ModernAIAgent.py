# Description: Usually AI Agents are build to let LLM have tool calling so that they can perfrom action in a deterministic way

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain.messages import HumanMessage

class Response(BaseModel):
    weather:str = Field(description='It contians the descriptions of weather')

@tool
def weatherApi(city:str):
    """This tool helps find weather of a city"""
    """
    Args:
        city: The city for which weather is to be looked up 
    Returns:
        Current weather of the city
    """
    return 'Its Sunny'

llm = ChatOpenAI(model='gpt-4o-mini')
agent = create_agent(model=llm, tools=[weatherApi],response_format=Response)

def main():
    print('Running the AI Agent file')
    result = agent.invoke(
            {
                "messages": HumanMessage(
                    content="What is weather of dallas city?"
                )
            }
        )
    print(result['structured_response'].weather)



if __name__ == '__main__':
    main()