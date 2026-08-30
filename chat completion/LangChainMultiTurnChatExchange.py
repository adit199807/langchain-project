from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(model='gpt-4o-mini')
chat_history = []

def main():
    chatTemplate = ChatPromptTemplate.from_messages([
        SystemMessage(content='You are a helpful AI assistant.'),
        MessagesPlaceholder(variable_name="chat_history"),
    ])
    chain = chatTemplate | llm
    count = 0

    while count < 2:
        new_user_query = input("Please enter your query: ")
        chat_history.append(HumanMessage(content=new_user_query))
        response = chain.invoke(input={'new_user_query':new_user_query, 'chat_history':chat_history})
        print(response.content)
        chat_history.append(response)
        count+=1

if __name__ == '__main__':
    main()