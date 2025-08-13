from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template="What is the capital of {input}?",
    input_variables=["input"]
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"input": "France"})

print(result)  # Output: Paris
print(type(result))  # Output: <class 'str'>

chain.get_graph().print_ascii()
# This will print the graph of the chain in ASCII format

