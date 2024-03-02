
run-server-docker:
    docker build . -t tmp && docker run -p 8000:8000 -it tmp

run-server-venv:
	. venv/bin/activate && cd src && uvicorn main:app

portforward:
	kubectl proxy