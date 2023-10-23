import csv

high_scores = []

with open("scores.csv", 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    for row in csv_reader:
        player_name, score = row
        score = int(score)
        high_scores.append((player_name, score))

player_scores = {}
for player, score in high_scores:
    if player in player_scores:
        player_scores[player] = max(player_scores[player], score)
    else:
        player_scores[player] = score

sorted_scores = sorted(player_scores.items(), key=lambda x: x[1], reverse=True)

with open("high_scores.csv", 'w', newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Name", "Highscore:"])
    csv_writer.writerows(sorted_scores)
