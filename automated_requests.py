import requests

for i in range(10000):
    r = requests.get("http://loady-1134132452.eu-central-1.elb.amazonaws.com:80/cpu")
    print("{}: {}".format(i, r.json()))
