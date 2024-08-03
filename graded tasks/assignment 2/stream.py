import threading
from queue import Queue
from typing import Callable, Any

class Stream:
    def __init__(self):
        self.queue = Queue()
        self.action = None
        self.next_stream = None
        self.running = True
        self.thread = threading.Thread(target=self._process)
        self.thread.start()

    def _process(self):
        while self.running:
            if not self.queue.empty() and self.action:
                item = self.queue.get()
                result = self.action(item)
                if self.next_stream:
                    if isinstance(result, bool):
                        if result:
                            self.next_stream.add(item)
                    else:
                        self.next_stream.add(result)
            else:
                threading.Event().wait(0.1)

    def add(self, item: Any):
        self.queue.put(item)

    def forEach(self, func: Callable[[Any], None]):
        self.action = func

    def apply(self, func: Callable[[Any], Any]) -> 'Stream':
        self.next_stream = Stream()
        self.action = func
        return self.next_stream

    def stop(self):
        self.running = False
        if self.next_stream:
            self.next_stream.stop()
        self.thread.join()