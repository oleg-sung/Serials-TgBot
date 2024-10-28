from typing import Any

import requests

from config import config


async def get_serials_by_name(name: str) -> list[dict[str, Any]]:
    params = {'q': name}
    response = requests.get(config.API_URL + 'search/shows', params=params, timeout=config.REST_TIMEOUT)
    data = response.json()
    return data


