# MIL-005: Documentation and wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-22 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [08a6fcc] |

---

## Purpose

This gate decides whether S02 and S03 can use the repository without help: a complete README, screenshots, a wiki in English, Danish and Bahasa Malaysia, and generated source documentation.

## Deliverable

The final README with screenshots, the wiki pages under `docs/wiki/` in three languages with the same page set, the publish-wiki workflow, and a Doxygen run that finishes without warnings.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The README follows the framework template and `check-readme.sh` passes | Passes | Fails |
| 2 | The README and the wiki contain screenshots that are files in `docs/images/` | At least 2 screenshots, all links resolve | Missing or broken |
| 3 | `docs/wiki/` has every page in English, Danish (`-da`) and Bahasa Malaysia (`-ms`) | Same page set in 3 languages | A page is missing in a language |
| 4 | Every wiki page starts with the language line and `_Sidebar.md` lists all languages | Present | Missing |
| 5 | `doxygen Doxyfile` finishes with no warning | 0 warnings | Any warning |
| 6 | The README tells how to run the project and its tests from a clean clone, and the commands were run as written | Verified | Not verified |
| 7 | `.gitea/workflows/publish-wiki.yml` is installed and parses as YAML | Valid | Missing or invalid |
| 8 | Test coverage of `src/` is at least 90 % | 90 % or more | Less |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | The documentation describes the finished commands |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 4, 5 and 6 | [BC-001] |
| Success criteria 3, 4 and 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-28 — within the two-day effort of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Capture screenshots | Run the three commands in dry-run mode and the test suite, render the real terminal output as images with a headless browser, and save them under `docs/images/` for the README and the wiki. No real Pixela account is created. | No | |
| 2 | Complete the README | Fill every section of the framework README template: overview, requirements, setup with the `.venv` steps, run, tests, license, links and the appendix of project documents, with the screenshots. | No | |
| 3 | Write the English wiki | Write the pages Home, Getting-Started, Usage, Architecture and Development, and `_Sidebar.md`, in English as the authoritative text, each starting with the language line. | No | |
| 4 | Write the Danish wiki | Translate every English page to Danish as `<Page>-da.md`, keeping commands, file names and IDs in English. | No | |
| 5 | Write the Bahasa Malaysia wiki | Translate every English page to Bahasa Malaysia as `<Page>-ms.md`, keeping commands, file names and IDs in English. | No | |
| 6 | Install publish-wiki workflow | Copy the framework template to `.gitea/workflows/publish-wiki.yml`, which calls the reusable workflow of `TirSystem/github-action`, and list the secret `TOKEN_FOR_GITEA_WIKI` in the README. | No | |
| 7 | Verify Doxygen output | Run `doxygen Doxyfile` and fix every warning so that the Doxygen comments of the source are complete. | No | |
| 8 | Close the plan | Update the project plan and the traceability matrix with the final state and the links of the milestones. | No | |

---

[BC-001]: ../business-case.md
[08a6fcc]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/commit/08a6fcc2c14667fa77bf15d126c00b34200252b5
