from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from dotenv import load_dotenv
import os

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('openapi_key')
llm = ChatGroq(model_name="llama3-8b-8192" )


def generate_resturant_name_and_items(cuisine):

    prompt_template_name = PromptTemplate(
        input_variables = ['cuisine'],
        template = "Suggest a unique and creative name for {cuisine} restaurant. Only return one name, nothing else."
        )

    name_chain = LLMChain(llm = llm , prompt = prompt_template_name , output_key = "resturant_name")

    prompt_template_items = PromptTemplate(
        input_variables = ['resturant_name'],
        template = "List 5 of menu items for {resturant_name} in main course .Return it as comma separated list , nothing else"
    )

    food_items_chain = LLMChain(llm = llm , prompt = prompt_template_items , output_key = "food_items")

    chain = SequentialChain(
        chains = [name_chain , food_items_chain],
        input_variables = ['cuisine'],
        output_variables = ['resturant_name' , 'food_items']
    )

    response = chain.invoke({"cuisine" : cuisine})

    return {
        'resturant_name':  response['resturant_name'],
        'menu_items' : response['food_items']
    }