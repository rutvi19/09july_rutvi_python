import requests as r

class wifi:
    def __init__(self):
        a=r.system("google.com")
        if a==0:
            print("connected")
        else:
            print("not connected")

w=wifi()            