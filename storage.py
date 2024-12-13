import time

class Signal():
    def __init__(self, value: float):
        self.received_at_ts = time.time()
        self.sent_at_ts = 0.0
        self.value = value
    received_at_ts: float = 0.0
    sent_at_ts: float = 0.0
    value: float = 0.0

class Storage():
    # can take values from 0.0 to 1.00
    lvalue: float = 0.0
    rvalue: float = 0.0
    lsignal: Signal = None
    rsignal: Signal = None
    last_sent_at_ts: float = 0
    allow_signal_sending: bool = True
    max_intensity: float = 1.0
    last_hb_received_at_ts: float = 0.0
    is_device_online: bool = False

storage = Storage()

WS_CONNECTIONS = set()
