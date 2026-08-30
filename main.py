from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
key = os.environ.get('OPENAI_API_KEY')


def main():
    print("Hello from langchain-project!")

    llm = OpenAI(model='gpt-4o-mini-2024-07-18')
    information = """
    As a Senior Software Engineer with 6 years, I have been designing fault tolerant, scalable distributed systems, on cloud native platforms across finance,
    education, health care and human capital management domains. I have specialized in AI/Machine Learning implementation including RAG pipelines,
    LLM inference, agentic workflow design, specialized in developing microservice and monolithic architecture, migrating to cloud and distributed system.
    Expertized in server-side optimization, scaling systems horizontal and vertical scaling, implementing fault recovery strategies, led debugging root cause
    analysis ping pointing issue with Splunk, Grafana, Prometheus and provided deployment side support by designed CI/CD pipelines with Jenkins and
    GitHub Actions along with designing Docker images and configuring Kubernetes. Also have mentored engineering teams/interns, establishing coding
    standards, code reviews, engaged directly with and key stakeholders to elicit and analyze business requirements.
    """
    system_prompt = """
    This is the information about a user:{information}. Perfrom following activity
    1. A short summary
    2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
            input_variables=["information"], template=system_prompt
        )
    chian = summary_prompt_template | llm
    response = chian.invoke(input={'information':information})

if __name__ == "__main__":
    main()
