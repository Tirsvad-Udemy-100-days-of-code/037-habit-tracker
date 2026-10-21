# Architecture Decision Record

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-22 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [08a6fcc] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The assignment is about the `requests` module. S02 compares code with the lectures, so the code should use the same API. S03 asked for no runtime dependencies, and the brief says to avoid runtime dependencies unless they are needed. The two needs conflict.

Options evaluated:

1. Use `requests`, the one runtime dependency. S02 can compare line by line with the lecture. S03 installs one package.
2. Use only `urllib` from the standard library. No runtime dependency, but the code no longer shows what the lectures teach, and it is longer and harder for a beginner to read.

S01 was asked and chose option 1 in chat on 2026-10-22.

## Decision

The project uses `requests` as its only runtime dependency, behind a gateway port in the infrastructure layer, and adds no other runtime dependency.

## Consequences

**Positive:**

- The code matches the lectures, which serves S02 and objective 1 of the Business Case.
- Because `requests` is only in the infrastructure adapter, the domain and application layers stay free of it and can be tested with a fake gateway.

**Negative:**

- S03's wish for no runtime dependencies is relaxed; a viewer has to install one package.
- The README must say why the dependency is needed.

## Affected Artifacts

- [BC-001] — the constraint "one runtime dependency at most" follows this decision.
- [SA-001] — the conflict between S02 and S03 is resolved here.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[08a6fcc]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/commit/08a6fcc2c14667fa77bf15d126c00b34200252b5
