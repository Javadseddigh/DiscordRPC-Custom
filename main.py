from pypresence import Presence
import time

CLIENT_ID = "" 

rpc = Presence(CLIENT_ID)
rpc.connect()


rpc.update(
    state="Grabber",
    details="",
    large_image="big_image",  
    small_image="small_icon",  
    large_text="By JavaD", 
    small_text="DeAd_Launcher"  
)

print("Run Shod !")
while True:
    time.sleep(15) 