"""Create a function that takes the number of wins, draws and losses and
calculates the number of points a football team has obtained so far."""
def num_point(wins,draws, losses):
    win_points=3
    draw_point=1
    losses_point=0
    
    total_marks=wins*win_points+draws*draw_point-losses*losses_point
    return total_marks
team_wins=6
team_draws=5
team_loses=2
result=num_point(team_wins,team_draws,team_loses)

print(result)

    
    