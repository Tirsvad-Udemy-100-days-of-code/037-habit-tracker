# 🚀 Habit Tracker

A small Python project that tracks a habit with the [Pixela][pixela-docs] HTTP API. It is the Pixela assignment of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp", written for course participants who want readable, runnable code and for visitors who want an idea.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The project follows the three lecture steps of the assignment, each a POST request to Pixela:

1. create a user (`create_user`),
2. create a graph, sending the token in the `X-USER-TOKEN` header (`create_graph`),
3. post a pixel with a `YYYYMMDD` date and a quantity string (`post_pixel`).

| Part | What it is for |
| --- | --- |
| `src/habit_tracker/` | The package. `constants.py` holds every constant; the layers `domain`, `application`, `infrastructure` and `presentation` follow Clean Architecture |
| `tests/` | The pytest tests (`unit`, `integration`, `e2e`); none of them reaches an external host |
| `docs/` | The plan, the reviews, the screenshots (`docs/images/`) and the wiki sources (`docs/wiki/`, in English, Danish and Bahasa Malaysia) |
| `pyproject.toml` | Project configuration: dependencies, pytest, ruff, mypy |
| `Doxyfile` | Configuration of the Doxygen source documentation |

The username and the token are never in the source. They are read from the process environment (`PIXELA_USERNAME` and `PIXELA_TOKEN`); the project does not read a `.env` file.

## 📋 Requirements

- Python 3.13 or later, to run the code and the tests.
- `requests`, the one runtime dependency, because the assignment teaches the `requests` module (decision [ADR-0001][ADR-0001]). It is installed with the project.
- `pytest`, `pytest-cov`, `ruff`, `mypy` and `types-requests` for development; they are installed with the `dev` extra.
- [Doxygen][doxygen] 1.9 or later, only if you want to build the source documentation.

## 🛠️ Setup

Create and use a local virtual environment named `.venv`, then upgrade `pip` and install the project with its development tools.

On Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Leave the environment with `deactivate`. The folder `.venv` is ignored by git.

Choose your own Pixela username and token, and put them in the environment of your shell (never in a file you commit):

```bash
export PIXELA_USERNAME="your-username"
export PIXELA_TOKEN="your-secret-token"
```

In PowerShell use `$env:PIXELA_USERNAME = "your-username"` and `$env:PIXELA_TOKEN = "your-secret-token"`. The token is a secret of 8 to 128 characters that you choose; Pixela does not generate it.

## ▶️ Run

Every command reads `PIXELA_USERNAME` and `PIXELA_TOKEN` from the environment. Add `--dry-run` before the command name to print the request, with the token hidden, and send nothing. Remove it to send the request to Pixela.

| Step of the assignment | Command | Python function |
| --- | --- | --- |
| 1. Create the user | `python -m habit_tracker create-user --agree-terms --not-minor` | `create_user` |
| 2. Create a graph | `python -m habit_tracker create-graph --id cycling --name "Cycling Graph" --unit Km --type float --color ajisai` | `create_graph` |
| 3. Post a pixel | `python -m habit_tracker post-pixel --graph-id cycling --date 2026-10-22 --quantity 9.74` | `post_pixel` |

The colours are the Pixela names `shibafu`, `momiji`, `sora`, `ichou`, `ajisai` and `kuro`. The date is `YYYY-MM-DD` or `YYYYMMDD`; Pixela receives `YYYYMMDD`. A taken username makes `create-user` print `Rejected (409)` and exit with code 1.

The installed program is also available as `habit-tracker`, for example `habit-tracker --dry-run create-user --agree-terms --not-minor`.

The functions can be used from Python as well:

```python
from habit_tracker import create_graph, create_user, post_pixel
```

Each takes a gateway (`RequestsPixelaGateway` or `DryRunPixelaGateway`), the credentials and the data of the step; the [wiki][wiki] shows an example.

![Create user in dry-run mode][shot-user]

![Create graph in dry-run mode][shot-graph]

![Post pixel in dry-run mode][shot-pixel]

## 🧪 Tests

With the virtual environment active:

```bash
python -m pytest
```

Add `--cov` for the coverage report. The quality checks that the pull requests run are:

```bash
python -m ruff check .
python -m ruff format --check .
python -m mypy --strict src tests
```

Build the source documentation with `doxygen Doxyfile`; the result is in `doxygen/html/index.html`.

![The test run][shot-tests]

## 📄 License

GNU Affero General Public License, version 3. See [LICENSE][license].

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]
- [Pixela API documentation][pixela-docs]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Decisions][adr] | Why `requests` is used and why there are no use cases |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

### CI secrets

The workflows in `.gitea/workflows/` call the shared workflows of `TirSystem/github-action`. The quality checks and the English comments check need no secret. The wiki publishing (`publish-wiki.yml`) needs the secret `TOKEN_FOR_GITEA_WIKI` in the organisation of the repository: a Gitea token with the scope `write:repository` for a user who can write this repository. Enable the wiki in the repository settings.

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/issues
[pixela-docs]: https://docs.pixe.la/
[doxygen]: https://www.doxygen.nl/
[wiki]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/wiki
[shot-user]: ./docs/images/create-user-dry-run.png
[shot-graph]: ./docs/images/create-graph-dry-run.png
[shot-pixel]: ./docs/images/post-pixel-dry-run.png
[shot-tests]: ./docs/images/tests.png
[license]: ./LICENSE
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[adr]: ./docs/adr/
[ADR-0001]: ./docs/adr/adr-0001-requests-as-runtime-dependency.md
[registry]: ./docs/artifact-registry.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
