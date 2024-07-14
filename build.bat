python -m venv .venv
call .\.venv\Scripts\activate.bat
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --console --onefile  --collect-submodules zeroconf .\server.py
