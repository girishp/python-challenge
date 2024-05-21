import csv
from collections import Counter

votes = {}
total_votes = 0

with open("./PyPoll/Resources/election_data.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)

    candidate_selections = [row['Candidate'] for row in csv_reader]
    total_votes = len(candidate_selections)
    votes = Counter(candidate_selections)

with open("./PyPoll/analysis/results.txt", "w") as file:
    line = f"Election Results"
    print(line)
    file.write(line + '\n')
    line = f"-------------------------"
    print(line)
    file.write(line + '\n')
    line = f"Total Votes: {total_votes}"
    print(line)
    file.write(line + '\n')
    line = f"-------------------------"
    print(line)
    file.write(line + '\n')
    
    winner = ""
    winning_votes = 0
    for candidate,num_votes in votes.items():
        percentage = num_votes / total_votes * 100
        percentage = round(percentage, 3)
        line = f"{candidate}: {percentage}% ({num_votes})"
        print(line)
        file.write(line + '\n')
        if num_votes > winning_votes:
            winning_votes = num_votes
            winner = candidate

    line = f"-------------------------"
    print(line)
    file.write(line + '\n')
    line = f"Winner: {winner}"
    print(line)
    file.write(line + '\n')
    line = f"-------------------------"
    print(line)
    file.write(line + '\n')
