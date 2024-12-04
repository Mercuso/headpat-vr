class Storage():
    # can take values from 0.0 to 1.00
    lvalue: float = 0.0
    rvalue: float = 0.0
    last_sent_at_ts: float = 0
    allow_signal_sending: bool = True
    max_intensity: float = 1.0
    last_hb_received_at_ts: float = 0.0
    is_device_online: bool = False

storage = Storage()

WS_CONNECTIONS = set()
