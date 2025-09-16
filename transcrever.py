import whisper
import subprocess
import os

def baixar_audio(url, saida="audio.mp3"):
    comando = ["yt-dlp", "-x", "--audio-format", "mp3", "-o", saida, url]
    subprocess.run(comando, check=True)

def transcrever_audio(caminho_audio, modelo="small"):
    model = whisper.load_model(modelo)
    resultado = model.transcribe(caminho_audio, language="pt")
    return resultado["text"]

if __name__ == "__main__":
    url = os.getenv("INPUT_URL", "")
    if not url:
        print("Nenhuma URL fornecida em INPUT_URL")
        exit(1)

    arquivo_audio = "audio.mp3"
    if not os.path.exists(arquivo_audio):
        baixar_audio(url, arquivo_audio)

    texto = transcrever_audio(arquivo_audio, modelo="small")
    with open("transcricao.txt", "w", encoding="utf-8") as f:
        f.write(texto)
    print("✅ Transcrição salva em transcricao.txt")
