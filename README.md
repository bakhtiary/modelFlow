# modelFlow

## setup

pyenv -m venv venv
source venv/bin/activate
pip install -r requirements.locked.txt

# to lock requirments
pip install -r requirements.txt
pip freeze >> requirements.locked.txt

