import time
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import asyncio
import aiohttp
from tqdm import tqdm

# I/O bound tasks

def download_content(url: str) -> bool:
    """Blocking version of download_content, get response, then return."""
    try:
        _ = requests.get(url)
        return True
    except Exception:
        return False
async def adownload_content(session, url: str) -> bool:
    """Non-blocking version of download_content, return while waiting for response."""
    try:
        async with session.get(url) as response:
            _ = await response.read()
            return True
    except Exception:
        return False
def generate_urls(base_url: str, count: int) -> list:
    """Generate a list of URLs for testing."""
    return [f"{base_url}/delay/1" for _ in range(count)]


def run_single_threaded(urls: list) -> None:
    """Single-threaded version of download_content."""
    count = 0
    print("---- Starting single-threaded download ----")
    start_time = time.time()
    for url in tqdm(urls, desc="Single-threaded"):
        if download_content(url):
            count += 1
    time_diff = time.time() - start_time
    print(f"Single-threaded: {count} requests done in {time_diff:.2f} seconds")


def run_multithreaded(urls: list, max_workers: int = 8) -> None:
    """Multithreaded version of download_content."""
    print("---- Starting multithreaded download ----")
    start_time = time.time()
    count = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(download_content, url): url for url in urls}
        for future in tqdm(as_completed(futures), desc="Multithreading", total=len(urls)):
            if future.result():
                count += 1
    time_diff = time.time() - start_time
    print(f"Multithreaded: {count} requests done in {time_diff:.2f} seconds")


async def run_asyncio(urls: list) -> None:
    """Asyncio version of download_content."""
    print("---- Starting asyncio download ----")
    start_time = time.time()
    count = 0
    async with aiohttp.ClientSession() as session:
        tasks = [adownload_content(session, url) for url in urls]
        for result in tqdm(asyncio.as_completed(tasks), desc="Asyncio", total=len(urls)):
            if await result:
                count += 1
    time_diff = time.time() - start_time
    print(f"Asyncio: {count} requests done in {time_diff:.2f} seconds")

def run_multiprocessing(urls: list, max_workers: int = 8) -> None:
    """Multiprocessing version of download_content."""
    print("---- Starting multiprocessing download ----")
    start_time = time.time()
    count = 0
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(download_content, url): url for url in urls}
        for future in tqdm(as_completed(futures), desc="Multiprocessing", total=len(urls)):
            if future.result():
                count += 1
    time_diff = time.time() - start_time
    print(f"Multiprocessing: {count} requests done in {time_diff:.2f} seconds")


# if __name__ == "__main__":
#     base_url = "https://httpbin.org"
#     num_requests = 64  # Number of requests for testing
#     urls = generate_urls(base_url, num_requests)
#     run_single_threaded(urls)
#     run_multithreaded(urls, max_workers=8)
#     asyncio.run(run_asyncio(urls))
#     run_multiprocessing(urls, max_workers=8)


# CPU bound tasks

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import asyncio
from tqdm import tqdm
def pure_python_task(task_id):
    result = 0
    for i in range(1000000):
        result += i * i * (i % 7) + (i % 11) * (i % 13)
    return result
async def async_pure_python_task(task_id):
    result = 0
    for i in range(1000000):
        result += i * i * (i % 7) + (i % 11) * (i % 13)


def run_single_threaded(task_ids):
    start = time.time()
    [pure_python_task(task_id) for task_id in task_ids]
    end = time.time()
    print(f"Single-threaded: {len(task_ids)} tasks in {end-start:.2f}s")
    return end - start


def run_thread_pool(task_ids, max_workers=8):
    start = time.time()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        list(executor.map(pure_python_task, task_ids))
    end = time.time()
    print(f"ThreadPoolExecutor: {len(task_ids)} tasks in {end-start:.2f}s")
    return end - start

async def run_asyncio(task_ids):
    start = time.time()
    await asyncio.gather(*(async_pure_python_task(task_id) for task_id in task_ids))
    end = time.time()
    print(f"Asyncio: {len(task_ids)} tasks in {end-start:.2f}s")
    return end - start

def run_process_pool(task_ids, max_workers=4):
    start = time.time()
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        list(executor.map(pure_python_task, task_ids))
    end = time.time()
    print(f"ProcessPoolExecutor: {len(task_ids)} tasks in {end-start:.2f}s")
    return end - start

def run_benchmark():
    print("=== CPU-Bound Concurrency Benchmark ===")
    task_ids = list(range(100))
    t_single = run_single_threaded(task_ids)
    t_thread = run_thread_pool(task_ids, max_workers=8)
    t_process = run_process_pool(task_ids, max_workers=4)
    t_async = asyncio.run(run_asyncio(task_ids))
    print("\n=== Summary ===")
    print(f"Single-threaded:    {t_single:.2f}s")
    print(f"ThreadPoolExecutor: {t_thread:.2f}s")
    print(f"ProcessPoolExecutor:{t_process:.2f}s")
    print(f"Asyncio:            {t_async:.2f}s")

if __name__ == "__main__":
    run_benchmark()