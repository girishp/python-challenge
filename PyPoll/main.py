import csv

votes = {}
total_votes = 0

with open("./PyPoll/Resources/election_data.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        total_votes = total_votes + 1
        candidate = row['Candidate']
        if(candidate in votes):
            votes[candidate] += 1
        else:
            votes[candidate] = 1


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
