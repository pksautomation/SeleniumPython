class TestContext:
    __test__ = False  # tell pytest not to collect this as a test class (name starts with "Test")

    def __init__(self):
        self._data = {}

    def set(self, key, value):
        self._data[key] = value
        return value

    def get(self, key, default=None):
        return self._data.get(key, default)

    def has(self, key):
        return key in self._data

    def clear(self):
        self._data.clear()

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]

    def __contains__(self, key):
        return key in self._data

    def __repr__(self):
        return f"TestContext({self._data!r})"
