# MIL-002: Create user

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-22 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

This gate decides whether the first lecture step, creating a Pixela user with a POST request, works and whether the layers that every later step reuses (domain rules, the gateway port, the HTTP adapter, the command line) are sound.

## Deliverable

A `create_user` function and a `create-user` command that send the Pixela user request, with the domain rules for the username and the token, the `PixelaGateway` port, the `requests` adapter, a dry-run adapter, and unit, integration and end-to-end tests.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `from habit_tracker import create_user` works | Imports | ImportError |
| 2 | A test shows that `create_user` sends a POST to `https://pixe.la/v1/users` with token, username, `agreeTermsOfService` and `notMinor` in the JSON body | Pass | Fail |
| 3 | A test shows that an invalid username or token is rejected before any request is sent | Pass | Fail |
| 4 | A test shows that a response with status 409 (name already taken) is returned as a failed result, not raised | Pass | Fail |
| 5 | `python -m habit_tracker --dry-run create-user ...` prints the request with the token hidden and sends nothing | Token hidden | Token printed |
| 6 | The integration test sends a real HTTP request to a local test server only | Local only | Any external host |
| 7 | `ruff`, `mypy --strict` and `pytest` are clean, and the code review against `QC-PY-001` is a Go | Clean and Go | Any finding or No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | The project configuration, `constants.py` and the test setup must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1 (the assignment's functions) | [BC-001] |
| Objective 2 (credentials not in the source) | [BC-001] |
| Objective 3 (offline tests) | Success criteria 1, 2 and 3 of [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-24 — within the two-day effort of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add domain value objects and errors | Add `Username`, `Token` and `Credentials` value objects in `domain/` that enforce the Pixela rules (username 2 to 33 characters starting with a lower case letter, token 8 to 128 characters without spaces) and an `InvalidInputError`, so bad input is stopped before a request. | No | ADR-0002 |
| 2 | Add PixelaGateway port and response DTO | Define in `application/ports/` the narrow `PixelaGateway` protocol (send one JSON POST with headers) and in `application/dto/` the `ApiResponse` that holds the status code and the Pixela message, so use cases do not depend on `requests`. | No | ADR-0002 |
| 3 | Implement create_user use case | Add `create_user(gateway, credentials, agree_terms, not_minor)` in `application/use_cases/` that builds the body of the lecture and returns the `ApiResponse`; this is the first assignment function. | No | ADR-0002 |
| 4 | Add requests gateway and dry-run gateway | Implement `PixelaGateway` with `requests` in `infrastructure/http/` (with a timeout and no exception for a 4xx answer) and a dry-run gateway that prints the request with the token hidden. | No | ADR-0001 |
| 5 | Add environment configuration | Read `PIXELA_USERNAME` and `PIXELA_TOKEN` from the process environment in `infrastructure/config/`; the project never reads or imports `.env`. | No | |
| 6 | Add command line and create-user command | Add the composition root and the `create-user` command in `presentation/` (command per use case) with `--dry-run`, and export `create_user` from the package. | No | |
| 7 | Add tests for create user | Add unit tests with a fake gateway, an integration test against a local `http.server`, and an end-to-end test of the command, all offline; plus the code review record for the milestone. | No | |

---

[BC-001]: ../business-case.md
