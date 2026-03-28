Analysis - I/O Bound
Single-Threaded: Takes the longest time since URLs are downloaded one after another.

Multithreading: Faster than single-threaded due to concurrent downloads, but limited by thread overhead and the Global Interpreter Lock (GIL).

Asyncio: Fastest among all methods for IO-bound tasks, efficiently handling many concurrent connections with low overhead.

Multiprocessing: Faster than single-threaded but slower than multithreading and asyncio for IO-bound tasks due to the overhead of inter-process communication.

Key Takeaways:

Asyncio excels in IO-bound tasks, providing the best performance with minimal overhead.

Multithreading improves performance over single-threaded execution but is less efficient than asyncio.

Multiprocessing is not ideal for IO-bound tasks due to higher overhead and does not provide significant performance gains.



Analysis - CPU Bound
Single-Threaded: Baseline performance.
Multithreading: May not improve performance and can even be slower due to the Global Interpreter Lock (GIL).
Asyncio: Not suitable for CPU-bound tasks; may not provide any performance benefit.
Multiprocessing: Shows a substantial decrease in execution time by utilizing multiple CPU cores.
Key Takeaways:

Multiprocessing is effective for CPU-bound tasks, allowing true parallelism.
Multithreading is not effective for CPU-bound tasks in Python due to the GIL.
Asyncio is not designed for CPU-bound tasks and should be avoided in this context.