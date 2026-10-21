# RC-016: MIL-005 YAML review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [MIL-005], [QC-YML-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-22 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-005]
- Checklist used: [QC-YML-001] (`QC-YML-001`)
- Scope: full review of .gitea/workflows/publish-wiki.yml and the changed .gitea/workflows/english-comments.yml; the other YAML files were reviewed with MIL-001
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file parses with a safe YAML loader and has no duplicate keys in any mapping | Pass | PyYAML 6.0.3 `safe_load` parses the files (tests/unit/test_workflows.py); yamllint's `key-duplicates` rule finds no duplicate key. |
| 2 | Indentation is 2 spaces everywhere, never tabs; lines end with LF; the file ends with one newline and has no trailing spaces | Pass | yamllint (indentation, new-lines, trailing-spaces, new-line-at-end-of-file) passes; `.gitattributes` fixes LF. |
| 3 | Passes `yamllint` (or the project's YAML linter) with its configuration committed next to the code and no unexplained `disable` comments | Pass | `yamllint -c .yamllint.yml` (yamllint 1.35.1) passes; the only disabled rule, `document-start`, has a comment saying why. |
| 4 | A scalar that YAML would coerce to another type is quoted: `yes`, `no`, `on`, `off`, `null`, `~`, numbers with a leading zero, versions such as `1.10`, and values that contain `: ` or ` #` | Pass | `python-version` is quoted ("3.13"); `on` is the trigger key of a workflow, which yamllint is configured to accept. |
| 5 | Only safe, plain types are used: no language-specific tags (`!!python/object`, `!ruby/object`) and no `!include`-style extension unless the consuming tool documents it | Pass | Only plain mappings, sequences and scalars; no tag. |
| 6 | No secret is written in the file: no password, token, key or private connection string; a secret is referenced by name and supplied by the consuming tool | Pass | No secret is written in any of the files. |
| 7 | Embedded program text (shell, Python, SQL, `jq`, and so on) in a value is at most five lines; a longer one is moved to a file of its own, in its own language, and the YAML calls it | Pass | Every `run:` value is one line. |
| 8 | A block of keys or values repeated in the file or across files is defined once (an anchor, a template, an include or a reusable unit the consumer supports) | Pass | No block is repeated; the permissions of each job are different. |
| 9 | Anchors, aliases and merge keys (`&`, `*`, `<<`) are used only where the consuming tool is known to support them | Pass | No anchor, alias or merge key. |
| 10 | The file validates against the schema of the consuming tool where one exists, and the schema or tool version is stated | N-A | No schema is used; the workflow test and the run on Gitea 1.27.3 are the checks. |
| 11 | A header comment states what the file is for, which tool reads it, and where its decision or design is recorded | Pass | The header comment of `publish-wiki.yml` names its purpose, the reader (Gitea Actions), the opt-in and the decision (MIL-005 of the project plan). |
| 12 | Key names follow the convention of the consuming tool; one case style is used within the file (kebab-case or snake_case, never mixed) | Pass | All keys use kebab-case (`runs-on`, `timeout-minutes`, `cancel-in-progress`, `python-version`). |
| 13 | Multi-line strings use a block scalar (`\|` or `>`) and state the chomping indicator (`\|-`, `\|+`) where the trailing newline matters | N-A | No multi-line scalar is used. |
| 14 | The file name is lowercase kebab-case with one extension style (`.yml` or `.yaml`) used throughout the repository | Pass | `publish-wiki.yml` and `english-comments.yml`: lower case kebab-case, `.yml` throughout. |
| 15 | A change is exercised by a check that runs without the real target: a parse and schema test, or a dry run of the consuming tool | Pass | `tests/unit/test_workflows.py` and yamllint check the files without the real target. |

## Overall Verdict

Go — All Mandatory criteria of QC-YML-001 pass.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None. Every criterion passes. | S01 | - |

---

[MIL-005]: ../../milestones/mil-005-docs-and-wiki.md
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md
