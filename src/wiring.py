from typing import Dict

from VertexEmbeddingAdapter import VertexEmbeddingAdapter
from model_controller import build_model_controller
from model_server import ModelServer


class Wiring:
    def __init__(self, mocks: Dict[object, object]):
        self.mocks = mocks

    def up(self):
        vertex_embedding_adapter = self.mocks.get(VertexEmbeddingAdapter, VertexEmbeddingAdapter())
        return build_model_controller(ModelServer([vertex_embedding_adapter]))