# Essential Libraries
import os
import logging
import re
from dotenv import load_dotenv
import time
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType, Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.memory import ConversationBufferMemory
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.agents import AgentOutputParser
from langchain.schema import AgentAction, AgentFinish


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log', filemode='a')

load_dotenv()

# Load Groq API Key
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize LLM with Groq (LLM: mixtral-8x7b-32768)
llm = ChatGroq(groq_api_key=groq_api_key, temperature=0.3)

# Initialize Search Tool
search_tool = DuckDuckGoSearchRun()

# Initialize Memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Initialize Vector Database for Knowledge Retention
embedding_model = HuggingFaceEmbeddings()
empty_document = Document(page_content="", metadata={})
vector_store = FAISS.from_documents([empty_document], embedding_model)

def save_to_memory(query, response):
    """Save search interactions in vector store."""
    doc = Document(page_content=response, metadata={"query": query})
    vector_store.add_documents([doc])

# Initialize Retrieval Chain for Knowledge Retrieval
retriever = vector_store.as_retriever()
retrieval_qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

# Medical Tool
def medical_info(query):
    """Retrieves medical information from internal knowledge or external sources."""
    try:
        structured_query = f"""
        Please provide factual, evidence-based information about: {query}
        
        If you don't have sufficient information, state this clearly.
        Focus only on well-established medical facts.
        """
        result = retrieval_qa.run(structured_query)
        return result
    except Exception as e:
        return f"Error retrieving medical information: {e}"

medical_tool = Tool(
    name="Medical Information Retrieval",
    func=medical_info,
    description="Useful for retrieving medical information about diseases, symptoms, treatments, and drugs.",
)

# Symptom Checker Tool
def symptom_check(symptoms):
    """Checks symptoms and provides possible conditions."""
    structured_query = f"""
    Given the following symptoms: {symptoms}, what are the possible medical conditions?
    
    If you don't have sufficient information, state this clearly.
    Focus only on well-established medical facts.
    """
    response = llm.predict(structured_query)
    return response

symptom_tool = Tool(
    name="Symptom Checker",
    func=symptom_check,
    description="Useful for checking symptoms and identifying possible medical conditions.",
)

# Drug Interaction Checker
def drug_interaction(drugs):
    """Checks for interactions between drugs."""
    structured_query = f"""
    Check for any interactions between the following drugs: {drugs}
    
    If you don't have sufficient information, state this clearly.
    Focus only on well-established medical facts.
    """
    response = llm.predict(structured_query)
    return response

drug_tool = Tool(
    name="Drug Interaction Checker",
    func=drug_interaction,
    description="Useful for checking drug-drug interactions.",
)

# Custom Prompt Template for Medical Context
template = """You are a helpful medical assistant. Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

{chat_history}
Question: {input}
{agent_scratchpad}

If you don't have sufficient information, state this clearly.
Focus only on well-established medical facts.
"""

prompt = PromptTemplate.from_template(template)

# Custom Output Parser
class CustomOutputParser(AgentOutputParser):
    def parse(self, llm_output: str) -> AgentAction | AgentFinish:
        if "Final Answer:" in llm_output:
            return AgentFinish(
                return_values={"output": llm_output.split("Final Answer:")[-1].strip()},
                log=llm_output,
            )

        regex = r"Action: (.*?)\nAction Input: (.*?)(?:\n|$)"
        match = re.search(regex, llm_output, re.DOTALL)
        if not match:
            raise ValueError(f"Could not parse LLM output: `{llm_output}`")
        action = match.group(1).strip()
        action_input = match.group(2).strip().replace("'", "").replace('"','')
        return AgentAction(tool=action, tool_input=action_input.strip(" "), log=llm_output)

output_parser = CustomOutputParser()

# Tools List
tools = [search_tool, medical_tool, symptom_tool, drug_tool]

# Initialize Agent
llm_with_stop = llm.bind(stop=["\nObservation:"])

agent_executor = initialize_agent(
    tools=tools,
    llm=llm_with_stop,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    memory=memory,
    max_iterations=5,  # Limit the number of iterations
    early_stopping_method="force"  # Force stop after max_iterations
)

def run_agent(user_input):
    start_time = time.time()
    logging.info(f"Starting agent execution for input: {user_input}")
    try:
        response = agent_executor.run(input=user_input)
        save_to_memory(user_input, response)
        end_time = time.time()
        logging.info(f"Agent execution completed in {end_time - start_time:.2f} seconds")
        logging.info(f"Response: {response}")
        return response
    except Exception as e:
        end_time = time.time()
        logging.error(f"An error occurred: {e}")
        logging.info(f"Agent execution failed in {end_time - start_time:.2f} seconds")
        return f"An error occurred: {e}"
