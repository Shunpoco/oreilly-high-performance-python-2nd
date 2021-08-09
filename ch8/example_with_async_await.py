from functools import partial
from some_async_databse_library import save_results_to_db

from toy_event_loop import EventLoop

eventloop: EventLoop = None

async def save_value(value):
    print(f"Saving {value} to database")
    db_response = await save_results_to_db(value)
    print(f"Response from database: {db_response}")

if __name__ == "__main__":
    eventloop.put(
        partial(save_value, "Hello world", print),
    )
