import json
import logging
from websockets.asyncio.server import broadcast
from storage import Storage, storage, WS_CONNECTIONS
from handlers import pat_left_handler, pat_right_handler

def get_state(storage: Storage):
    return {
        "lastHeartbeatReceivedAt": storage.last_hb_received_at_ts,
        "deviceStatus": storage.is_device_online,
        "allowSignalsSending": storage.allow_signal_sending,
        "maxIntensity": storage.max_intensity 
    }

async def register(websocket):
    global storage
    WS_CONNECTIONS.add(websocket)
    # send app state
    state = get_state(storage)
    await websocket.send(json.dumps({"type": "state", "value": state}))
    try:
        async for message in websocket:
            # TODO: add validation
            logging.debug(f"[WS Handler] data received: {message}")
            event = json.loads(message)
            event_type = event["type"]
            if event_type == "allowSignalsSending":
                storage.allow_signal_sending = event["value"]
            elif event_type == "maxIntensity":
                storage.max_intensity = event["value"]
                broadcast(WS_CONNECTIONS, json.dumps({"type": "state", "value": get_state(storage)}))
            elif event_type == "testSignal":
                logging.debug('[WS Handler] test signal received')
                intensity = event["value"]
                await pat_left_handler(None, intensity)
                await pat_right_handler(None, intensity)
    finally:
        WS_CONNECTIONS.remove(websocket)

