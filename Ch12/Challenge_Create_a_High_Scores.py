#%%
from pathlib import Path
import csv

new_path = Path.home()/'high_scores.csv'
path = Path("C:\Study\Coding\Real_Python Basic\Ch12\scores.csv")

# %%
data = []
def process_row(row):
    row['score'] = int(row['score'])
    return row

with path.open(mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(process_row(row))
# %%
highest_scores = {}
for enter in data:
    name = enter['name']
    score = enter['score']
    if name not in highest_scores or score > highest_scores[name]:
        highest_scores[name] = score

result = [{'name': name, 'score': score} for name, score in highest_scores.items()]

# %%
with new_path.open(mode='w',encoding='utf-8',newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name','score'])
    writer.writeheader()
    writer.writerows(result)
# %%
