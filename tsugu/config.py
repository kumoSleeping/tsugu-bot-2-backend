import os
import json
from dotenv import dotenv_values
from tsugu_api_core import settings


def load_config():
    kv = dotenv_values(".env")
    result = {
        "timeout": 120,
        "proxy": "",
        "backend_url": "http://tsugubot.com:8080",
        "backend_proxy": True,
        "userdata_backend_url": "http://tsugubot.com:8080",
        "userdata_backend_proxy": True,
        "use_easy_bg": True,
        "compress": True,
    }

    for k, v in os.environ.items():
        if k.startswith("TSUGU_"):
            result[k.lower()] = v

    for k, v in kv.items():
        if v is None:
            continue
        try:
            result[k.lower()] = json.loads(v.lower())
        except json.JSONDecodeError:
            result[k.lower()] = v
    return result


def apply_config(config: dict):
    for k, v in config.items():
        k = k.lower().removeprefix("tsugu_")
        if hasattr(settings, k):
            setattr(settings, k, v)
        else:
            print(f"Unknown config key: {k}")
