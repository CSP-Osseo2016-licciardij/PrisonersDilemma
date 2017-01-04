
team_name = 'Bjorgolf'
strategy_name = 'BestComputetrColluders'
strategy_description = '''Strategy Axe'''
    
def move(my_history, their_history, my_score, their_score):
   
    
    if 'b' in their_history:
        return 'b'
    else:
        return 'c'
    
