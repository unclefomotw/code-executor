import requests


def test_sending_normal_code():
    code = """\
def f():
  sum = 0
  for i in range(10):
    sum += i
  return sum


print(f())
"""

    r = requests.post("http://127.0.0.1:8000/execute",
                      json={"code": code})
    print(r.json())
    print(r.status_code)


def test_sending_wrong_code():
    code = """\
def f():
  sum = 0
  for i in range(10):
    sum += 100/(9-i)
  return sum


print(f())
"""

    r = requests.post("http://127.0.0.1:8000/execute",
                      json={"code": code})
    print(r.json())
    print(r.status_code)


def test_sending_dangerous_code():
    code = """\
import os

os.mkdir("abcde")
"""

    r = requests.post("http://127.0.0.1:8000/execute",
                      json={"code": code})
    print(r.json())
    print(r.status_code)


def test_sending_while_loop_code():
    code = """\
sum = 0
while True:
    sum += 1
"""

    r = requests.post("http://127.0.0.1:8000/execute",
                      json={"code": code})
    print(r.json())
    print(r.status_code)


test_sending_normal_code()
test_sending_wrong_code()
test_sending_dangerous_code()
test_sending_while_loop_code()
