# Conversational-AI-Bot-with-Semantic-parsing
### Problem statement:
The task is to design an advanced chatbot solution for a financial services company, leveraging semantic parsing and text-to-SQL techniques. The chatbot should be able to understand natural language queries from employees and convert them into structured SQL queries to retrieve and present information related to customer profiles, customer interactions, company products, and past marketing campaigns. The goal is to create a user-friendly, AI-driven tool that empowers employees with efficient access to critical data for improved customer engagement and informed decision-making.
Here is an example of how marketing lists are created in a company using a "Dynamics 360" tool
https://www.youtube.com/watch?v=iqyMnGbOVMw

Generating the marketing lists is a quite intense process, involves multiple steps, several back and forth analysis between multiple teams, which presents itself as a pain-point. A solution that can understand the employee question and gets the marketing list customers, would immensely reduce the pain-point, increase the efficiency, and reduce the turnaround time to get the marketing list customers. 


Ex: For the below question:
﻿"Give me a list of married customers with at least two dependents in Arizona state", we expect below query to be generated:
SELECT  c.customer_id,  c.first_name,  c.last_name 
FROM  customers c 
WHERE  c.marital_status = 'married'  AND c.number_of_dependents >= 2  AND c.state = 'Arizona';
and the output should include the above SQL query, and the  executed result from SQL query (list of customers information)

Note: Instruction to run the code are given in the Readme.txt file
