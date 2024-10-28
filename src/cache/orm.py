import json
from typing import Any

import redis.asyncio as aioredis


redis_client = aioredis.Redis(host='redis', port=6379, db=0)


async def save_json_to_redis(data_key: str, json_data: list[dict[str, Any]]) -> None:
    print(f'Saving data to redis in {data_key}')
    await redis_client .set(data_key, json.dumps(json_data), ex=1000)


async def get_json_from_redis(data_key: str) -> list[dict[str, Any]]:
    print(f'Getting data in redis {data_key}')
    json_str = await redis_client.get(data_key)
    return json.loads(json_str) if json_str else []
