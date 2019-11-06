

team_name = 'Son' # Only 10 chars displayed.
strategy_name = 'Innocent Crime'
strategy_description = 'Scared wanting to help his friends'
    
def move(my_history, their_history, my_score, their_score):
    from random import uniform
    
    if len(my_history)==0:  #First move, baby!
        if uniform(False,True):
            return 'c'  #I...I won't tell you anything!
        else:
            return 'b' #Please...don't hurt me.
            
    else:   #Not the first move.
        sonC = 0 ; unknownC = 0
        sonB = 0 ; unknownB = 0
        
        for x in range(0,len(my_history)):  #Range of the list.
            if my_history[x] == 'c':
                sonC += 1
            elif my_history[x] == 'b':
                sonB += 1
            if their_history[x] == 'c':
                unknownC += 1
            elif their_history[x] == 'b':
                unknownB += 1           
        #Now we know the count.
        
        if my_score < (their_score/2): return 'b'   #I'm dragging you down with me!
        
        if unknownC < unknownB: #Betrays more often than not. 
            return 'b'  #No! I can't go to jail ; I'll tell you what you want to know!
        elif unknownC > unknownB:   #Colludes more often that not.
            return 'c'  #Whoever you're examining me against: they've got my back and I've got their's!
        else:
            from random import randint
            x = randint(1,2)
            if x ==1:
                return 'c'
            return 'b'


