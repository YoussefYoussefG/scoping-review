# Team contribution guide

## GitHub workspace
Repository: https://github.com/YoussefYoussefG/scoping-review
Owner: YoussefYoussefG. Public visibility authorized on 2026-11-22.
Use the documentation and CSV templates to maintain the review audit trail.

## Invite your teammates
After creation, open the repository → Settings → Collaborators (under Access) → Add people. Search each teammate's GitHub username or email, choose the person and send the invitation. They must accept it. In a personal repository these are collaborators; GitHub Teams are an organization feature. Invite only intended contributors because invited collaborators have write access.
Official instructions: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository

## Daily work
1. Create an issue for a specific task and assign an owner.
2. Create a branch such as protocol/eligibility or extraction/batch-001.
3. Edit the relevant files, keeping evidence locators, versions and decision records.
4. Open a pull request with the changes, sources, checks and unresolved questions. Ask another team member to review before merging to main. This is a team convention until branch rules are actually configured.
5. Resolve comments, merge and update the task log. Avoid simultaneous edits to the same CSV; agree on batches or separate reviewer files and merge carefully.

## Review roles
Name the lead, two independent screening reviewers, adjudicator, search specialist where available, extractors and verifiers. AI is not an independent human reviewer. A shared Git repository does not blind reviewer decisions: use a blinded screening system or private independent worksheets during screening, then archive exports after decisions are locked.

## Evidence and documentation
Preserve original exports and reviewer decisions. Cite page/table/section for extracted values. Record protocol changes in amendments.csv. Run python3 scripts/validate_workspace.py. Never include secrets. Full texts and restricted exports remain in ignored storage and need separate team access/backups. The repository alone does not back up ignored files. Authorship/contributions should be agreed explicitly, not inferred from commit counts.

