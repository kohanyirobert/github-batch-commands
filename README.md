# About

Script environment to run batch commands against GitHub repo (e.g. enable/disable vulnerability alerts).

# Usage

* Install `pipenv`, e.g `pip install pipenv`.
* Copy `.env.sample` to `.env` and provide a [personal GitHub access token](https://github.com/settings/tokens) with [`:repo` scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/#available-scopes).
* Edit `main.py` to your liking.
* Enter the virtual environment created by `pipenv` with `pipenv shell`.
* Run `python main.py`.
