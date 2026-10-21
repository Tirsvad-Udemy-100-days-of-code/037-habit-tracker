# MIL-003: Create graph

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-22 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [08a6fcc] |

---

## Purpose

This gate decides whether the second lecture step, creating a graph with the token sent in an HTTP header, works and is safe: the token must travel in the `X-USER-TOKEN` header and never in the URL or the body.

## Deliverable

A `create_graph` function and a `create-graph` command that send the Pixela graph request to `/v1/users/<username>/graphs`, with the graph domain rules and tests.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `from habit_tracker import create_graph` works | Imports | ImportError |
| 2 | A test shows that the request goes to `https://pixe.la/v1/users/<username>/graphs` with `id`, `name`, `unit`, `type` and `color` in the body | Pass | Fail |
| 3 | A test shows that the token is in the `X-USER-TOKEN` header and not in the URL or the body | Pass | Fail |
| 4 | A test shows that an invalid graph id, type or colour is rejected before any request is sent | Pass | Fail |
| 5 | The accepted colours are the Pixela names `shibafu`, `momiji`, `sora`, `ichou`, `ajisai` and `kuro` | Exactly these | Any difference |
| 6 | `ruff`, `mypy --strict` and `pytest` are clean, and the code review against `QC-PY-001` is a Go | Clean and Go | Any finding or No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The gateway port, the adapters, the credentials and the command line are reused |

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

2026-10-25 — within the two-day effort of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add graph domain types | Add `GraphId`, `GraphType` and `GraphColor` (enums for the Pixela colour names `shibafu`, `momiji`, `sora`, `ichou`, `ajisai`, `kuro`) and a `Graph` value object in `domain/` with the Pixela id rule (lower case letter first, 1 to 16 characters of letters, digits and hyphen). | No | ADR-0002 |
| 2 | Implement create_graph use case | Add `create_graph(gateway, credentials, graph)` in `application/use_cases/` that builds the URL with the username and puts the token in the `X-USER-TOKEN` header; this is the second assignment function. | No | ADR-0002 |
| 3 | Add create-graph command | Add the `create-graph` command in `presentation/` with `--id`, `--name`, `--unit`, `--type` and `--color`, and export `create_graph` from the package. | No | |
| 4 | Add tests for create graph | Add unit tests with a fake gateway for the URL, body and header, tests for the rules, an integration test against the local test server and an end-to-end test of the command; plus the code review record. | No | |

---

[BC-001]: ../business-case.md
[08a6fcc]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/commit/08a6fcc2c14667fa77bf15d126c00b34200252b5
