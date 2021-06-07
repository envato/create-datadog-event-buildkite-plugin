#!/usr/bin/env python3

import os
import json

def plugin_var_name(name):
  return f"BUILDKITE_PLUGIN_CREATE_DATADOG_EVENT_{name.upper()}"

def get_var(name, default=None):
  return os.environ.get(plugin_var_name(name), default)

payload = {}

def add_var(key, default=None):
  value = get_var(key, default)

  if value is not None:
    payload[key] = value

add_var("title")
add_var("text")
add_var("host")
add_var("aggregation_key")
add_var("related_event_id")
add_var("source_type_name")
add_var("priority", "normal")
add_var("alert_type", "info")

tags = []
tag_number = 0

while plugin_var_name(f"TAGS_{tag_number}") in os.environ.keys():
  tags.append(os.environ[plugin_var_name(f"TAGS_{tag_number}")])
  tag_number += 1

if any(tags):
  payload['tags'] = tags

print(json.dumps(payload))
