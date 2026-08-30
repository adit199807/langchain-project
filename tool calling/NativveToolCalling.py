from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
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

tools = [productPrice, productDiscount]
chatHistory = []

def main():
    toolMap = {tool.name:tool for tool in tools}
    llm = init_chat_model(model=MODEL_NAME)
    llm = llm.bind_tools(tools)
    
    userInput = ''
    # userInput  = input('Type in product name :')
    chatHistory.append(HumanMessage(content='Price of Avacado'))

    for iteration in range(1, MAX_ITERATION + 1):
        aiMessage = llm.invoke(chatHistory)
        tool_calls = aiMessage.tool_calls
        if not tool_calls:
            chatHistory.append(AIMessage(content=aiMessage.content))
            print(aiMessage.content)
            break
        
        tool_call = tool_calls[0]
        tool_name = tool_call.get("name")
        tool_args = tool_call.get("args", {})
        tool_call_id = tool_call.get("id")
        tool_to_use = toolMap.get(tool_name)

        if tool_to_use is None:
            raise ValueError(f"Tool '{tool_name}' not found")
        chatHistory.append(aiMessage)
        observation = tool_to_use.invoke(tool_args)
        chatHistory.append(ToolMessage(content=str(observation), tool_call_id = tool_call_id))


if __name__ == '__main__':
    main()