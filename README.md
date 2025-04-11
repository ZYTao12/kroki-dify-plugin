## kroki

**Author:** zy
**Version:** 0.0.1
**Type:** extension

### Description

A Dify plugin that converts textual diagram descriptions into SVG diagrams using the Kroki service.

### Function
Converts textual code for various types of diagrams (UML, flowcharts, etc.) into SVG format that can be rendered directly in chat.

### Input Parameters
- `diagram_code`: The source code/textual description for generating the diagram
- `diagram_type`: The diagram format to use (default: plantuml)
  - Supports multiple diagramming languages including: PlantUML, Mermaid, Graphviz, C4 PlantUML, D2, BPMN, ERD, SVGbob and more. See [Kroki.io](https://kroki.io) for the full list of supported formats.

### Output
Returns a JSON object containing:
- `svg`: The generated SVG diagram content
- `url`: Direct URL to view the diagram on Kroki