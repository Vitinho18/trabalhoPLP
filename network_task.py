class NetworkTask:
    def __init__(self, url):
        self.url = url
        self.status = 'pending'

    def execute(self):
        raise NotImplementedError("Execute method should be implemented by subclasses")
