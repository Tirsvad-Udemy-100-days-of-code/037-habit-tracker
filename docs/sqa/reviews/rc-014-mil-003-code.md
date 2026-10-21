# RC-014: MIL-003 code review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [MIL-003], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-22 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [e6fef2e] |

---

## Artifact Under Review

- Instance reviewed: [MIL-003]
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review of the Python code delivered by MIL-003: graph domain types, create_graph use case, create-graph command and their tests; written by the python-developer agent and verified by the AI author
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Packages and modules are snake_case, classes PascalCase (`Username`, `RequestsPixelaGateway`), constants UPPER_SNAKE. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`create_user`, `load_credentials`, `DryRunPixelaGateway`); no abbreviation, no single-letter name outside a comprehension. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check .` and `ruff format --check .` (ruff 0.6.9) are clean. The two `noqa` comments of the local test server carry their reason; the one `type: ignore[misc]` in the graph domain test is explained in place (a frozen field is written on purpose). |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function and method is annotated, including `-> None`; `mypy --strict` passes. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare `except`; `RequestException` is caught and re-raised as `GatewayError ... from error`; a non-JSON body is handled by catching `ValueError` only. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable default and no shadowed builtin (the `format` parameter in the test server is fixed by the base class and marked). |
| 7 | Files, locks and connections are managed with context managers | Pass | `RequestsPixelaGateway` opens a `requests.Session` with `with` when none is injected; the test server is started and stopped in a context manager. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every new module, class and function has a Doxygen docstring; `doxygen Doxyfile` prints no warning. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` and no logging. The token is only in the `X-USER-TOKEN` header; tests assert that it is absent from the path, the body and the dry-run output. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No Design Class Diagram exists (ADR-0002). The classes follow the layers named in the milestone tasks 1 to 6; there is no unexplained class. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 149 tests in `unit`, `integration` and `e2e`; coverage of `src` is 99 %; the graph tests check path, body, header, the six colours, invalid input and that nothing is sent on invalid input; only fake credentials and 127.0.0.1 are used. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` passes with and without the dev dependencies; `Any` stays limited to the cases named in the MIL-002 review. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Dependencies are unchanged from MIL-002; nothing declared is unused. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The graph id pattern is `GRAPH_ID_PATTERN` in `constants.py`; the path is built once in `graphs_path`; the colours and types are enums defined once. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `domain` imports only `constants`; `application` imports `domain`; `infrastructure` imports `application` and `domain`; only `presentation/cli.py` imports `infrastructure`. No cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One reason to change per module; `CreateGraphCommand` was added to `COMMANDS` without editing the other commands; the use case depends on the `PixelaGateway` Protocol. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Layers are `domain`, `application`, `infrastructure`, `presentation` under `src/habit_tracker/`, and `unit`, `integration`, `e2e` under `tests/`; imports point inward. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All names are English, lower case with `_`, no space. |

## Overall Verdict

Go — All Mandatory criteria of QC-PY-001 pass.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None. Every criterion passes. | S01 | - |

---

[MIL-003]: ../../milestones/mil-003-create-graph.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[e6fef2e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/commit/e6fef2e5bd8da31689a5b2c006a46d1f80b9c5b7
