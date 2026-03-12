import asyncio
import httpx


async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com")
        print(response.status_code)

asyncio.run(fetch_data())