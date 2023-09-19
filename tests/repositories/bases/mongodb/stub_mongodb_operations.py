class StubMongoDBOperations:
    def __init__(self, data=None):
        self.insert_one_called = False
        self.find_one_called = False
        self.data = data
        self.total_items = 0
        self.sorted_field = None
        self.update_one_called = False
        self.delete_one_called = False

    def insert_one(self, data: dict):
        self.insert_one_called = True

    def find_one(self, data: dict, projection: dict):
        return self.data

    def find(self, query: dict, projection: dict):
        return self.data

    def update_one(
        self,
        query,
        update_data,
        array_filters: list | None = None,
        upsert: bool = False,
    ):
        self.update_one_called = True

    def delete_one(self, query):
        self.delete_one_called = True

    def count_documents(self, query: dict):
        self.total_items = len(self.data)
        return self.total_items

    def sort(self, sort=None):
        data = self.data
        self.sorted_field = sort
        data.sort(key=self.my_sort)
        return StubMongoDBOperations(self.data)

    def to_list(self, limit=None):
        data = self.data
        return data[:limit]

    def skip(self, skip=None):
        return StubMongoDBOperations(self.data[skip:])

    def limit(self, limit=None):
        return StubMongoDBOperations(self.data[:limit])

    def my_sort(self, data):
        return data[self.sorted_field]
