**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

## Requirements

- Python 3.13 or later.
- `requests` (installed with the project).
- Optional: [Doxygen](https://www.doxygen.nl/) to build the source documentation.

## Create and use a local .venv

Clone the repository, then create the virtual environment in its root, upgrade `pip` and install the project with its development tools.

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Leave the environment with `deactivate`. The folder `.venv` is ignored by git.

## Choose your username and token

Pick your own Pixela username (a lower case letter first, 2 to 33 lower case letters, digits or hyphens) and a secret token (8 to 128 printable characters without a space). Pixela does not generate the token; you choose it. Set both in your shell:

```bash
export PIXELA_USERNAME="your-username"
export PIXELA_TOKEN="your-secret-token"
```

PowerShell:

```powershell
$env:PIXELA_USERNAME = "your-username"
$env:PIXELA_TOKEN = "your-secret-token"
```

## First run

Try the dry run first. It sends nothing:

```bash
python -m habit_tracker --dry-run create-user --agree-terms --not-minor
```

If the output shows `POST https://pixe.la/v1/users` and a hidden token (`********`), everything is in place. Continue with [Usage](Usage).

![Create user in dry-run mode](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/raw/branch/main/docs/images/create-user-dry-run.png)
