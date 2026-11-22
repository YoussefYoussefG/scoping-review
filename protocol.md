# Scoping review protocol

Version: 0.7 draft | Created: 2026-11-21 | Status: NOT APPROVED

Project context: [project_brief.md](project_brief.md). The user confirmed binary and multiclass classification, a multiphase CT focus with single-phase comparisons, and access to all three target databases on 2026-11-22. Other proposed methods below remain subject to team approval. PRISMA-ScR is the reporting framework, not a substitute for a review protocol.

## Title, authors and roles
Proposed title: **CT phase combinations in radiomics and deep learning for focal liver-lesion classification: a scoping review**.

Authors and roles pending: assign lead, two independent reviewers, adjudicator and search reviewer.

## Background and rationale
HepatoLens proposes classifying HH, HCC, ICC and liver metastases and comparing PVP alone, NC + AP + PVP, and all four phases including delayed phase. The review will map how existing studies use phases, combine information and validate classification models. It will not assume that adding delayed-phase imaging improves performance.

Existing reviews overlap with this topic: [Wang et al. (2022)](https://doi.org/10.1259/bjr.20211136) cover AI in hepatic CT/MRI, while [Younger et al. (online 2025; issue 2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12769607/) examine AI versus radiologists for HCC on multiphase CT. A proposed contribution is a cross-task map of exact phase combinations, fusion approaches and within-study evidence for phase contribution. Novelty remains to be established by a fuller overlap assessment. A scoping review suits this methodological mapping; it will not establish one universally best model.

## Objectives and PCC questions
Proposed PCC:

- **Population:** human patients with focal liver lesions, including human clinical imaging datasets. Human-only research is confirmed by the user (2026-11-22); animal research is excluded. No age restriction is proposed. Exclude any study involving animal subjects, animal imaging/data, or animal experiments, including mixed human–animal studies even when human results are separable. Incidental references to animal studies in a bibliography or background do not constitute animal research.
- **Concept:** radiomics, machine learning using CT-derived features, deep learning, and agentic or multi-agent workflows for binary or multiclass lesion classification using multiphase CT; retain single-phase comparison arms. CT is the only eligible imaging modality. Workflows requiring MRI, ultrasound, PET or other non-CT imaging for the reported classification result are outside scope; a separately evaluated CT-only arm may be retained.
- **Context:** any clinical setting or country, including retrospective model development and external validation.

Primary question: **How are CT phase combinations used in computational focal liver-lesion classification, including radiomics, deep learning and agentic or multi-agent workflows, and what evidence is reported about phase contribution and model validation?**

Secondary questions: Which lesion labels and reference standards are used? Which exact phases and fusion methods are evaluated? What direct evidence addresses adding delayed phase? Where implemented, what roles do agents perform and how is the complete workflow evaluated? How are patient separation, internal/external validation, class imbalance and uncertainty handled? Which evidence applies to the HepatoLens HH/HCC/ICC/LM task?

Binary and multiclass inclusion is confirmed. The precise PCC wording and remaining eligibility boundaries are draft.

## Eligibility
Operational draft rules are in [eligibility.csv](eligibility.csv), with a separate status for each decision. The proposed main corpus requires at least one evaluated multiphase classification approach; single-phase arms within those studies remain eligible. Whether to add standalone single-phase-only studies is still an open boundary and must be resolved before screening. Studies do not need to cover all four HepatoLens lesion labels.

Confirmed restrictions (user, 2026-11-22): **English-language full reports only, published within the last three years**. Operational interpretation: a rolling three-year window ending on the initial formal search date, inclusive; if searched on 2026-11-22, this is **2023-11-22 through 2026-11-22**. Freeze and document the exact window when the initial search is run; subsequent updates retain its lower bound and extend the upper bound. An English abstract alone does not make a non-English full report eligible. These user-selected restrictions narrow coverage; acknowledge potential language bias and omission of older evidence. Older sources may support background or search development but are not eligible primary evidence.

Apply supported publication-date and English-language limits in each database and record the exact settings. Where only year-level filtering is available, retrieve the encompassing years and check exact dates during screening. Proposed date convention: use the first publication date of the eligible report (online-first where available), document it, and manually resolve incomplete or conflicting dates.

Confirmed publication eligibility: include only peer-reviewed original research reported in full journal articles or full conference papers. Verify peer-review status from the journal or conference proceedings; database indexing alone does not establish it. Exclude all review articles (systematic, scoping, narrative and other reviews), meta-analyses, preprints, non-peer-reviewed reports, abstract-only conference records, editorials and protocols without original results. Dataset papers must be peer-reviewed and report an eligible original classification evaluation. Reviews may be consulted solely for background or locating primary studies; they never enter the included evidence or extraction set. Link multiple reports of the same study rather than counting them as independent studies. For a preprint with a published peer-reviewed version, assess the published version against all criteria and link the versions.

## Information sources and search methods
Target bibliographic databases confirmed by the user on 2026-11-22:

- **PubMed**
- **Scopus**
- **IEEE Xplore**

Additional sources requested if available: **UpToDate** and **NICE** (interpreting the user's wording as these named services). Proposed role: clinical background, relevant guidance and identification of cited primary studies. They will be documented separately from the bibliographic database searches. Guidance and clinical summaries are not eligible original research and will not enter the primary evidence corpus; use them only for background and locating potentially eligible primary studies.

The user confirmed team access to PubMed, Scopus and IEEE Xplore on 2026-11-22. Export functionality has not yet been tested by the assistant; individual full texts may still require retrieval. UpToDate access remains unconfirmed. The NICE guidance page returned HTTP 403 to the browsing tool during setup; this does not establish that the team cannot access it.

Search architecture (draft): combine (1) liver/hepatic lesion or tumour terms, (2) CT/computed tomography terms, and (3) radiomics/machine learning/deep learning, agentic AI, AI agents, multi-agent systems and related model terms. Agent terms belong in an OR branch of the methods block, not as a mandatory condition for all studies. Pilot alternate spellings and terminology in each database. Do not require the words delayed phase, all four target lesion types, or a particular performance metric: these could omit relevant studies. Initially assess phase eligibility during screening; pilot whether a phase term block loses known relevant studies.

Prepare and test a PubMed strategy with MeSH plus title/abstract terms; translate it to Scopus title/abstract/keyword fields and supported IEEE Xplore metadata fields. Verify actual interface syntax, query limits and known-paper retrieval before declaring strategies final. Candidate seed papers must themselves be checked for eligibility. An independent search reviewer should check concepts, spelling, Boolean logic and translation. Search references and citing papers of included studies and relevant reviews, recording the source and date. Plan an update before manuscript submission.

Still to specify: exact database-specific strategies, actual search dates, any additional grey-literature sources and named search reviewer. Record exact queries, limits, dates, counts and exports when searching begins. For supplementary sources, record the topic/guideline title, URL, version/update date, access date and any primary studies identified. No formal review searches have been run.

Source descriptions: [UpToDate](https://www.wolterskluwer.com/en/solutions/uptodate); [NICE guidance](https://www.nice.org.uk/guidance).

## Record management and selection
Proposed workflow, pending team agreement:

1. Preserve each original database export with database, exact query, search date and returned/exported counts. Retain provenance when merging duplicates. Record unique identifiers (DOI/PMID where available), title, year and authors; inspect uncertain duplicate matches manually. Do not deduplicate distinct reports solely because they use the same dataset.
2. Pilot 25–50 titles/abstracts with two independent human reviewers. Discuss disagreements, revise definitions and repeat a pilot if the criteria are unstable. Retain uncertain records for full-text assessment.
3. Screen all titles/abstracts independently, then pilot 5–10 full texts before independent full-text assessment. Resolve disagreements through discussion or a third reviewer.
4. Log retrieval attempts; reports not retrieved are distinct from reports assessed and excluded. Assign one principal full-text exclusion reason using the criteria, while retaining explanatory notes.
5. Reconcile PRISMA flow counts against the record history, keeping records, reports and studies distinct. No count is inferred from these planning notes.

Software/version and named reviewers remain pending. Rayyan or a shared sheet can be evaluated before selection; neither has been set up.

## Data charting
Proposed charting fields (no extraction file created yet):

- Citation, report/study/cohort IDs, country, setting, recruitment dates and data availability.
- Patient and lesion counts separately, lesion labels/class balance, diagnostic reference standard, public dataset name/version and overlap with other studies.
- Exact CT phase identities and timing, acquisition protocol, registration, segmentation/VOI source and preprocessing. Record author-defined phase terminology; do not infer identities from “three-phase” alone.
- Task, input unit (patient/lesion/slice), radiomics/features, model, pretraining, phase-fusion method and clinical covariates.
- For agentic workflows: author definition of an agent, number and roles of agents, underlying models, tools, orchestration, communication, autonomy, human oversight and end-to-end classification evaluation. Record comparisons with non-agent baselines where available. Do not equate ordinary ensembles or multi-branch networks with multi-agent systems without evidence of agent behavior.
- Train/validation/test sizes, split unit, patient independence, cross-validation, feature selection/tuning location, external validation and missing-data handling.
- Metrics with class/averaging definition, test cohort, thresholds, confidence intervals, calibration and reported errors. Distinguish accuracy from macro-F1 and per-class sensitivity.
- Each phase comparison: exact arms, shared patients/splits, model/training differences, paired testing and reported uncertainty. Flag whether delayed-phase contribution can actually be isolated.
- Funding/conflicts and reproducibility details.

Proposed pilot: one extractor and an independent verifier chart 3–5 varied studies, reconcile differences, then revise the form before full charting. Verify all extracted fields against page/table/figure locators. Use “not reported”, “not applicable” and “not assessed” distinctly. Revisit earlier records after material changes. Names and final fields require approval.

## Critical appraisal
Decision pending. Proposed minimum is descriptive charting of validation and reporting practices, without calling this a formal risk-of-bias assessment or assigning an invented quality score. If formal appraisal is selected, verify a current design-appropriate instrument, define reviewer procedures and explain its role in synthesis before use. Explain any omission in the manuscript; PRISMA-ScR treats critical appraisal as optional.

## Synthesis and presentation
Proposed outputs: descriptive tables of lesion tasks, exact phase combinations, fusion methods and validation designs; an evidence map of phase combinations by classification task; and a separate table of direct delayed-phase comparisons. Report denominators and missing information explicitly. Count linked cohorts/reports transparently.

Compare phase performance primarily within studies using matched cases and evaluation conditions. Differences across studies cannot establish the incremental benefit of delayed phase. Do not rank models by accuracy across different tasks or datasets. No meta-analysis is planned in this draft. Discuss evidence gaps and applicability to HepatoLens without presenting published results as team experiments.

## Stakeholder involvement
TBD whether, who, when and purpose.

## Transparency
Protocol deposit/registration: undecided, not registered. Record actual date, URL and version if deposited. Document amendments and AI assistance in the change notes below, with dates, reasons, affected work and human verification. Do not count AI as an independent human reviewer.

## Funding, conflicts, dissemination and approval
TBD funding/support and roles, conflicts, contributions, target outputs and sharing plan. Author approval names/dates: pending. Confirm current JBI guidance and journal requirements before protocol finalization.

## Change notes

- 2026-11-22: Moved this draft to the repository root and removed references to unused template folders. No eligibility or methodological decisions were finalized.

- 2026-11-22: Recorded the user-selected target databases and conditional supplementary sources. Search strategy and supplementary-source eligibility remain pending.

## Preliminary feasibility notes — not the formal review search

2026-11-22: Exploratory web queries included `systematic scoping review multiphasic CT focal liver lesions radiomics deep learning delayed phase classification`, and DOI-specific searches for the two datasets in the proposal. These were topic-orientation checks, not reproducible exports from the three selected databases, and supply no PRISMA counts.

- Existing review leads: Wang et al., DOI 10.1259/bjr.20211136; Younger et al., DOI 10.1007/s11604-025-01853-y. Their relevance is described above; neither is an included primary study.
- Primary-study candidate for search testing: Cao et al., *Multiphase convolutional dense network for classification of focal liver lesions on dynamic contrast-enhanced CT*, [DOI 10.3748/wjg.v26.i25.3660](https://doi.org/10.3748/wjg.v26.i25.3660). Eligibility has not been formally assessed.
- Dataset citations from the proposal: [MCT-LTDiag](https://doi.org/10.1038/s41597-025-06343-4) and [PLC-CECT](https://doi.org/10.1038/s41597-025-05125-2). Direct Nature retrieval failed during this check. Indexed MCT-LTDiag versions show a 2025 accepted manuscript and a 2026 final issue; verify final bibliographic metadata and dataset claims against the primary text before citation. No benchmark values have been independently validated here.
- Reporting reference: [official PRISMA-ScR checklist and explanation](https://www.prisma-statement.org/scoping). Maintain a checklist with manuscript locations during writing; reporting compliance is not yet established.

2026-11-22 amendment: user confirmed binary/multiclass inclusion and access to all three target databases. Expanded draft PCC, eligibility, selection, charting and synthesis methods with AI assistance. Remaining proposals require team review; no formal searching, screening or extraction performed.

2026-11-22 amendment (v0.3): User restricted eligibility to the last three years and English only. Replaced the earlier proposed unrestricted dates/languages in the protocol and criteria. Rolling-window interpretation and publication-date handling are documented above; no existing screened records require reassessment.

2026-11-22 amendment (v0.4): User explicitly excluded animal research. Confirmed human-only eligibility in the PCC and eligibility.csv. Mixed-species reports require separable human results; no screening has been performed.

2026-11-22 amendment (v0.5): User explicitly confirmed CT-only imaging and requested coverage of implemented agentic/multi-agent workflows. These workflows are eligible when they perform the same human focal liver-lesion classification task and meet the date, language and phase criteria. Generic agents for literature review, unrelated clinical tasks or report generation without evaluated lesion classification are outside the primary evidence corpus. Papers using other imaging modalities contribute only separately evaluated CT-only results. Agentic workflow coverage is an inclusion category, not a requirement for every study; its presence in the literature has not yet been established.

2026-11-22 amendment (v0.6): User strengthened the animal exclusion to cover any animal-related research component. This supersedes the v0.4 allowance for separately extractable human results from mixed-species studies. Exclude mixed human–animal research and workflows using animal data in development or evaluation; retain the distinction between actual animal research involvement and incidental background citations.

2026-11-22 amendment (v0.7): User excluded reviews and meta-analyses and restricted inclusion to peer-reviewed research. Confirmed original-research-only eligibility and resolved the previously pending preprint/abstract status as excluded. Full peer-reviewed conference research papers remain eligible; verify publication and peer-review status during screening.
