# RAG with Ollama

## Setup Ollama, Phi3 and embed model

Install Ollama, pull a few models

<https://github.com/ollama/ollama/blob/main/docs/linux.md>

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull phi3
```

## Setup Cuda (if necessary)

<https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_network>

```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-4
nvidia-smi
```

## Setup Python + libraries

I'm using pyenv + virtual environments, so set up Python env any way you like. Then you can install the requirements like so:

```bash
pip install ollama chromadb feedparser
```

## How to use?

You can run the scripts using Python. rag-read-and-store-data.py will do what the name tells, rag-query-data.py will use the embeddings in chromadb database to answer questions (modify the prompts to your likings) - and rag-cleanup-data.py can be used to cleanup database if you don't need it anymore.

Additionally there's a version with speech synthesis that requires some extra libs but can be awesome :)


## Optional: Install speech parts if you like to run those experiments


```bash
pip install coqui-tts SpeechRecognition pyaudio sounddevice
```



## Optional: WSL2 Cuda fix if it's not working

Hmm optional WSL2 fix if needed, to get the correct nvidia lib from Windows drivers showing:

```bash
export LD_LIBRARY_PATH=/mnt/c/Windows/System32/lxss/lib:$LD_LIBRARY_PATH
```


## Optional: WSL2 enable systemctl if it's not active

systemctl may or may not be working in your WSL, it depends on how archaic version you have. If it's not, you can set it up, or just run 'ollama serve' manually when using it, to have the service available.

If you don't have systemd, and need to fix it, you can try these instructions:


Add these lines to the /etc/wsl.conf note you will need to run your editor with sudo privileges, e.g: sudo nano /etc/wsl.conf

```
[boot]
systemd=true
```

And close out of the nano editor using CTRL+O to save and CTRL+X to exit.

Shutdown wsl and restart ubuntu (wsl --shutdown in admin powershell)

Check if systemctl works now:

```
sudo systemctl status
```

... should show your Systemd services.
