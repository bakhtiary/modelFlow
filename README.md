# modelFlow

## setup

pyenv -m venv venv
source venv/bin/activate
pip install -r requirements.locked.txt

## run server
uvicorn main:app --reload

## run server from docker
docker build . -t tmp && docker run -it -p8000:8000 tmp

## to lock requirments
pip install -r requirements.txt

pip freeze > requirements.locked.txt

