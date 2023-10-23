import random
import csv


players = ["Josh", "Luke", "Kate", "Mark", "Mary"]
results = []

for _ in range(100):
    for player in players:
        score = random.randint(0, 1000)
        results.append((player, score))

with open("scores.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Name", "Score:"])
    csv_writer.writerows(results)
