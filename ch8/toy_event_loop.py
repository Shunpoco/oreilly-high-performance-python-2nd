from queue import Queue
from functools import partial

class EventLoop(Queue):
    def start(self):
        while True:
            function = self.get()
            function()

eventloop: EventLoop = None

def do_hello():
    global eventloop
    print("Hello")
    eventloop.put(do_world)

def do_world():
    global eventloop
    print("world")
    eventloop.put(do_hello)


if __name__ == "__main__":
    eventloop = EventLoop()
    eventloop.put(do_hello)
    eventloop.start()
