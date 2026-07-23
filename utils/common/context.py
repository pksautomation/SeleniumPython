class BaseContext:
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
        return f"{self.__class__.__name__}({self._data!r})"


class FunctionContext(BaseContext):
    """Fresh for every single test method - never shared with another test."""


class ClassContext(BaseContext):
    """Shared across every test method within one test class, isolated from other classes."""


class SessionContext(BaseContext):
    """Shared across the entire test session, across every class and file."""
