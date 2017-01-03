####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = '1==1'
strategy_name = 'Working Together'
strategy_description = 'Collude until betrayed unless they collude twice. Betray when 20 rounds have ended.'
    
def move(my_history, their_history, my_score, their_score):
    if len(their_history) <= 1:
        return 'c'
    elif their_history[-1] == 'c' and their_history[-2] == 'c':
        return 'c'  
    elif 'b' in their_history:
        return 'b'   
    elif  len(their_history)>20: 
        return 'b'         
    else:
        return 'c' 