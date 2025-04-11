from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
import requests


class KrokiProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            # Test Kroki service availability
            response = requests.get("https://kroki.io/")
            response.raise_for_status()
        except Exception as e:
            raise ToolProviderCredentialValidationError(f"Failed to connect to Kroki service: {str(e)}")
