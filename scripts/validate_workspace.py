"""Structural validation, not a methodological audit."""
from pathlib import Path
import csv
import sys
root = Path(__file__).resolve().parents[1]
errors = []
tables = {}
for path in sorted(root.rglob('*.csv')):
    with path.open(newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f))
    name = str(path.relative_to(root))
    if not rows or len(rows[0]) != len(set(rows[0])):
        errors.append(f'{name}: missing or duplicate headers')
        continue
    for line, row in enumerate(rows[1:], 2):
        if len(row) != len(rows[0]):
            errors.append(f'{name}:{line}: incorrect column count')
    tables[name] = [dict(zip(rows[0], row)) for row in rows[1:]]
keys = {'02_search/search_runs.csv':'search_id', '03_records/records.csv':'record_id', '04_screening/decisions.csv':'decision_id', '04_screening/consensus.csv':'consensus_id', '05_extraction/data_items.csv':'extraction_id', '05_extraction/variable_dictionary.csv':'variable_id'}
for name, key in keys.items():
    values = [row.get(key, '') for row in tables.get(name, [])]
    if any(not v for v in values) or len(values) != len(set(values)):
        errors.append(f'{name}: blank or duplicate {key}')
for source, field, target, key in [
    ('03_records/records.csv','search_id','02_search/search_runs.csv','search_id'),
    ('04_screening/decisions.csv','record_id','03_records/records.csv','record_id'),
    ('05_extraction/data_items.csv','variable_id','05_extraction/variable_dictionary.csv','variable_id')]:
    allowed = {row.get(key) for row in tables.get(target, [])}
    for row in tables.get(source, []):
        if row.get(field) not in allowed:
            errors.append(f'{source}: unresolved {field}')
items = tables.get('07_reporting/prisma_scr_tracker.csv', [])
if [row.get('item') for row in items] != [str(n) for n in range(1, 23)]:
    errors.append('PRISMA-ScR tracker must contain items 1-22')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(tables)} CSV files; structure, selected identifiers and links checked.')
print('Empty ledgers are setup templates, not completed review work.')

