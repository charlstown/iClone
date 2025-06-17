#Usaremos Mistral 7B Instruct cuantizado a 4-bit (Q4_K_M) 
#para reducir el uso de VRAM y disco (~4.5-5 GB)

#LICENCIA = APACHE 2.0
#LENGUA ESPAÑOLA = OK

from huggingface_hub import hf_hub_download
from transformers import AutoTokenizer

# Descargar el modelo GGUF (Q4_K_M para 4 GB VRAM)
model_name = "TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF"
gguf_file = "mixtral-8x7b-instruct-v0.1.Q4_K_M.gguf"  # Archivo cuantizado 4-bit
model_path = hf_hub_download(
    repo_id=model_name,
    filename=gguf_file,
    local_dir="./mistral_7b_instruct",
    local_dir_use_symlinks=False
)

# Descargar el tokenizer de la versión no-GGUF
tokenizer_name = "mistralai/Mixtral-7B-Instruct-v0.1"
tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
tokenizer.save_pretrained("./mistral_7b_instruct")

print(f"Modelo GGUF guardado en: {model_path}")
print("Tokenizer guardado en: ./mistral_7b_instruct")

#Ejecuta "python test_descarga_Mixtral-7B-Instruct-v0.1-GGUF.py" para descargar