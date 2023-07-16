"""

Abhmanyu Kidarithil Meethal
PSID:2105385

"""
class Team:
    def __init__(self, team_name='none', team_wins=0, team_losses=0):
        self.team_name = team_name
        self.team_wins = team_wins
        self.team_losses = team_losses

    def get_win_percentage(self):
        if self.team_wins + self.team_losses == 0:
            return 0.0
        win_percentage = self.team_wins / (self.team_wins + self.team_losses)
        return win_percentage
try:
    teamname = input()
    teamwins = int(input())
    teamlosses = int(input())

    team = Team(teamname, teamwins, teamlosses)

    if team.get_win_percentage() >= 0.5:
        print(f"Congratulations, Team {team.team_name} has a winning average!")
    else:
        print(f"Team {team.team_name} has a losing average.")

except:
   print()






