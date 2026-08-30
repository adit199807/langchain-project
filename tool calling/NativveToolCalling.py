from langchain.tools import tool
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
    dic ={'Apple':10, 'Mango':20, 'Avacado':2}
    return dic.get(product, 0)

@tool
def productDiscount(product:str):
    """Use this tool to get discount on product"""
    """
    Args:
        product: The name of product
    Return:
        discount on the product
    """
    dic ={'Apple':2, 'Mango':1, 'Avacado':0.5}
    return dic.get(product, 0)

ChatTemp = ChatPromptTemplate([
    SystemMessage(content='You are AI assistant. Help user, use provided tools if needed'),
    MessagesPlaceholder(variable_name='chatHistory')
])
chatHistory = []
tools = [productPrice, productDiscount]

def main():
    toolMap = {tool.name:tool for tool in tools}
    llm = init_chat_model(model=MODEL_NAME)
    llm = llm.bind_tools(tools)
    
    chain = ChatTemp | llm
    userInput = ''
    while userInput != 'exit':
        userInput  = input('Type in product name :')
        if userInput == 'exit':
            continue
        chatHistory.append(HumanMessage(content=userInput))
        response = chain.invoke(input={'chatHistory':chatHistory})
        if len(response.tool_calls):
            toolName = response.tool_calls[0]['name']
            args = response.tool_calls[0]['args']['product']
        print(toolName, args)
        print(response.content)
        chatHistory.append(AIMessage(content=response.content))


if __name__ == '__main__':
    main()