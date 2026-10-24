# RC-030: MIL-004 delta re-review: language and domain confirmed by S01

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-030 |
| CrossReference | [MIL-004], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-24 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-004]
- Checklist used: [QC-LANG-001] (`QC-LANG-001`)
- Scope: delta re-review of criteria 3, 5 and 9 of QC-LANG-001 only; reason: these criteria were checked by the AI as stand-in in RC-006 and S01 has now confirmed them; the content is unchanged; all other rows of RC-006 still hold
- Language and domain: en / it
- Language reviewer: none
- Mode: supervised for these rows: S01, who reads English and knows the IT domain, confirmed them in chat on 2026-10-24

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 3 | The content (prose and table cells) is written in the stated language | Pass | S01 confirmed in chat on 2026-10-24 that the content is written in English. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | S01 confirmed in chat on 2026-10-24 that the domain terms are used correctly; the project has no domain dictionary (ADR-0002). |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 reads English and knows software and IT, and confirmed the language check in chat on 2026-10-24; the review is by the person in the role, not by the stand-in. |

## Overall Verdict

Go — Criteria 3, 5 and 9 of QC-LANG-001 are confirmed by S01. This closes the stand-in decision recorded in RC-006; the other rows of RC-006 still hold because the content is unchanged.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Stand-in language check of RC-006 is confirmed by S01. | S01 | 2026-10-24 |

---

[MIL-004]: ../../milestones/mil-004-post-pixel.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
