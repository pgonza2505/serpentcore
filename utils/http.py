from __future__ import annotations
import asyncio
import json
from typing import Any, Optional

import aiohttp


async def _get_json(
    url: str,
    *,
    headers: dict | None = None,
    timeout: int = 10,
) -> Optional[dict[str, Any]]:
    """
    Simple JSON HTTP GET helper.

    - New ClientSession per call (no shared-state weirdness).
    - Optional headers.
    - Returns parsed JSON dict or None on failure.
    """
    headers = headers or {}
    client_timeout = aiohttp.ClientTimeout(total=timeout)

    async with aiohttp.ClientSession(headers=headers, timeout=client_timeout) as session:
        try:
            async with session.get(url) as resp:
                if resp.status != 200:
                    print(f"[http] GET {url} -> {resp.status}")
                    return None

                try:
                    return await resp.json()
                except aiohttp.ContentTypeError:
                    txt = await resp.text()
                    try:
                        return json.loads(txt)
                    except json.JSONDecodeError:
                        print(f"[http] Non-JSON response from {url}")
                        return None
        except (aiohttp.ClientError, aiohttp.ServerTimeoutError, asyncio.TimeoutError) as e:
            print(f"[http] Error fetching {url}: {e}")
            return None
