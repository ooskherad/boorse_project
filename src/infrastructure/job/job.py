import datetime
import time
from typing import Callable

from infrastructure.helper.utils import TEHRAN


class Job:
    def __init__(self, task: Callable, start: datetime.time, end: datetime.time, duration: int):
        self.start_at: datetime.time = start
        self.end_at: datetime.time = end
        self.duration: int = duration
        self.task: Callable = task

    def run(self):
        while True:
            if self.check_condition():
                try:
                    self.task()
                except Exception as e:
                    print("an error occurred", e)
                    
                time.sleep(self.duration)

    def check_condition(self) -> bool:
        now = datetime.datetime.now(TEHRAN)
        if now.time() < self.start_at:
            return False

        if self.end_at > now.time():
            return False

