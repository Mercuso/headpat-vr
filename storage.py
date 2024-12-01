class Storage():
    # can take values from 0.0 to 1.00
    lvalue: float = 0.0
    rvalue: float = 0.0
    last_sent_at_ts: float = 0
    allow_signal_sending = True
    max_intensity = 1.0

storage = Storage()

WS_CONNECTIONS = set()
