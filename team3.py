####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Leader' # Only 10 chars displayed.
strategy_name = 'Collude most of the time'
strategy_description = 'Always Collude, but if they betray first move, betray. If other player betrays twice in a row, betray, and if they have a lower score, collude no matter what'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    if their_score < my_score:
        return 'c'
    
    if their_history[0] == 'b':
        return 'b'
    
    if their_history[-1] == 'b' and their_history[-2] == 'b':
        return 'b'
    
    else:
        return 'c'
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Betray if their first move was betray
    if test_move(my_history='c',
              their_history='b', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
    
    # Betray if other player has betrayed twice in a row
    if test_move(my_history='cccc',
              their_history='ccbb', 
              my_score=0, 
              their_score=0,
              result='b'):
              print 'Test passed'
              
    # Collude if other player has a lower score, even if they betray
    if test_move(my_history='c',
              their_history='b', 
              my_score=0, 
              their_score=-100,
              result='c'):
              print 'Test passed'
    
    # Always Collude
    if test_move(my_history='c',
              their_history='c', 
              my_score=0, 
              their_score=0,
              result='c'):
              print 'Test passed'