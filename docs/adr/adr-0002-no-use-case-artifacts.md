# Architecture Decision Record

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0002 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-22 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [08a6fcc] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The three lecture steps (create a user, create a graph, post a pixel) are goals of one actor, S01 or S02, so the `project-planning` skill would give each a user story and a use case, and a domain model, system sequence diagram and design class diagram on top. The project is a lesson exercise of three POST requests with no stored data and no more than one actor. The Business Case sets about two days of effort.

Options evaluated:

1. Write a user story, a use case and design artifacts for each step. Complete, but the documents would be longer than the code they describe.
2. Skip the use cases and the design artifacts, state the steps as tasks in the milestones, and describe the design in the code (Doxygen) and in the wiki page Architecture.

## Decision

The project writes no user story, use case, domain model, system sequence diagram or design class diagram; the three lecture steps are plain tasks of the milestones MIL-002 to MIL-004, and the design is documented in the Doxygen comments and in the wiki.

## Consequences

**Positive:**

- The effort stays in proportion to the project, and the baseline (Business Case, Stakeholder Analysis, Project Plan, milestones) is complete.
- The tasks still trace to the Business Case objectives through their milestones.

**Negative:**

- There is no use case that a reviewer can check the behaviour against; the Go/No-Go criteria of the milestones take that role.
- If the project grows (update and delete of pixels), a use case must be written first.

## Affected Artifacts

- [BC-001] — the scope names the three steps, which the milestones deliver without use cases.

---

[BC-001]: ../business-case.md
[08a6fcc]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/commit/08a6fcc2c14667fa77bf15d126c00b34200252b5
