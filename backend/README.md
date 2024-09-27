# WIP
## Unnamed game

This repository handles backend API for a single game instance.

## How to run repository locally

To run this repo you will need:
* Python
* Poetry (`python3 -m pip install poetry`)

After that, you can get all dependencies by running `poetry install` in the root directory.
Then you should be ready to run the repo locally (using `fastapi dev main.py` in the root folder)

Since the core framework we are using for this api is FastAPI, you can refer to FastAPI manual for more info:
https://fastapi.tiangolo.com/

### Testing

Pytest is used for testing purposes, to run all tests, run `pytest` from root directory.