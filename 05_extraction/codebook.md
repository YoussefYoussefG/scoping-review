# Extraction codebook

`source_characteristics.csv`: one row per report (P ID), linked to the underlying study (S ID) when applicable. Bibliographic information remains tied to record IDs. Multiple reports are not independent studies.

`data_items.csv`: one row per extracted variable, report and subgroup/time point. Define topic-specific variables in variable_dictionary.csv before extraction. Capture units, denominator and context. Source locator is a printed/PDF page plus table/figure/section where possible. A brief evidence excerpt or faithful paraphrase supports verification; avoid copying long passages.

Missing values: NR = not reported after checking; NA = not applicable; NOT_ASSESSED = not yet checked; UNCLEAR = reported ambiguously. Blank means unfinished. Never convert these to zero. Separate author-reported values from derived calculations; give formula and input record IDs for derived values.

Verification: pending, verified, disputed. Record extractor, verifier, date, source locator and version. Keep disagreements and their resolution in the decisions log. Do not treat abstract-only extraction as verified full-text evidence. Topic-specific fields will be added after the question is confirmed.
