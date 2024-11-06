from transformers import AutoTokenizer, AutoModelForCausalLM
import os

# Tentukan path absolut model
model_path = r"D:\Hari Ini\Semester 8\Tugas\Thrive\tugasKursBI\Chatbot\Chatbot-custom\Chatbot\app\model\GPT-Neo-daniel"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_path)
print("Tokenizer loaded successfully.")

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True).to("cpu")
print("Model loaded successfully.")
