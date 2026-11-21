# Scoping review workspace

Status: setup only; topic, eligibility criteria, reviewer team and protocol remain unconfirmed. No review searches or screening have been performed. Empty tables mean not yet populated, not zero results.

Start with [project brief](00_admin/project_brief.md), then complete [protocol](01_protocol/protocol.md). Follow [workflow](00_admin/workflow.md). Reporting follows PRISMA-ScR; methods are to be specified using JBI guidance. These templates do not establish compliance by themselves.

## Repository map
- `00_admin/`: project brief, decisions, tasks, supplied-file inventory, AI activity.
- `01_protocol/`: dated protocol, eligibility rules, amendments and approvals.
- `02_search/`: exact strategies, search runs, raw exports and search review.
- `03_records/`: imported citations, duplicate decisions and record-to-report links.
- `04_screening/`: independent decisions, reconciled outcomes and retrieval tracking.
- `05_extraction/`: source characteristics, evidence values, verification and codebook.
- `06_synthesis/`: analysis plan, evidence map and claim-to-source ledger.
- `07_reporting/`: manuscript, PRISMA-ScR tracking and flow counts.
- `08_references/`: bibliography and methods sources.
- `09_tools/`: installation record and tool limitations.
- `local_only/`: PDFs, restricted materials and private working files; ignored by Git.

## Working conventions
Use stable IDs: search `Q0001`, imported record `R000001`, report `P000001`, underlying study `S000001`. Multiple database records can point to one report; several reports can describe one study. Record timestamps with timezone, dates as YYYY-MM-DD. Preserve source exports unchanged and hash them. Keep original reviewer decisions when recording consensus. Every extracted value needs a source locator and verification status. Never replace unknown values with zero. See the data dictionary.

Run `python3 scripts/validate_workspace.py` to check CSV shape, identifiers and selected links. This structural check does not assess methodological completeness. Keep documentation updated with each substantive change. Commit small, meaningful changes; protocol changes also require an amendment row.

This is a local Git repository. No GitHub remote, public deposit, protocol registration or submission has been made.
