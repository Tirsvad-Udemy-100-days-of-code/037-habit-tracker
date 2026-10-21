# RC-013: MIL-002 code review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-22 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [725e63f] |

---

## Artifact Under Review

- Instance reviewed: [MIL-002]
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review of the Python code delivered by MIL-002: the domain, application, infrastructure and presentation modules for create user, and the unit, integration and e2e tests; the tests were written by the python-developer agent, the source by the AI author and then checked by the agent
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Packages and modules are snake_case, classes PascalCase (`Username`, `RequestsPixelaGateway`), constants UPPER_SNAKE. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`create_user`, `load_credentials`, `DryRunPixelaGateway`); no abbreviation, no single-letter name outside a comprehension. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check .` and `ruff format --check .` (ruff 0.6.9) are clean. Two `noqa` comments in the local test server carry their reason (the method name `do_POST` and the parameter `format` are fixed by `http.server`). |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function and method is annotated, including `-> None`; `mypy --strict` passes. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare `except`; `RequestException` is caught and re-raised as `GatewayError ... from error`; a non-JSON body is handled by catching `ValueError` only. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable default and no shadowed builtin (the `format` parameter in the test server is fixed by the base class and marked). |
| 7 | Files, locks and connections are managed with context managers | Pass | `RequestsPixelaGateway` opens a `requests.Session` with `with` when none is injected; the test server is started and stopped in a context manager. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every module, class and public function has a Doxygen docstring with `@brief`, `@param`, `@return`, `@throws` where they apply; `doxygen Doxyfile` prints no warning. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` and no logging; the CLI writes to the stream it is given. The token is hidden in `str`, `repr`, the dry run and error messages, and the e2e tests assert that it never appears in the output. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No Design Class Diagram exists (ADR-0002). The classes follow the layers named in the milestone tasks 1 to 6; there is no unexplained class. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 103 tests named for behaviour, in `unit`, `integration` and `e2e`; coverage of `src` is 99 %; they use only fake credentials and 127.0.0.1, so they do not need the network and do not depend on order. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` passes with dev dependencies and in a venv without them; `Any` appears only for YAML values in the workflow test and for the `*args` of the fixed `log_message` signature, each with a reason. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `requests` is imported by the infrastructure adapter and declared in `pyproject.toml`; development tools are pinned; nothing declared is unused. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | URL joining is in `urls.py`, the paths in `endpoints.py`, constants in `constants.py`, the secret mask in `HIDDEN_TOKEN`; each is defined once. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `domain` imports only `constants`; `application` imports `domain`; `infrastructure` imports `application` and `domain`; only `presentation/cli.py` imports `infrastructure`. No cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One reason to change per module; commands are added to `COMMANDS` without editing others (open for extension); `PixelaGateway` is a narrow Protocol that both gateways satisfy and the use case receives. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Layers are `domain`, `application`, `infrastructure`, `presentation` under `src/habit_tracker/`, and `unit`, `integration`, `e2e` under `tests/`; imports point inward. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All names are English, lower case with `_`, no space. |

## Overall Verdict

Go — All Mandatory criteria of QC-PY-001 pass.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None. Every criterion passes. | S01 | - |

---

[MIL-002]: ../../milestones/mil-002-create-user.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[725e63f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/commit/725e63fa8a55c1c4987b1ade4f9480f0602afd27
