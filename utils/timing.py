import time


class PerformanceTest:
    def __init__(self, runs: int = 1e7):
        self.runs = int(runs)

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()

            for _ in range(self.runs):
                result = func(*args, **kwargs)

            end_time = time.time()
            elapsed_time = end_time - start_time
            average_time = elapsed_time / self.runs
            print(f"Function {func.__name__} took an average of {average_time:.10f} seconds for {self.runs} runs.")
            return result

        return wrapper
