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
    new_user_query = ''

    while new_user_query != 'exit':
        new_user_query = input("Please enter your query:")
        if new_user_query == 'exit':
            continue
        chat_history.append(HumanMessage(content=new_user_query))
        response = chain.invoke(input={'chat_history':chat_history})
        print(response.content)
        chat_history.append(AIMessage(content=response.content))

if __name__ == '__main__':
    main()