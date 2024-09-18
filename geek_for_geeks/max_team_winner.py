n=int(input("enter number of teams:"))
team_players=[]
for i in range(n):
    team=[]
    for j in range(n):
        team.append(int(input("enter a player strength:")))
    team_players.append(team)
max_player=0
while len(team_players[0])!=0 and len(team_players[1])!=0 and len(team_players[2])!=0:
    if team_players[0][0]>=team_players[1][0] and team_players[0][0]>=team_players[2][0]:
        max_player=0
        del team_players[1][0]
        del team_players[2][0]
    elif team_players[1][0]>=team_players[0][0] and team_players[1][0]>=team_players[2][0]:
        max_player=1
        del team_players[0][0]
        del team_players[2][0]
    elif team_players[2][0]>=team_players[0][0] and team_players[2][0]>=team_players[1][0]:
        max_player=2
        del team_players[0][0]
        del team_players[1][0]
print(max_player)
