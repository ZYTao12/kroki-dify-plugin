from collections.abc import Generator
from typing import Any
import requests
import base64
import zlib

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class KrokiTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        # Get the diagram code and type from parameters
        diagram_code = tool_parameters.get('diagram_code', '')
        diagram_type = tool_parameters.get('diagram_type', 'plantuml').lower()
        
        # Validate diagram type
        supported_types = [
            'blockdiag', 'seqdiag', 'actdiag', 'nwdiag', 'packetdiag', 'rackdiag',
            'bpmn', 'bytefield', 'c4plantuml', 'd2', 'dbml', 'ditaa', 'erd',
            'excalidraw', 'graphviz', 'mermaid', 'nomnoml', 'pikchr', 'plantuml',
            'structurizr', 'svgbob', 'symbolator', 'tikz', 'umlet', 'vega',
            'vegalite', 'wavedrom', 'wireviz'
        ]
        
        if diagram_type not in supported_types:
            yield self.create_text_message(f"Unsupported diagram type. Supported types are: {', '.join(supported_types)}")
            return

        try:
            # Compress the diagram code
            compressed = zlib.compress(diagram_code.encode('utf-8'))
            # Base64 encode the compressed data
            encoded = base64.urlsafe_b64encode(compressed).decode('utf-8')
            
            # Construct the Kroki URL
            kroki_url = f"https://kroki.io/{diagram_type}/svg/{encoded}"
            
            # Get the SVG from Kroki
            response = requests.get(kroki_url)
            response.raise_for_status()
            
            # Return the SVG content
            yield self.create_json_message({
                "svg": response.text,
                "url": kroki_url
            })
            
        except Exception as e:
            yield self.create_text_message(f"Error generating diagram: {str(e)}")
