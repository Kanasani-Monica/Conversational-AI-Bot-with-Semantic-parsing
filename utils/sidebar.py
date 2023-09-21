import streamlit as st

content = '''
# Customer Insights App - User Guide

Welcome to the Customer Insights App User Guide! This guide will help you make the most out of the app and gain valuable insights from your SQL database.

## Getting Started

1. Open the app by running the application.
2. Enter your query in the provided text box.
3. Click the "Get Insights" button to receive the response.

## Features

- **Query Database:** Enter questions about your database to get detailed responses.
- **User-Friendly Interface:** The app is designed for easy navigation and interaction.
- **AI-Powered:** The app uses advanced AI to provide intelligent responses.

---

Thank you for using the Customer Insights App to explore your database and gain insights!
'''

def sidebar():
    with st.sidebar:
        st.markdown(content)
