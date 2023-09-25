class StubRedis:
    def __init__(self, *args, **kwargs):
        self.send_called = False