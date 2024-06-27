import random
import csv

# Task 1 
def generate_files():
    with open('summary.txt', 'w') as summary_file:
        for char in range(ord('A'), ord('Z') + 1):
            file_name = chr(char) + '.txt'
            random_number = random.randint(1, 100)
            with open(file_name, 'w') as file:
                file.write(str(random_number))
            summary_file.write(f"{file_name}: {random_number}\n")
            print(f"{file_name} with number {random_number}")
    print(f'Summary file create success')
          
generate_files()


# Task 2 
content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'

with open('file1.txt', 'w') as f:
    f.write(content)

with open('file1.txt') as file_1, open('file2.txt', 'w') as file_2:
    upper_context = file_1.read().upper()
    file_2.write(upper_context)
    
# Task 3
def simulate_game(players, rounds):
    players_scores = []   
    for player in players:
        for _ in range(rounds):
            score = random.randint(0, 1000)
            players_scores.append((player, score))          
    return players_scores
 
 
def save_scores_to_csv(scores, filename):
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = ['Player name', 'Score']
        writer = csv.writer(csv_file)
        writer.writerow(fieldnames)
        writer.writerows(scores)
    print(f'Results save in {filename}')

    
def main():
    players = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']
    rounds = 100
    scores = simulate_game(players, rounds)
    save_scores_to_csv(scores, 'game_scores.csv')
    
main()

# Task 4
def process_scores(input_file, output_file):
    scores = {}

    with open(input_file) as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            player_name = row[0]
            score = int(row[1])
            if player_name in scores:
                if score > scores[player_name]:
                    scores[player_name] = score
            else:
                scores[player_name] = score

    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Player name', 'Highest score'])
        for player, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([player, score])

    print(f"High scores saved to {output_file}")


input_file = 'game_scores.csv'
output_file = 'high_scores.csv'
process_scores(input_file, output_file)
