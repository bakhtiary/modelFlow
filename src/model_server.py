class ModelServer:

    def __init__(self, list_of_adapters):
        self.list_of_adapters = list_of_adapters

    async def invoke(self, model_name):
        return self.list_of_adapters[0].invoke()

