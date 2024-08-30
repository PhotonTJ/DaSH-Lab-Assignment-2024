from transformers import GPT2LMHeadModel,GPT2Tokenizer

tokenizer=GPT2Tokenizer.from_pretrained('gpt-2')

model=GPT2LMHeadModel.from_pretrained('gpt-2')

prompt="Paris is the capital if France"

input_ids=tokenizer.encode(prompt,return_tensors='pt')

output=model.generate(input_ids,max_length=50,num_return_sequences=1)

output_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(output_text)