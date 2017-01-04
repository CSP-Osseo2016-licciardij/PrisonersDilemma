####
# Each team's file must define four tokens:

#     move: A function that returns 'c' or 'b'

team_name = 'Balls of Gold'
strategy_name = 'Tit for Tat'
strategy_description = 'Collude for 100 rounds then betray at 101' 
    
def move(my_history, their_history, my_score, their_score):
    
    
    C always until round 100 then switch too B always
    '''Make my move based on the history with this player.