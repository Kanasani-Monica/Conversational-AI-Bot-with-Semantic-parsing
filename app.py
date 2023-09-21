from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_experimental.sql import SQLDatabaseChain

from utils.sidebar import sidebar
from utils.streaming import StreamHandler

from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

load_dotenv()

# Update the database URI to point to your enhanced_database.db
db_uri = "sqlite:///D:/University/challenge/Marketing List Chatbot/Solution/enhanced_database.db"
db = SQLDatabase.from_uri(db_uri)


# Streamlit App
sidebar()

st.title("Customer Insights App")
st.write("Welcome to the Customer Insights App. Enter your query below:")

query = st.text_area("Enter your query here:")

placeholder = st.empty()
placeholder.write("*[Agent Chatter will appear here]*")
st_cb = StreamHandler(placeholder)
chat = ChatOpenAI(streaming=True, callbacks=[st_cb])

db_chain = SQLDatabaseChain.from_llm(chat, db, verbose=True)

tools = [
    Tool(
        name="customers-DB",
        func=db_chain.run,
        description="useful for when you need to answer questions about customers, communication, interactions, life events, marketing campaigns, products, transactions"
    )
]

agent = initialize_agent(tools, chat, agent=AgentType.OPENAI_MULTI_FUNCTIONS, verbose=True)

if st.button("Get Insights"):
    response = agent.run(query)
    st.subheader("Response:")
    st.markdown(response)