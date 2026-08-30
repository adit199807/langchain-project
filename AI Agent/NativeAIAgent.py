# Description: 

from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

key = os.environ.get('OPENAI_API_KEY')
load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')

def main():

    pass


if __name__ == '__main__':
    main()