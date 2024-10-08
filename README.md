# WIP

## Unnamed game

This repository handles backend API for a single game instance.

## How to run BACKEND api locally

To run this repo you will need:

-   Python
-   Poetry (`python3 -m pip install poetry`)

After that, you can get all dependencies by running `poetry install` in the root directory.
Then you should be ready to run the repo locally (using `poetry run fastapi dev backend/main.py --host 0.0.0.0` in the root folder)

Since the core framework we are using for this api is FastAPI, you can refer to FastAPI manual for more info:
https://fastapi.tiangolo.com/

### Testing

(nothing to test yet)
Pytest is used for testing purposes, to run all tests, run `pytest` from root directory.

## How to run FRONTEND in docker

```sh
docker run --rm -p 5173:5173 --name frontend -it -v $PWD/frontend:/frontend -v $PWD/setup.sh:/setup.sh node:22 bash setup.sh
```

If you dont want to have space issues delete the neutron star called `frontend/node_modules` after.
