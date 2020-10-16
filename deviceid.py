#!/usr/bin/env python3
import os

device=input("hallo give me your \nparallel space device id : ")

ff='{\\"device_id\\": \\"'+device+'\\", \\"device_id_sig\\": \\"AaauX/ZA2gM3ozqk1U5j6ek89SMu\\", \\"user_agent\\": \\"Dalvik/2.1.0 (Linux; U; Android 7.1; LG-UK495 Build/MRA58K; com.narvii.amino.master/3.3.33180)\\"}'
os.system("printf \""+ff+"\">device.json")
os._exit(1)
