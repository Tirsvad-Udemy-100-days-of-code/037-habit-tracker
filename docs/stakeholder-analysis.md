# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-22 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [08a6fcc] |

---

## Purpose

The analysis names the people who influence or use the Habit Tracker and decides how closely each is involved. It uses the power/interest grid. The IDs below are the stable identifiers that every other document uses for owners, reviewers and RACI.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Finish the assignment with work that is correct, reviewable and reusable |
| S02 | Udemy coursists | Participants of the 100 Days of Code course who share code and compare solutions | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | GitHub community | LOW | LOW | Monitor | A clear repository description, topics and README, and no extra setup |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, writes and reviews every document and accepts the plan. High power and high interest.
- **Keep Informed (S02):** cannot change the project, but uses the result and compares it with their own. High interest, low power.
- **Monitor (S03):** browses the repository and may use an idea. Low power and low interest; the repository description, topics and README are enough for them.

The brief for the project gave S03 "no runtime dependencies" as a need. The quadrant of S03 is Monitor, so a small relaxation is acceptable when it serves S02 (see the conflict below).

## Primary Concerns and FURPS+ Mapping

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Correct calls to the Pixela API, reviewable steps, reuse | Functionality, Supportability |
| S02 | Readable code, the assignment's function names, instructions that work | Usability, Functionality |
| S02 | Code that runs without hidden setup | Usability |
| S03 | Clear description, topics and README | Usability |
| S03 | No runtime dependencies | Implementation constraint (+) |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat in the working session | At every plan and every end-of-run summary | Plan, review records, summary | All milestones |
| S02 | Repository README and wiki | At each merge to `main` | Run instructions, wiki pages in three languages | MIL-005 |
| S03 | Repository description, topics and README | Once, updated when scope changes | Description, topics, README | MIL-001, MIL-005 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S03 wants no runtime dependencies, S02 wants code that uses `requests` as the lectures do | S02, S03 | S01 decided for `requests` (ADR-0001). It is the only runtime dependency, the README names it and gives the install command, and everything else is the standard library |
| S02 wants the code to look like the lecture, S01 wants layered, tested code | S01, S02 | The assignment's function names stay (`create_user`, `create_graph`, `post_pixel`) in one readable module of the application layer, and the layers are explained in the wiki |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct calls, reviewable work | Objective 1 and 3 ([BC-001]) |
| S02 | Assignment's function names | Objective 1 ([BC-001]) |
| S02 | Instructions that work | Objective 4 and 6 ([BC-001]) |
| S03 | Description, topics, README | Objective 7 and 6 ([BC-001]) |
| S03 | No runtime dependencies | Constraint on dependencies ([BC-001]) |

## Sign-Off

S01 accepts the analysis as Product Owner. In autonomous mode the review is recorded as AI as stand-in for S01.

---

[BC-001]: ./business-case.md
[08a6fcc]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/commit/08a6fcc2c14667fa77bf15d126c00b34200252b5
