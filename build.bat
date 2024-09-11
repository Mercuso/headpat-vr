python -m venv .venv  || exit /b
call .\.venv\Scripts\activate  || exit /b
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --console --onefile  --collect-submodules zeroconf --name headpat-vr-server .\server.py
