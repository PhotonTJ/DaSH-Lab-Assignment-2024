from groq import Groq
import json
import time
import os

def process_prompt(prompt, client_number):
    client = Groq(api_key="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")
    
    time_sent = int(time.time())
    
    try:
        chat_completion = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {"role": "system", "content": "Provide the output in JSON"},
                {"role": "user", "content": prompt}
            ]
        )
        
        time_received = int(time.time())
        
        output = {
            "Prompt": prompt,
            "Message": chat_completion.choices[0].message.content,
            "TimeSent": time_sent,
            "TimeRecvd": time_received,
            "Source": "Groq-Mixtral"
        }
        
        json_output = json.dumps(output, indent=2)
        print(f"Client {client_number} output:")
        print(json_output)
        
        output_file_path = f'C:\\Users\\acer\\Desktop\\Dash Assignments\\Dev\\Level 2\\output_client_{client_number}.json'
        with open(output_file_path, 'w') as json_file:
            json.dump(output, json_file, indent=2)
        
        print(f"JSON output for Client {client_number} has been saved to {output_file_path}")
    
    except Exception as e:
        print(f"An error occurred for Client {client_number}: {e}")


input_file_path = 'C:\\Users\\acer\\Desktop\\Dash Assignments\\Dev\\Level 2\\input.txt'
with open(input_file_path, 'r') as file:
    prompts = file.readlines()


for i, prompt in enumerate(prompts, 1):
    prompt = prompt.strip()
    if prompt:  
        process_prompt(prompt, i)