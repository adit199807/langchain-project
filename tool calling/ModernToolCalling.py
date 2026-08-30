from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field

MODEL_NAME = 'gpt-4o-mini'
MAX_ITERATION = 10

class Response(BaseModel):
    response:str = Field('Final response')

@tool
def productPrice(product:str):
    """Use this tool to get product price"""
    """
    Args:
        product: The name of product
    Return:
        Price of the product
    """
    product = product.lower()
    dic ={'apple':10, 'mango':20, 'avacado':2}
    return dic.get(product, 0)

@tool
def productDiscount(product:str):
    """Use this tool to get discount on product"""
    """
    Args:
        product: The name of product
    Return:
        discount on the product in dollars
    """
    dic ={'Apple':2, 'Mango':1, 'Avacado':0.5}
    return dic.get(product, 0)

tools = [productPrice, productDiscount]

def main():
    llm = init_chat_model(model=MODEL_NAME)
    agent = create_agent(llm, tools=tools)
    userInput = ''
    while userInput != 'exit':
        userInput  = input('Type in product name :')
        if userInput == 'exit':
            continue
        response = agent.invoke(
            input={
                'messages' : [HumanMessage(content=userInput)]
            }
        )
        print(response['messages'][-1].content)

if __name__ == '__main__':
    main()