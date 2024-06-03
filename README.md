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

Note that the guardrail of resourcing is here and here only.

## Usage

The sandbox is a very simple HTTP server that listens to port 8000.

You POST the python code to `/execute` API entry, with the JSON payload
`{"code": "<the python code>"}` .  The python code can be multi-line.

The output is a JSON object with 3 keys: `stdout`, `stderr` and `returncode`
if the execution "ends successfully", and HTTP status code is 200.
Some examples are at`test/test_app.py` .

There's timeout of code execution (hardcoded);
then the output is instead a single-key JSON object and HTTP status code is 408.

* Installing packages via API is not supported
* Sending input via API is not supported
* Feeding files via API is not supported

The API is very naive: pass the code itself, and the API runs with `python`.