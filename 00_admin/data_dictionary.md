# Shared table conventions

CSV files are UTF-8 with headers. Keep commas and line breaks quoted using a CSV-aware editor. Dates use ISO format; execution timestamps include offset. *_id fields are stable identifiers; never renumber after screening begins. Pipe-separated columns in this description are stored as normal CSV columns. For multiple references inside a field, use semicolons and define the convention in the analysis code.

Decision and consensus tables are append-only: use supersedes IDs for corrections. Each search run gets its own ID even for repeat searches. Different hits from different exports keep separate record IDs before deduplication. Full-text retrieval status is pending, retrieved or not_retrieved. Source paths point to local files; publication requires a separate rights review.

Blank cells are unfinished. Extracted missingness uses the explicit codes in 05_extraction/codebook.md. Checklist status: pending, complete, not_applicable (with justification). Task status: pending, in_progress, blocked, complete. No person is considered to have approved a decision until their actual approval is recorded.
