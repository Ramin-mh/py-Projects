import csv
import random
from pathlib import Path

if __name__ == '__main__':
    with open('Reactions_OG.csv', newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    random.shuffle(rows)
    keys_list = list(rows[0].keys())

    for row in rows:
        max_blank = len(keys_list) - 1
        weights = [1 + i*2 for i in range(max_blank + 1)] 
        blank_num = random.choices(range(max_blank + 1), weights=weights, k=1)[0]

        for key in random.sample(keys_list, blank_num):
            row[key] = ""

    written_filestem = 'Reactions_'
    written_filesuffix = '.csv'

    i = 1
    while (
        written_filepath := Path.cwd() / f"{written_filestem}{i}{written_filesuffix}"
    ).exists():
        i += 1

    with open(written_filepath, 'w', newline='', encoding='utf-8-sig') as f:
        fieldnames = rows[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)
