# brushfire-api

A typed Python client for the [Brushfire API](https://developer.brushfire.com).

## Installation

```bash
pip install brushfire-api
```

## Usage

```python
import os
from brushfire_api import BrushfireClient

client = BrushfireClient(os.environ["BRUSHFIRE_API_KEY"])

events = client.get_events()
for event in events:
    print(event.Title)
```
