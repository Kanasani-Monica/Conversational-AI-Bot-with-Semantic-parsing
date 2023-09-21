import pandas as pd
import json

excel_file_path = '"D:/University/challenge/Marketing List Chatbot/Questions/Training.xlsx"'
jsonl_file_path = 'file.jsonl'

data_frame = pd.read_excel(excel_file_path)

with open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:
    for _, row in data_frame.iterrows():
        prompt_text = row['Question']
        ideal_generated_text = row['Query']
        
        data = {
            "prompt": prompt_text,
            "completion": ideal_generated_text
        }
        
        jsonl_file.write(json.dumps(data, ensure_ascii=False) + '\n')

print("Conversion completed successfully.")
