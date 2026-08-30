from openai import Client
from dotenv import load_dotenv
import os

load_dotenv()
key = os.environ.get('OPENAI_API_KEY')
client = Client(api_key=key)
chatHistory = [{'role':'system', 'content' : 'Your are an helpful AI assitent'}]
def main():
    userInput = ''
    while userInput!= 'exit':
        userInput = input('please type your question:')
        if userInput == 'exit':
            continue
        chatHistory.append({'role':'user', 'content':userInput})
        response = client.chat.completions.create(model='gpt-4o-mini',messages= chatHistory)
        print(response.choices[0].message.content)
        chatHistory.append({'role':'system', 'content':response.choices[0].message.content})

if __name__ == '__main__':
    main()