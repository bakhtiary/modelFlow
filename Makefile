
run-server-docker:
	docker build . -t tmp && docker run -p 8000:8000 -it tmp

run-server-venv:
	. venv/bin/activate && cd src && uvicorn main:app

portforward:
	kubectl proxy

start-kind-cluster:
	- rm ~/.kube/config
	kind create cluster --config cluster-setup/kind.yaml

delete-kind-cluster:
	kind delete clusters modelflow

.PHONY: deploy-k8s
deploy-k8s:
	TAG=$$( date +'%y-%m-%d-%H-%M-%S' ); \
	docker build . -t modelflow:$$TAG; \
	kind load docker-image modelflow:$$TAG --name modelflow ; \
	./apply_kustomize_changing_image_names.sh  k8s-setup "modelflow=modelflow:$$TAG" | kubectl apply -f -