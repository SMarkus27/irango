class StubRedisRepository:
    def __init__(self, return_value=None, *args, **kwargs):
        self.send_called = False
        self.set_called = False
        self.return_value = return_value

    def get(self, name=None):
        return self.return_value

    def set(self, name=None, value=None, ex=None):
        self.set_called = True