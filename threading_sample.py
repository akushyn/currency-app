import concurrent
import threading
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor


def task(x):
    time.sleep(3)
    result = x * x
    # print(f"Execute task: {result}")
    return result


class ThreadService:
    def instance_task(self):
        time.sleep(1)
        print(f"Execute instance task")

    @classmethod
    def class_method(cls):
        time.sleep(1)
        print(f"Execute class method")

    @staticmethod
    def static_function():
        time.sleep(1)
        print(f"Execute static method")


if __name__ == '__main__':
    # for i in range(5):
    #     thread = threading.Thread(target=task, args=(i, ))
    #     thread.start()

    service = ThreadService()
    t = threading.Thread(target=ThreadService.static_function)
    t.start()

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(task, x=i) for i in range(10)]

        for future in concurrent.futures.as_completed(futures):
            print(future.result())
