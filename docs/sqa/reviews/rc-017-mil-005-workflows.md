# RC-017: MIL-005 workflow review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-017 |
| CrossReference | [MIL-005], [QC-WF-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-22 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-005]
- Checklist used: [QC-WF-001] (`QC-WF-001`)
- Scope: full review of .gitea/workflows/publish-wiki.yml; applies together with the YAML review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file meets the YAML checklist ([QC-YML-001]) | Pass | See the YAML review of MIL-005: Go. |
| 2 | The file is in `.gitea/workflows/` or `.github/workflows/` with the extension `.yml` or `.yaml`, and the same workflow does not exist in both directories | Pass | The file is in `.gitea/workflows/` with extension `.yml`; there is no `.github/workflows/`. |
| 3 | The file declares `name`, `on` and `jobs`; `on` lists explicit events and, where it matters, `branches` or `paths` | Pass | Declares `name`, `on` (push to `main`, path `docs/wiki/**`) and `jobs`. |
| 4 | A header comment states the purpose, the triggers, the inputs, the secrets it needs, what it changes outside the repository, and the decision or milestone it implements | Pass | The header comment states purpose, trigger, the secret it needs, what it changes outside the repository (the wiki) and the decision. |
| 5 | Every job and step has a descriptive `name`, unique within its job | Pass | The workflow, the job and the trigger are named; the job is a call of the shared workflow. |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated | Pass | `tests/unit/test_workflows.py` passes for the file; actionlint is not used. |
| 7 | Every job declares `permissions` explicitly with the least access that works (`contents: read` or none by default); write access only on the job that needs it | Pass | The job declares `permissions: contents: read`; the wiki is written with the secret token, not the run token. |
| 8 | Every action used is pinned to a full commit SHA or an exact release tag, never to a branch; a moving major tag (`@v1`) is accepted only for an action published by the same organisation under a stated release policy | Pass | The shared workflow is called at the major tag `v2` of the same organisation under its release policy (`MAJOR_TAG`). |
| 9 | No secret is written in the file; a secret is read as `secrets.NAME`, passed to a step through `env:`, never placed on a command line or echoed | Pass | The secret is passed as `${{ secrets.TOKEN_FOR_GITEA_WIKI }}` to the reusable workflow; the name does not start with `GITEA_` or `GITHUB_`; the value is not in the file. |
| 10 | Untrusted text (`inputs.*`, event fields such as a title, branch name or label, step outputs derived from them) is never interpolated into a `run:` script; it is passed through `env:` and used as a quoted variable | Pass | No expression other than the secret reference. |
| 11 | A trigger that gives a run secrets or a write token on code from a fork or an untrusted branch (`pull_request_target`, `workflow_run`) does not check out or execute that code | Pass | Trigger is `push` to `main`; no `pull_request_target`. |
| 12 | A workflow that changes state outside the repository (release, tag, publish, sync, deploy) is started by hand or by a protected branch, and a manual run defaults to a dry run with an explicit input to apply | Pass | The workflow changes the wiki, so it starts only on a push to `main`; the template's `workflow_dispatch` was removed, so no manual run can publish or prune by accident. |
| 13 | The token the workflow uses has only the scope the job needs, and where the host's built-in token is enough it is used instead of a personal token | Pass | The token has the single scope `write:repository`, as the header says. |
| 14 | Every job sets `runs-on` to an explicit label and `timeout-minutes` | Pass | The job calls a reusable workflow, which sets the runner and the timeout. |
| 15 | `concurrency` is set where two runs would conflict: a check cancels the older run (`cancel-in-progress: true`); a publishing job queues (`cancel-in-progress: false`) | Pass | `concurrency` group `publish-wiki` with `cancel-in-progress: false`, so two merges queue. |
| 16 | Triggers are filtered (`branches`, `paths`, `types`) so the workflow runs only for the changes it concerns | Pass | Triggers are limited to `main` and to `docs/wiki/**`. |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place | Pass | The tool version comes from the shared workflow's `tools-ref` default, in one place. |
| 18 | A dependency cache is used where the install is slow enough to matter | N-A | The install takes seconds; a cache is not worth its complexity. |
| 19 | A failing step names the tool, the file and the reason in its log (annotation or `::error::` line) | Pass | The shared workflow names the pages it publishes or fails with the reason. |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file (`tools/`, or a shared repository fetched at a pinned ref) that the step calls with one command, and the workflow passes its settings through `env:` | Pass | No `run:` block. |
| 21 | Logic used by more than one workflow or repository is a reusable workflow (`workflow_call`) or a composite action; each input has a `description`, a `type` and a `default` where one is sensible | Pass | The publishing is the shared reusable workflow; nothing is copied. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header | Pass | The same shared workflow runs successfully on this Gitea 1.27.3 instance for the wiki of TirSystem/github-action (publish-own-wiki.yml, two successful runs). The first run of this caller happens after the merge and needs the secret that S01 sets; see the action item. |
| 23 | A reusable workflow states, in its header, how a caller pins it and the script it fetches, so the workflow and its script are the same release | N-A | The files are callers, not reusable workflows. |
| 24 | A static test of the repository's workflows exists and runs on every pull request: valid YAML, required keys, explicit permissions and runner, no inline script above the limit | Pass | `tests/unit/test_workflows.py` runs in the `tests` job on every pull request. |

## Overall Verdict

Go — All Mandatory criteria of QC-WF-001 pass; the first run of this caller depends on the secret, which is an action item for S01.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Set the secret TOKEN_FOR_GITEA_WIKI in the organisation and enable the wiki in the repository settings; then check the first run of publish-wiki.yml. | S01 | 2026-10-28 |

---

[MIL-005]: ../../milestones/mil-005-docs-and-wiki.md
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md
