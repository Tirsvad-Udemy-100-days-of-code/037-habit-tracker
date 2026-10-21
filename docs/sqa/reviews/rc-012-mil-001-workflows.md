# RC-012: MIL-001 workflow review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [MIL-001], [QC-WF-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-22 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [8129020] |

---

## Artifact Under Review

- Instance reviewed: [MIL-001]
- Checklist used: [QC-WF-001] (`QC-WF-001`)
- Scope: full review of .gitea/workflows/ci.yml and .gitea/workflows/english-comments.yml; applies together with the YAML review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file meets the YAML checklist ([QC-YML-001]) | Pass | See the YAML review of MIL-001: Go. |
| 2 | The file is in `.gitea/workflows/` or `.github/workflows/` with the extension `.yml` or `.yaml`, and the same workflow does not exist in both directories | Pass | Both files are in `.gitea/workflows/` with extension `.yml`; there is no `.github/workflows/`. |
| 3 | The file declares `name`, `on` and `jobs`; `on` lists explicit events and, where it matters, `branches` or `paths` | Pass | Both declare `name`, `on` (with `branches: [main]`) and `jobs`. |
| 4 | A header comment states the purpose, the triggers, the inputs, the secrets it needs, what it changes outside the repository, and the decision or milestone it implements | Pass | Each header comment states purpose, triggers, jobs, secrets, what changes outside the repository and the decision. |
| 5 | Every job and step has a descriptive `name`, unique within its job | Pass | Every job and every step has a descriptive `name`. |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated | Pass | The project's workflow validation test `tests/unit/test_workflows.py` passes (pytest 9.1.1, PyYAML 6.0.3); actionlint is not used. |
| 7 | Every job declares `permissions` explicitly with the least access that works (`contents: read` or none by default); write access only on the job that needs it | Pass | Every job declares `permissions`: `contents: read`; `contents: write` only on the metrics job; `pull-requests: write` only on the English comments job, which comments. |
| 8 | Every action used is pinned to a full commit SHA or an exact release tag, never to a branch; a moving major tag (`@v1`) is accepted only for an action published by the same organisation under a stated release policy | Pass | checkout 4.2.2, setup-python 5.4.0 and upload-artifact 4.6.2 are exact tags; the shared workflows of TirSystem/github-action are at the major tag `v2`, the same organisation under the release policy of its `MAJOR_TAG`. |
| 9 | No secret is written in the file; a secret is read as `secrets.NAME`, passed to a step through `env:`, never placed on a command line or echoed | Pass | No secret is used; `REPORT_TOKEN` is named only in a comment. |
| 10 | Untrusted text (`inputs.*`, event fields such as a title, branch name or label, step outputs derived from them) is never interpolated into a `run:` script; it is passed through `env:` and used as a quoted variable | Pass | The only expression in the files is `github.ref` in a `concurrency` group; no untrusted text reaches a `run:` script. |
| 11 | A trigger that gives a run secrets or a write token on code from a fork or an untrusted branch (`pull_request_target`, `workflow_run`) does not check out or execute that code | Pass | Triggers are `pull_request` and `push`; there is no `pull_request_target` or `workflow_run`. |
| 12 | A workflow that changes state outside the repository (release, tag, publish, sync, deploy) is started by hand or by a protected branch, and a manual run defaults to a dry run with an explicit input to apply | Pass | No release, tag, deploy or sync; the metrics job writes only the `badges` branch of this repository and runs on a push to `main`. |
| 13 | The token the workflow uses has only the scope the job needs, and where the host's built-in token is enough it is used instead of a personal token | Pass | The built-in token of the run is used; no personal token. |
| 14 | Every job sets `runs-on` to an explicit label and `timeout-minutes` | Pass | The own job `tests` has `runs-on: ubuntu-latest` and `timeout-minutes: 15`; the jobs that call a shared workflow take them from it. |
| 15 | `concurrency` is set where two runs would conflict: a check cancels the older run (`cancel-in-progress: true`); a publishing job queues (`cancel-in-progress: false`) | Pass | Both files set `concurrency` with `cancel-in-progress: true`; there is no publishing job that must queue. |
| 16 | Triggers are filtered (`branches`, `paths`, `types`) so the workflow runs only for the changes it concerns | Pass | Triggers are limited to pull requests and pushes to `main`. |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place | Pass | ruff and mypy come from the shared workflow's pinned defaults; the development tools are pinned exactly in `pyproject.toml`, one place; Python is 3.13. |
| 18 | A dependency cache is used where the install is slow enough to matter | N-A | The install takes seconds; a cache is not worth its complexity. |
| 19 | A failing step names the tool, the file and the reason in its log (annotation or `::error::` line) | Pass | The tools write `path:line` findings; the shared workflows list the failed tools. |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file (`tools/`, or a shared repository fetched at a pinned ref) that the step calls with one command, and the workflow passes its settings through `env:` | Pass | Every `run:` is one line. |
| 21 | Logic used by more than one workflow or repository is a reusable workflow (`workflow_call`) or a composite action; each input has a `description`, a `type` and a `default` where one is sensible | Pass | The quality checks, the metrics and the English comments check are the shared reusable workflows; nothing is copied. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header | Pass | Run 2545 (ci.yml) and run 2546 (english-comments.yml) on pull request 32 of git.tirsystem.com, Gitea 1.27.3, passed all jobs; the metrics job was skipped as designed. |
| 23 | A reusable workflow states, in its header, how a caller pins it and the script it fetches, so the workflow and its script are the same release | N-A | The files are callers, not reusable workflows. |
| 24 | A static test of the repository's workflows exists and runs on every pull request: valid YAML, required keys, explicit permissions and runner, no inline script above the limit | Pass | `tests/unit/test_workflows.py` runs in the `tests` job on every pull request. |

## Overall Verdict

Go — All Mandatory criteria of QC-WF-001 pass; criterion 22 is verified by two runs on the instance.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None. Every criterion passes. | S01 | - |

---

[MIL-001]: ../../milestones/mil-001-project-setup.md
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md
[8129020]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/commit/8129020b8a0f090aa2383d543f3a980cfbb021c1
