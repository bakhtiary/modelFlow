import unittest
from unittest.mock import Mock, MagicMock

import pytest

from wiring import Wiring
from VertexEmbeddingAdapter import VertexEmbeddingAdapter
from fastapi.testclient import TestClient


class TestMain(unittest.TestCase):


    def setUp(self):
        self.vertex_embedding_adapter = Mock(VertexEmbeddingAdapter)
        wiring = Wiring(mocks={VertexEmbeddingAdapter:self.vertex_embedding_adapter})
        self.client = TestClient(wiring.up())

    def test_main(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}

    def test_vertex_text_embedding(self):
        self.vertex_embedding_adapter.invoke = MagicMock(return_value=[1,2,3,4])
        response = self.client.post("/models/text-embedding-004/invoke")
        assert "2,3,4" in response.text



