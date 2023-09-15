class StubMongoDBOperations:
    def __init__(self, data=None):
        self.insert_one_called = False
        self.find_one_called = False
        self.data = data
        self.total_items = 0
        self.sorted_field = None
        self.update_one_called = False
        self.delete_one_called = False

    async def insert_one(self, data: dict):
        self.insert_one_called = True

    async def find_one(self, data: dict, projection: dict):
        return self.data

    def find(self, query: dict, projection: dict):
        return StubMongoDBOperations(self.data)

    async def update_one(
        self,
        query,
        update_data,
        array_filters: list | None = None,
        upsert: bool = False,
    ):
        self.update_one_called = True

    async def delete_one(self, query):
        self.delete_one_called = True

    async def count_documents(self, query: dict):
        self.total_items = len(self.data)
        return self.total_items

    def sort(self, sort=None):
        data = self.data
        self.sorted_field = sort
        data.sort(key=self.my_sort)
        return StubMongoDBOperations(self.data)

    async def to_list(self, limit=None):
        data = self.data
        return data[:limit]

    def skip(self, skip=None):
        return StubMongoDBOperations(self.data[skip:])

    def limit(self, limit=None):
        return StubMongoDBOperations(self.data[:limit])

    def my_sort(self, data):
        return data[self.sorted_field]
