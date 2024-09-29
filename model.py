from transformers import T5Tokenizer, T5ForConditionalGeneration

model_name = "KhantKyaw/T5-small_new_chatbot"

tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def generate_response(input_text):
  input_ids = tokenizer.encode(input_text, return_tensors='pt')
  outputs = model.generate(input_ids, min_length=5, max_length=512, do_sample=True, num_beams=10, no_repeat_ngram_size=2)
  generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
  return generated_text