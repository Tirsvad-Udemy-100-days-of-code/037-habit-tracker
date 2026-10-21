# MIL-004: Post pixel

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-22 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [08a6fcc] |

---

## Purpose

This gate decides whether the third lecture step, adding a pixel to a graph, works: the date must be a `YYYYMMDD` string and the quantity a string such as `"9.74"`, and the token must travel in the header.

## Deliverable

A `post_pixel` function and a `post-pixel` command that send the Pixela pixel request to `/v1/users/<username>/graphs/<graph id>`, with the date and quantity rules and tests.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `from habit_tracker import post_pixel` works | Imports | ImportError |
| 2 | A test shows that the request goes to `https://pixe.la/v1/users/<username>/graphs/<graph id>` with `date` and `quantity` as strings in the body | Pass | Fail |
| 3 | A test shows that the date `2026-10-22` is sent as `20261022` and that an invalid date is rejected before any request | Pass | Fail |
| 4 | A test shows that a quantity is sent as a string and that a non-number is rejected | Pass | Fail |
| 5 | A test shows that the token is in the `X-USER-TOKEN` header only | Pass | Fail |
| 6 | The three commands work in `--dry-run` mode end to end | Pass | Fail |
| 7 | `ruff`, `mypy --strict` and `pytest` are clean, and the code review against `QC-PY-001` is a Go | Clean and Go | Any finding or No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | The graph id and the header handling are reused |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1 (the assignment's functions) | [BC-001] |
| Objective 3 (offline tests) | Success criteria 1, 2 and 3 of [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-26 — within the two-day effort of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pixel domain types | Add `PixelDate` (accepts a `date`, formats it as `YYYYMMDD`) and `Quantity` (a finite number kept as a string) and a `Pixel` value object in `domain/`, so the format the lecture stresses is enforced in one place. | No | ADR-0002 |
| 2 | Implement post_pixel use case | Add `post_pixel(gateway, credentials, graph_id, pixel)` in `application/use_cases/` that posts the pixel with the token in the header; this is the third assignment function. | No | ADR-0002 |
| 3 | Add post-pixel command | Add the `post-pixel` command in `presentation/` with `--graph-id`, `--date` and `--quantity`, and export `post_pixel` from the package. | No | |
| 4 | Add tests for post pixel | Add unit tests with a fake gateway, tests for the date and quantity rules, an integration test against the local test server and an end-to-end test of all three commands in dry-run; plus the code review record. | No | |

---

[BC-001]: ../business-case.md
[08a6fcc]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/commit/08a6fcc2c14667fa77bf15d126c00b34200252b5
