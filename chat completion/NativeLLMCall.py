from openai import Client
from dotenv import load_dotenv
import os
load_dotenv()
key = os.environ.get('OPENAI_API_KEY')
client = Client(api_key=key)



def main():
    information = """
As a Senior Software Engineer with 6 years, I have been designing fault tolerant, scalable distributed systems, on cloud native platforms across finance,
education, health care and human capital management domains. I have specialized in AI/Machine Learning implementation including RAG pipelines,
LLM inference, agentic workflow design, specialized in developing microservice and monolithic architecture, migrating to cloud and distributed system.
Expertized in server-side optimization, scaling systems horizontal and vertical scaling, implementing fault recovery strategies, led debugging root cause
analysis ping pointing issue with Splunk, Grafana, Prometheus and provided deployment side support by designed CI/CD pipelines with Jenkins and
GitHub Actions along with designing Docker images and configuring Kubernetes. Also have mentored engineering teams/interns, establishing coding
standards, code reviews, engaged directly with and key stakeholders to elicit and analyze business requirements.
"""

    system_prompt = f"""
given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
"""
    response = client.chat.completions.create(model='gpt-4o-mini',
                                              messages=[
                                                  {'role':'system', 'content':system_prompt}
                                              ])
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()