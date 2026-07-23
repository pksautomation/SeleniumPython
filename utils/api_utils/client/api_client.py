import logging

import requests


class ApiClient:
    def __init__(self, base_url, timeout=10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.logger = logging.getLogger("api")
        self.session = requests.Session()
        self.session.hooks["response"].append(self._log_response)

    def _log_response(self, response, *args, **kwargs):
        self.logger.info(
            "%s %s -> %s (%.3fs)",
            response.request.method,
            response.request.url,
            response.status_code,
            response.elapsed.total_seconds(),
        )
        return response

    def get(self, path, **kwargs):
        return self.session.get(f"{self.base_url}{path}", timeout=self.timeout, **kwargs)

    def post(self, path, **kwargs):
        return self.session.post(f"{self.base_url}{path}", timeout=self.timeout, **kwargs)

    def put(self, path, **kwargs):
        return self.session.put(f"{self.base_url}{path}", timeout=self.timeout, **kwargs)

    def delete(self, path, **kwargs):
        return self.session.delete(f"{self.base_url}{path}", timeout=self.timeout, **kwargs)
