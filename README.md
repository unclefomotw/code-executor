# Python Code Executor

Use docker as a sandbox to execute untrusted python code


## Installation

```bash
docker build -t python-executor .
```


## Run
```bash
docker run -d --name python-executor --memory="512m" --cpus="1" -p 8000:8000 python-executor
```
