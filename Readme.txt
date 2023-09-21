Team Design Challenge: Conversational Bot with Semantic Parsing
Project File Structure:


1. create_dedicated_tables.py: This Python script creates dedicated tables in the SQLite database using the provided Excel files and table configurations.
2. .env file: This contains your OpenAI API key.
3. requirements.txt: This file lists the required Python packages for the project.
4. enhanced_database.db: The enhanced SQLite database containing the tables and data.
5. data_preprocessing.py : Convert Excel files into prompt and completion pairs.
6. finetune.ipynb : Prepare and run the model for fine-tuning.
7. Challenge.ipynb: Fine Tuning and generating the treating, testing and validation files with the corresponding query and the results
8. validation_results.cvs: Model output on validation prompts.
9. train_results.csv: Model output on train prompts.
10. test_results: Model output on test prompts.
11. Past.py: Driver code


Project Execution Steps:


1. Make sure you have the latest version of Python (>=3.10.0) installed on your computer. (https://www.python.org/downloads/).
2. Open the command-line interface/Terminal and navigate to the project directory.
3. pip install -r requirements.txt: To install all the required libraries. If facing an issue with the package version use the virtual env
   1. Steps to create the virtual environment:
      1. Step1:  python -m venv venv
      2. Step2:  source venv/bin/activate
4. Run the ‘create_dedicated_tables.py’ script by executing the following command in your command line: python create_dedicated_tables.py (Note: you do not have to run the script again as the database has already been populated with all the required tables and we can use enhance_db.py)
5. streamlit run .\past.py : To run the Stream lit application.
6. Fine-tuned model: Feel free to test out our fine-tuned model (ft-personal:alpha-jarvis-2023-08-22-19-26-10) using our OpenAI API key given in the codebase. Make sure to include ‘->’ to mark the end of the prompt. Set the Configuration as shown below. 🙂