import requests
import os


# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    test = "Test"
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://google.es")
print(r.status_code)
