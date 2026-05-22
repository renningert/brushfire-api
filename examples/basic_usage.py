"""Basic usage examples for BrushfireClient."""

import os

from brushfire_api import BrushfireClient

API_KEY = os.environ["BRUSHFIRE_API_KEY"]

client = BrushfireClient(API_KEY)

events = client.get_events()
print(f"Found {len(events)} events")

if events:
    details = client.get_events_by_eventid(str(events[0].EventNumber))
    print(f"Title:  {details.Title}")
    print(f"Starts: {details.StartsAt}")
    print(f"Ends:   {details.EndsAt}")
