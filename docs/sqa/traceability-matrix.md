# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [ADR-0001], [ADR-0002], [RC-001], [RC-002], [RC-003], [RC-004], [RC-005], [RC-006], [RC-007], [RC-008], [RC-009], [RC-010], [RC-011], [RC-012], [RC-013], [RC-014], [RC-015], [RC-016], [RC-017], [RC-018], [RC-019], [RC-020], [RC-021], [RC-022], [RC-023], [RC-024], [RC-025], [RC-026], [RC-027], [RC-028], [RC-029], [RC-030], [RC-031], [MIL-006], [RC-032], [RC-033], [RC-034], [RC-035] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-24 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added RC-030 for MIL-004 | [8ebc4dd] |
| 2026-10-24 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added RC-031 for MIL-005 | [8ebc4dd] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added MIL-006, the review records RC-032 to RC-035 and the wiki; set the reviewed rows of BC-001 and PP-001 and the domain of the changed rows to education; replaced the stale coverage note (autonomous, not independent) | [c70439b] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | education | - | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006] | [RC-032], [RC-001], [RC-018], [RC-025] |
| [SA-001] | SA | en | it | [BC-001] | [BC-001], [PP-001] | [RC-002], [RC-019], [RC-026] |
| [PP-001] | PP | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006] | [RC-033] |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | [MIL-002] | [RC-003], [RC-010], [RC-011], [RC-012], [RC-020], [RC-027] |
| [MIL-002] | MIL | en | it | [BC-001], [PP-001], [MIL-001] | [MIL-003] | [RC-004], [RC-013], [RC-021], [RC-028] |
| [MIL-003] | MIL | en | it | [BC-001], [PP-001], [MIL-002] | [MIL-004] | [RC-005], [RC-014], [RC-022], [RC-029] |
| [MIL-004] | MIL | en | it | [BC-001], [PP-001], [MIL-003] | [MIL-005] | [RC-006], [RC-015], [RC-023], [RC-030] |
| [MIL-005] | MIL | en | it | [BC-001], [PP-001], [MIL-004] | [MIL-006] | [RC-007], [RC-016], [RC-017], [RC-024], [RC-031] |
| [MIL-006] | MIL | en | education | [BC-001], [PP-001], [MIL-005] | - | [RC-034] |
| [ADR-0001] | ADR | - | - | [BC-001], [SA-001] | [MIL-002] | [RC-008] |
| [ADR-0002] | ADR | - | - | [BC-001] | [MIL-002], [MIL-003], [MIL-004] | [RC-009] |
| Wiki | Wiki | en, da, ms | education | [BC-001], [MIL-006] | - | [RC-035] |

## Coverage Notes

- `-` in Upstream means the instance is foundational, in Downstream that nothing is built on it yet, and in Last Reviewed that no `RC-*` exists yet.
- [PP-001] was accepted without a QC checklist; it is reviewed against `QC-PP-001` for the first time in [RC-033].
- The wiki (`docs/wiki/`) is documentation, not an artifact with an ID or a Language and Domain row; it has its own review record, [RC-035].
- The project workflow `.gitea/workflows/publish-wiki.yml` that [MIL-005] added was removed in pull request #40, when the repository moved to the shared workflows of the git host; RC-017 reviewed it while it existed. `ci.yml` and `english-comments.yml` are still reviewed there and in RC-012.
- The domain of [BC-001], [PP-001], [MIL-006] and the wiki is `education` since [MIL-006]. The other documents keep the domain `it` they were accepted with; a change of their domain would need a new review of each (see the Open Issues of [PP-001]).
- [MIL-006] changes no source file, so the source code is not reviewed again. Its only changes under `tests/` are the pattern of the shared workflow repository in `tests/unit/test_workflows.py` and the sidebar check in `tests/unit/test_wiki.py` (task 6), and its only change to `.gitea/workflows/ci.yml` is the version of the coverage upload action (task 7); the test suite and the quality checks of the pull request verify them, and no new code review record is written for them.
- The types KPI, BMC, BPMN, UCD, US, UC, DM, SSD, OC, SD, DCD, ERD and DICT have no instance (ADR-0002).

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-setup.md
[MIL-002]: ../milestones/mil-002-create-user.md
[MIL-003]: ../milestones/mil-003-create-graph.md
[MIL-004]: ../milestones/mil-004-post-pixel.md
[MIL-005]: ../milestones/mil-005-docs-and-wiki.md
[ADR-0001]: ../adr/adr-0001-requests-as-runtime-dependency.md
[ADR-0002]: ../adr/adr-0002-no-use-case-artifacts.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-mil-001-project-setup.md
[RC-004]: ./reviews/rc-004-mil-002-create-user.md
[RC-005]: ./reviews/rc-005-mil-003-create-graph.md
[RC-006]: ./reviews/rc-006-mil-004-post-pixel.md
[RC-007]: ./reviews/rc-007-mil-005-docs-and-wiki.md
[RC-008]: ./reviews/rc-008-adr-0001.md
[RC-009]: ./reviews/rc-009-adr-0002.md
[RC-010]: ./reviews/rc-010-mil-001-code.md
[RC-011]: ./reviews/rc-011-mil-001-yaml.md
[RC-012]: ./reviews/rc-012-mil-001-workflows.md
[RC-013]: ./reviews/rc-013-mil-002-code.md
[RC-014]: ./reviews/rc-014-mil-003-code.md
[RC-015]: ./reviews/rc-015-mil-004-code.md
[RC-016]: ./reviews/rc-016-mil-005-yaml.md
[RC-017]: ./reviews/rc-017-mil-005-workflows.md
[RC-018]: ./reviews/rc-018-business-case-delta.md
[RC-019]: ./reviews/rc-019-stakeholder-analysis-delta.md
[RC-020]: ./reviews/rc-020-mil-001-project-setup-delta.md
[RC-021]: ./reviews/rc-021-mil-002-create-user-delta.md
[RC-022]: ./reviews/rc-022-mil-003-create-graph-delta.md
[RC-023]: ./reviews/rc-023-mil-004-post-pixel-delta.md
[RC-024]: ./reviews/rc-024-mil-005-docs-and-wiki-delta.md
[RC-025]: ./reviews/rc-025-business-case-language.md
[RC-026]: ./reviews/rc-026-stakeholder-analysis-language.md
[RC-027]: ./reviews/rc-027-mil-001-project-setup-language.md
[RC-028]: ./reviews/rc-028-mil-002-create-user-language.md
[RC-029]: ./reviews/rc-029-mil-003-create-graph-language.md
[RC-030]: ./reviews/rc-030-mil-004-post-pixel-language.md
[RC-031]: ./reviews/rc-031-mil-005-docs-and-wiki-language.md
[8ebc4dd]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/commit/8ebc4dd14053913fd2d9cd777c4b9a22f7fbfd82
[MIL-006]: ../milestones/mil-006-framework-baseline.md
[RC-032]: ./reviews/rc-032-business-case-baseline.md
[RC-033]: ./reviews/rc-033-project-plan-baseline.md
[RC-034]: ./reviews/rc-034-milestone-006.md
[RC-035]: ./reviews/rc-035-wiki.md
[c70439b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/commit/c70439bcf73548c2279f0cd9d30b3c1e92188270
