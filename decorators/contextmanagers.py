from contextlib import contextmanager
from dataclasses import dataclass, field
import uuid
import time
from typing import Any


@dataclass
class Event:
    id_: uuid.UUID = None
    start_time: int = None
    end_time: int = None
    duration: int = None
    metadata: dict[str, Any] = field(default_factory=dict)
    # Adding getters for fields and wrapper methods maybe is better


@contextmanager
def event():
    e = Event()
    e.id_ = uuid.uuid4()
    e.start_time = time.time_ns()
    try:
        print('Starting event:', e)
        yield e
    finally:
        e.end_time = time.time_ns()
        e.duration = e.end_time - e.start_time
        print('Finished event:', e)


with event() as e:
    e.metadata['name'] = 'abc'
    e.metadata['data'] = (1, 23)
    time.sleep(1)
    raise Exception("something went wrong")
