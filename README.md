# 🎥📝 YouTube Whisper Transcriber

Ferramenta para **baixar áudio de vídeos do YouTube** com [yt-dlp](https://github.com/yt-dlp/yt-dlp) e **transcrever automaticamente** usando [OpenAI Whisper](https://github.com/openai/whisper).  
Tudo isso empacotado em **Docker**, com automação de infraestrutura via **Terraform** e deploy contínuo no **GitHub Actions**.

---

## 🚀 Funcionalidades

- 📥 Download automático de áudio do YouTube (formato `.mp3`)
- 🤖 Transcrição em português usando modelos do Whisper
- 🐳 Container Docker pronto para rodar em qualquer ambiente
- ⚡ Automação da criação do repositório e workflows via Terraform
- ☁️ Publicação de imagens Docker no **GitHub Container Registry (GHCR)**

---

## 📂 Estrutura do Projeto

```bash
.
├── Dockerfile             # Imagem Docker com yt-dlp + Whisper
├── requirements.txt       # Dependências Python
├── transcrever.py         # Script principal de download + transcrição
├── .github/workflows/ci.yml # CI/CD para build + publish no GHCR
└── README.md              # Este arquivo :)
