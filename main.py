from discordrp import Presence
import time

client_id = ""  

with Presence(client_id) as presence:
    print("Connected")
    presence.set(
        {
            "details": "",
            "state": "Chapter 3rd",
            "timestamps": {"start": int(time.time())},
        
        }
    )
    print("Presence updated")

    while True:
        time.sleep(15)