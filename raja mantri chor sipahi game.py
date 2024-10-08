#game :D papa i changed it dont mind ur code did not work >:(
player_names=[]
print("Enter the names of 4 players:")
for i in range(4):
    name=input(f"Player {i + 1} name: ")
    player_names.append(name)

scores=[0, 0, 0, 0]

for game in range(10):
    print(f"\nGame {game + 1}:")
    for i in range(4):
        points=int(input(f"Enter points for {player_names[i]}: "))
        scores[i]+=points

print("\nFinal Scores:")
for i in range(4):
    print(f"{player_names[i]}: {scores[i]} points")


highest_score=max(scores)
winner_index=scores.index(highest_score)
print(f"\nThe winner is {player_names[winner_index]}!")

