from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from app.config import Config



llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        api_key=Config.qroq_api_key,
        )

prompt1=PromptTemplate(
    template="You are a powerful recommender system for gadgets. Suggest some alternative items for this product : {product},give the list of the products with thier features.",
    input_variable=['product']
)

parser=StrOutputParser()

chain= prompt1 | llm | parser 


def recommend_gadget(product: str) -> str:
    return chain.invoke({"product": product})
