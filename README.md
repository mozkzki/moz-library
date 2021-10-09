# moz-library

[![CircleCI](https://circleci.com/gh/mozkzki/moz-library/tree/main.svg?style=svg)](https://circleci.com/gh/mozkzki/moz-library/tree/main)
[![codecov](https://codecov.io/gh/mozkzki/moz-library/branch/main/graph/badge.svg?token=BRB5vsPkO2)](https://codecov.io/gh/mozkzki/moz-library)
[![Maintainability](https://api.codeclimate.com/v1/badges/df50bbce59225073a577/maintainability)](https://codeclimate.com/github/mozkzki/moz-library/maintainability)

図書館で借りた本, 予約した本の状況を取得する自前ライブラリ。

## Function

- search_rental (借りている本の状況確認)
- search_reserve (予約している本の状況確認)

## Usage

Environmental variables

`.env`ファイルに書いてproject rootに配置。`.env_sample`をコピーすると楽。

```txt
USER1='{"name": "foo1", "disp_name": "Foo1", "id": "11111", "password": "pass"}'
USER2='{"name": "foo2", "disp_name": "Foo2", "id": "11112", "password": "pass"}'
USER3='{"name": "foo3", "disp_name": "Foo3", "id": "11113", "password": "pass"}'
USER4='{"name": "foo4", "disp_name": "Foo4", "id": "11114", "password": "pass"}'
CHROME_BINARY_LOCATION='/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
CHROME_DRIVER_LOCATION='/usr/local/bin/chromedriver'
```

Install

```sh
pip install git+https://github.com/mozkzki/moz-library
# upgrade
pip install --upgrade git+https://github.com/mozkzki/moz-library
# uninstall
pip uninstall moz-library
```

Coding

```python
import moz_library
messages = moz_library.search_rental({
    "mode": "rental",
    "all_user": False,
    "users": ["USER1"],
    "debug": False,
    "zero_behavior": "message",
    "separate": False
})
import pprint
pprint.pprint(messages)
```

## Develop

base project: [mozkzki/moz-sample](https://github.com/mozkzki/moz-sample)

### Prepare

```sh
poetry install
poetry shell
```

### Run (Example)

```sh
python ./examples/example.py
# or
make start
```

### Unit Test

test all.

```sh
pytest
pytest -v # verbose
pytest -s # show standard output (same --capture=no)
pytest -ra # show summary (exclude passed test)
pytest -rA # show summary (include passed test)
```

with filter.

```sh
pytest -k app
pytest -k test_app.py
pytest -k my
```

specified marker.

```sh
pytest -m 'slow'
pytest -m 'not slow'
```

make coverage report.

```sh
pytest -v --capture=no --cov-config .coveragerc --cov=src --cov-report=xml --cov-report=term-missing .
# or
make ut
```

### Lint

```sh
flake8 --max-line-length=100 --ignore=E203,W503 ./src
# or
make lint
```

### Create API Document (Sphinx)

```sh
make doc
```

### Update dependency modules

dependabot (GitHub公式) がプルリクを挙げてくるので確認してマージする。

- 最低でもCircleCIが通っているかは確認
- CircleCIでは、最新の依存モジュールでtestするため`poetry update`してからtestしている
- dependabotは`pyproject.toml`と`poetry.lock`を更新してくれる
