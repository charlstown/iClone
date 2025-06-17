#Usaremos Mistral 7B Instruct cuantizado a 4-bit (Q4_K_M) 
#para reducir el uso de VRAM y disco (~4.5-5 GB)

#LICENCIA = APACHE 2.0
#LENGUA ESPAÑOLA = OK

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Descargar el modelo y tokenizer
model_name = "mistralai/Mistral-7B-Instruct-v0.2"
tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    trust_remote_code=True
)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use=True,
    trust_remote_code=True
)

# Guardar localmente
tokenizer.save_pretrained("./mistral_7b_instruct")
model.save_pretrained("./mistral_7b_instruct")

print("Modelo y tokenizer guardados en: ./mistral_7b_instruct")

#Ejecuta "python test_descarga_Mixtral-7B-Instruct-v0.1-GGUF.py" para descargar