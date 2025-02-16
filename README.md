# Coder

## Installation

To install the package, run the following command:

```bash
uv sync --all-extras --all-groups
```

## Setup

To setup the package, create a `.env` file in `~/cred/coder/.env` with the following content:

```bash
CODER_SAMPLE_ENV_VAR=sample
```

And for VSCode to recognize the environment file, add the following line to the
workspace [settings file](.vscode/settings.json):

```json
"python.envFile": "/home/pmn/cred/coder/.env"
```

Note that the path to the `.env` file should be absolute.

## Testing

To run the tests, use the following command:

```bash
# poetry run pytest # ??? uv
```

or use the VSCode interface.

## IDEAs
