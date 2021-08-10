import asyncio
import random
import string
from functools import partial

from tornado.httpclient import AsyncHTTPClient, HTTPClient

AsyncHTTPClient.configure(
    "tornado.curl_httpclient.CurlAsyncHTTPClient",
    max_clients=100,
)

def generate_urls(base_url: str, num_urls: int):
    for i in range(num_urls):
        yield base_url + "".join(random.sample(string.ascii_lowercase, 10))

async def run_experiment(base_url: str, num_iter=1000) -> int:
    http_client = AsyncHTTPClient()
    urls = generate_urls(base_url, num_iter)
    response_sum = 0
    tasks = [http_client.fetch(url) for url in urls]
    for task in asyncio.as_completed(tasks):
        response = await task
        response_sum += len(response.body)
    
    return response_sum

if __name__ == "__main__":
    import time

    delay = 100
    num_iter = 10
    run_func = partial(
        run_experiment,
        f"http://127.0.0.1:8080?name=tornado&delay={delay}&",
        num_iter,
    )

    start = time.time()
    result = asyncio.run(run_func())
    end = time.time()

    print(f"Result: {result}, Time: {end-start}")
