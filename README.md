# Multimodal RAG - MiG-29

## Windows Setup Reference

Open **Command Prompt** and move to the project directory:

```cmd
cd /d "C:\Users\User\Desktop\AI\Pratik_GEN_AI\GENAI\MultiModal_RAG"
```

Activate the existing virtual environment:

```cmd
multimodal_rag_mig\Scripts\activate
```

Install or update the project dependencies with `uv`:

```cmd
uv sync --active --no-install-project
```

The project uses `pdf2image`, which requires Poppler on Windows. If you have `winget`, install it once:

```cmd
winget install --id oschwartz10612.Poppler -e
```

If you do not have `winget`, download the [prebuilt Windows package (`Release-26.09.0-0.zip`)](https://github.com/oschwartz10612/poppler-windows/releases/download/v26.09.0-0/Release-26.09.0-0.zip) and extract it. Do not download GitHub's **Source code (zip)** archive. Add the extracted `Library\bin` folder to your Windows `Path` environment variable. For example, if you extracted it to `C:\Tools\poppler`, add `C:\Tools\poppler\Library\bin`.

Close and reopen Command Prompt after installation, then verify Poppler:

```cmd
where pdfinfo
where pdftoppm
```

Set `EURI_API_KEY` in the project `.env` file for answer generation. `GEMINI_API_KEY` is still required for image embeddings. The answer model defaults to `gemini-3.1-pro-preview` and can be changed with `EURI_MODEL`. Then run the application:

```cmd
python qdrant_rag_system\main.py
```

## Qdrant

Docker is optional. If Qdrant Docker is unavailable, the application automatically uses the local `qdrant_storage` directory.

If Docker Desktop is installed and virtualization is enabled, start Qdrant from Command Prompt:

```cmd
docker run -d --name qdrant --restart unless-stopped -p 6333:6333 -p 6334:6334 -v "%cd%\qdrant_storage:/qdrant/storage" qdrant/qdrant
```

For an existing stopped container:

```cmd
docker start qdrant
```

Qdrant dashboard:

http://localhost:6333/dashboard

## Stop the Application

Type `exit` or `quit` in the application, or press `Ctrl+C`.