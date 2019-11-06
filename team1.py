import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Gamblers' # Only 10 chars displayed.
strategy_name = 'Statistical Logic'
strategy_description = "Bases off of other players' moves"

def move2(myHistory, theirHistory, myScore, theirScore):
    ''' Arguments accepted: myHistory, theirHistory are strings.
    myScore, theirScore are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    Time = 0
    if len(myHistory)==0:
        Time = 8
    else:
        Time = random.randint(1,24)
    if len(myHistory) == 0:
        return 'b' 
    else:
        if Time > 12:
            return 'b'
        elif theirHistory[len(theirHistory)-1] == 'b':
            return 'b'
        elif myScore < theirScore + 150:
            return 'b'
        else:
            return 'c'
            
def move(myHistory, theirHistory, myScore, theirScore):
    if len(myHistory)==0:
        return 'b'
    elif theirHistory[-1]=='c' and theirHistory[-2]:
        return 'c'
    elif len(myHistory)==1 and theirHistory[-1]=='c':
        if random.randint(1,101)<=50:
            return 'c'
        else:
            return 'b'
    else:
        if theirHistory[-1]=='b' and theirHistory[-2]=='b':
            return 'b'
        elif theirHistory[-1]=='c' and myHistory[-1]=='c':
            if random.randint(1,101)>=15:
                return 'c'
            else: return 'b'
        elif theirHistory[-1]=='b' and myHistory[-1]=='b':
            return 'b'
        elif theirHistory[-1]=='b' and myHistory[-1]=='c':
            return 'b'
        elif theirHistory[-1]=='c' and myHistory[-1]=='b':
            if random.randint(1,101)<=25:
                return 'c'
            else:
                return 'b'
        
        
    
    
    

    # myHistory: a string with one letter (c or b) per round that has been played with this opponent.
    # theirHistory: a string of the same length as history, possibly empty. 
    # The first round between these two players is myHistory[0] and theirHistory[0].
    # The most recent round is myHistory[-1] and theirHistory[-1].
    
    # Analyze myHistory and theirHistory and/or myScore and theirScore.
    # Decide whether to return 'c' or 'b'.
    
    return 'b'

    
def test_move(myHistory, theirHistory, myScore, theirScore, result):
    '''calls move(myHistory, theirHistory, myScore, theirScore)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(myHistory, theirHistory, myScore, theirScore)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+myHistory+"'", "'"+theirHistory+"'",
                       str(myScore), str(theirScore)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(myHistory='bbb',
              theirHistory='bbb', 
              myScore=155,
              theirScore=0,
              result='b'):
         print 'Test passed'
    if test_move(myHistory='bc',
              theirHistory='cc', 
              myScore=155,
              theirScore=0,
              result='c'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    if test_move(myHistory='bbb',
              theirHistory='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              myScore=0, 
              theirScore=0,
              result='c'):
        print 'Test passed'