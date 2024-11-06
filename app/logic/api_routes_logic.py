from flask import jsonify, request
from app.services.logging_service import LoggerService
from app.middleware.token_verify import TokenService
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import LoraConfig, get_peft_model
import torch
import os

logger_service = LoggerService()
logger = logger_service.get_logger()
token_service = TokenService()

class RouteLogic:
    def __init__(self):
        logger.info("Inisialisasi RouteLogic dimulai...")
        try:
            self.company_id = None
            model_path = os.path.join(os.getcwd(), "app", "model", "GPT-Neo-daniel")
            
            # Load tokenizer
            logger.info("Memuat tokenizer dari path: %s", model_path)
            self.tokenizer = AutoTokenizer.from_pretrained(model_path)
            logger.info("Tokenizer berhasil dimuat.")
            
            # Load base model
            logger.info("Memuat model dasar dari path: %s", model_path)
            base_model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True).to("cpu")
            logger.info("Model dasar berhasil dimuat.")
            
            # Apply LoRA configuration
            logger.info("Menerapkan konfigurasi LoRA pada model.")
            peft_args = LoraConfig(
                lora_alpha=64,
                lora_dropout=0.1,
                r=8,
                bias="none",
                task_type="CAUSAL_LM"
            )
            
            # Wrap model with LoRA
            self.model = get_peft_model(base_model, peft_args)
            logger.info("Model berhasil dimuat dan dikonfigurasi dengan LoRA.")
        
        except Exception as e:
            logger.error("Gagal dalam inisialisasi RouteLogic: %s", str(e))
            raise e  # Raise to stop execution if initialization fails

    def generate_response(self, message):
        logger.info("Menerima pesan untuk generate response.")
        try:
            # Generate response using the loaded model
            input_ids = self.tokenizer.encode(message, return_tensors="pt").to("cpu")
            output_ids = self.model.generate(input_ids, max_length=100, temperature=0.5)
            response = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
            logger.info("Response berhasil di-generate.")
            return response
        except Exception as e:
            logger.error("Kesalahan dalam generate_response: %s", str(e))
            return "Error in generating response"

    @token_service.token_required
    def generate(self):
        try:
            # Parse JSON request
            data = request.get_json()
            message = data.get("inputs", "")
            logger.info("Request JSON berhasil di-parse. Pesan: %s", message)

            # Generate response from the model
            if message:
                generated_text = self.generate_response(message)
                logger.info("Response dikirim ke client.")
                return jsonify({"GPT Neo Custom": generated_text})
            else:
                logger.warning("Tidak ada pesan yang diberikan dalam permintaan.")
                return jsonify({"error": "No message provided"}), 400

        except Exception as e:
            logger.error("Terjadi kesalahan saat generate response: %s", str(e))
            return jsonify({"error": str(e)}), 500
