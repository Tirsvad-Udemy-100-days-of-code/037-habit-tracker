# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-22 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [08a6fcc] |
| 2026-10-22 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Spelled out abbreviations on first use (QC-LANG-001 criterion 10) | [7f06a77] |

---

## Executive Summary

The Habit Tracker is a small Python project built as the Pixela assignment of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp". It calls the Pixela HTTP (Hypertext Transfer Protocol) API (application programming interface) with POST requests to create a user, create a graph and post a pixel, and so tracks a habit. The project gives course participants readable, runnable code with the assignment's function names, and gives visitors to the GitHub repository a clear example with a good description, topics and README. We recommend building it as a repository with a plan, tests, source documentation and a three-language wiki.

## Methodological and Standards Foundation

The project follows the SQA (software quality assurance) and QC (quality control) framework mounted at `framework/`: a Business Case, a Stakeholder Analysis, a Project Plan and milestones come before code, and every step is reviewed against a QC checklist. Quality is judged against ISO/IEC (International Organization for Standardization and International Electrotechnical Commission) 25010:2023. The code follows Clean Architecture (Domain, Application, Infrastructure, Presentation) and the Python conventions of the `coding-conventions` skill (PEP 8 (Python Enhancement Proposal), PEP 257, PEP 484, `ruff`, `mypy --strict`).

## Problem Statement

The lectures of the assignment show the code only on screen, step by step, in an editor. The result is a loose script that holds the username and the token in plain text, with no tests, no instructions to run it and no documentation. A participant who wants to compare solutions, and a visitor who wants an idea, find little they can run and read at once.

## Business Opportunity

A tidy repository turns the lecture code into a reference that others can run in minutes. It also shows a way to keep secrets out of the code, to test HTTP calls without the network and to document a small project in three languages.

## Objectives

1. Provide `create_user`, `create_graph` and `post_pixel`, the functions of the assignment, each calling the Pixela API as the lecture does.
2. Keep the username and the token out of the source: they are read from the process environment.
3. Verify the behaviour with automated pytest tests that never use the network.
4. Document how to create and use a local `.venv` and how to run the project and its tests.
5. Document the source with Doxygen comments and provide a `Doxyfile`.
6. Publish a README and a wiki in English, Danish and Bahasa Malaysia with screenshots.
7. Describe the repository on the git host with a description and topics, and run the shared quality workflows of `TirSystem/github-action`.

## Scope

### In Scope

- Python 3.13 or later, a local `.venv`, `pyproject.toml`, a Python `.gitignore` and pytest.
- The three lecture steps: create a Pixela user (POST), create a graph (POST with the token in the `X-USER-TOKEN` header), post a pixel (POST with a `YYYYMMDD` date and a quantity string).
- A command line to run each step, with a dry run that prints the request and sends nothing.
- A `constants.py` for constants, Doxygen comments in the source and a `Doxyfile`.
- The README from the framework template, a wiki in English, Danish and Bahasa Malaysia, and screenshots for both.
- The shared workflows from `TirSystem/github-action` that suit a Python project, the repository description and topics, one pull request per milestone.

### Out of Scope

- Updating (PUT) and deleting (DELETE) pixels or graphs, which the lectures only mention.
- Automatic entry of today's date with `datetime` (the next lesson hints at it; the date is an argument here).
- Reading a `.env` file in the project: the file is personal to the author and is not imported, tested or committed.
- Graphical user interface, a database, packaging for PyPI and any other habit service than Pixela.
- Tests against the live Pixela service.

## Expected Benefits

### Tangible Benefits

- A runnable project that a participant starts with a few commands from the README.
- A passing pytest suite that runs offline.
- Generated API documentation (Doxygen) and a wiki in three languages.

### Intangible Benefits

- A clear example of secret handling and of layered code for beginners.
- A reference that participants can compare with their own solutions.
- A tidy portfolio repository for the author.

## Strategic Alignment

The project supports the author's goal of finishing the 100 Days of Code course with work that is reviewable and reusable, and the goal of the TirSystem repositories to follow one framework with shared automation.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | The assignment's functions exist | `create_user`, `create_graph` and `post_pixel` are importable | A pytest test imports each function |
| 2 | Tests pass offline | 100 % of tests pass, 0 requests to an external host | `python -m pytest` on a machine without internet access |
| 3 | Code is covered by tests | At least 90 % line coverage of `src/` | `pytest --cov` report |
| 4 | A newcomer can run the project | README steps work on a clean clone without changes | Follow the README on a fresh `.venv` |
| 5 | Wiki is complete | 3 languages, the same page set | File list of `docs/wiki/` |
| 6 | Lint and types are clean | 0 `ruff` findings, 0 `mypy --strict` errors | The quality workflow or the local commands |
| 7 | Repository is described | Description and at least 5 topics set | Gitea repository settings |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The author's token or password reaches the repository | A secret is public | `.env` is ignored by git, the project never reads it, credentials are read from the process environment and tests use fake values |
| The Pixela API changes | Examples stop working | Constants hold the endpoints, tests use a fake HTTP session, the wiki names the API documentation |
| The username in the examples is already taken on Pixela | A participant sees a 409 error | README tells the participant to choose their own username and shows the error case |
| Translations drift from English | Readers in Danish or Bahasa Malaysia get old text | Same page set in each language, English is authoritative, wiki pages are reviewed with the change |
| The shared workflows need secrets and a runner that the repository may not have | Continuous integration (CI) stays red or does not run | The workflows are installed from the shared repository and the needed secrets are listed in the README |
| `requests` is a runtime dependency although S03 asked for none | A viewer has to install one package | ADR-0001 (Architecture Decision Record) records the decision, the README names the one package and why |

## Assumptions

- The author, S01, is Product Owner, developer and reviewer, and AI stands in for reviewers in autonomous mode.
- The repository `Tirsvad-Udemy-100-days-of-code/037-habit-tracker` on git.tirsystem.com is the repository of the project and the push target.
- The Pixela API is reachable and stays compatible with the lectures.
- A runner is registered for the repository, or the workflows simply wait until one is.

## Constraints

- Python 3.13 or later and a `venv`; `pytest` for tests.
- The folders `src/`, `tests/` and `docs/`.
- `constants.py` holds the constants; Doxygen comments in the source; a `Doxyfile`.
- One runtime dependency at most, and only when needed (`requests`, ADR-0001).
- One branch and one pull request per milestone, so the steps stay traceable.
- Tokens come from the personal `.env`, which is not imported, not tested and not committed.

## Cost–Benefit Assessment

The assessment is qualitative: the project is a learning exercise with no revenue, and a money figure would not support the decision. The cost is the author's time and the benefit is shared knowledge.

| Costs | Benefits |
| --- | --- |
| About two days of the author's time, including reviews | A reviewed, reusable reference project |
| One runtime dependency (`requests`) | The same API the lectures teach |
| Maintenance of three wiki languages | A wider audience for participants who read Danish or Bahasa Malaysia |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Finishes the assignment with reviewable, reusable work |
| S02 | Gets readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | Gets a clear repository description, topics and a README, and no extra setup |

## Recommendation

Proceed — the scope is small, the risks are mitigated and the result is useful to all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
[08a6fcc]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/commit/08a6fcc2c14667fa77bf15d126c00b34200252b5
[7f06a77]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/commit/7f06a776d218cf5d350b0a4f53708e9ff336e034
