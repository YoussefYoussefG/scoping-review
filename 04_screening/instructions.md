# Screening instructions

Use the current approved eligibility version. `decisions.csv` has one row per reviewer, record, stage and decision version. Stages: title_abstract, full_text. Decisions: include, exclude, unsure. Keep each reviewer's judgement independent. `consensus.csv` records resolved decisions and the adjudication trail; never overwrite original decisions. Supersede prior rows explicitly when revising.

Use reason codes from eligibility.csv for full-text exclusions; choose one principal reason in a documented priority order. Log retrieval failures separately in retrieval.csv. Use report IDs to connect multiple imported records to one publication. Resolve duplicates before counting selection outcomes.
