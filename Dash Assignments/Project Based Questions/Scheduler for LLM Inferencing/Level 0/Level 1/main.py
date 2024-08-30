from groq import Groq
import json
import time

client = Groq(api_key="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")

with open('C:\\Users\\acer\\Desktop\\Dash Assignments\\Dev\\Level 1\\input.txt', 'r') as file:
    prompts = file.read().strip()

time_sent = int(time.time())

try:
    chat_completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {"role": "system", "content": "Provide the output in JSON"},
            {"role": "user", "content": prompts}
        ]
    )

    time_received = int(time.time())
    output = {
        "Prompt": prompts,
        "Message": chat_completion.choices[0].message.content,
        "TimeSent": time_sent,
        "TimeRecvd": time_received,
        "Source": "Groq-Mixtral"
    }

    json_output = json.dumps(output, indent=2)
    print(json_output)

    
    output_file_path = 'C:\\Users\\acer\\Desktop\\Dash Assignments\\Dev\\Level 1\\output.json'
    with open(output_file_path, 'w') as json_file:
        json.dump(output, json_file, indent=2)
    
    print(f"JSON output has been saved to {output_file_path}")

except Exception as e:
    print(f"An error occurred: {e}")