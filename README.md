# brushfire-api

A typed Python client for the [Brushfire API](https://developer.brushfire.com), with models and endpoints generated from the official OpenAPI spec.

## Setup

```bash
pip install ".[dev]"
```

## Generating the client

The client code is generated from the Brushfire OpenAPI spec. Run this whenever the API version changes:

```bash
python generate_api.py
```

This will:
1. Run `datamodel-codegen` to generate `src/brushfire_api/models.py`
2. Generate `src/brushfire_api/api.py` with a typed `BrushfireClient`
3. Generate `tests/test_api.py`

The API version and output paths are configured in `pyproject.toml`.

## Usage

```python
import os
from brushfire_api import BrushfireClient

client = BrushfireClient(os.environ["BRUSHFIRE_API_KEY"])

events = client.get_events()
for event in events:
    print(event.Title)
```

See `examples/basic_usage.py` for a runnable example:

```bash
BRUSHFIRE_API_KEY=your_key python examples/basic_usage.py
```

## Running tests

```bash
pytest tests/test_api.py
```
