#add required assignment header comment lines here

#Global Constants 

#MAIN-------------------------------------------------------------------------------------------
def main():
    #Test data

    #Display company header (by calling function 1)
    display_company_header()
    
    #Get game info
    print()
    print(" "*6,"Enter game information:")
    print(" "*6,'-'*31)
    
    team_name1 = str(input("          Team 1 Name:    "))
    team_score1 = int(input("          Team 1 Score:   "))
    print()
    team_name2 = str(input("          Team 2 Name:    "))
    team_score2 = int(input("          Team 2 Score:   "))
    
    print("\n")

        
    #Get team stats
    print(" "*6,"Enter team statistics:")
    print(" "*6,'-'*31)
    
    team1_shots_att = int(input("          Team 1 Shots attempted: "))
    team1_shots_made = int(input("          Team 1 Shots made: "))
    
    print()
    
    team2_shots_att = int(input("          Team 2 Shots attempted: "))
    team2_shots_made = int(input("          Team 2 Shots made: "))
    
    print("\n")

    
    
    
    #Display scoreboard (by calling functions2)
    display_scoreboard(team_name1, team_name2, team_score1, team_score2)
    
    #Validate additional user input

    #Display game analysis (by calling function 3)
    game_analysis(team_name1, team_name2, team_score1, team_score2, team1_shots_att, team1_shots_made, team2_shots_att, team2_shots_made)

#FUNCTIONS--------------------------------------------------------------------------------------

#FN1
def display_company_header():
    print()
    print('*-'*31)
    print(f'{"VSPN - Victorino Sports Network":^61}')
    print('*-'*31)
    
    

#FN2 
def display_scoreboard(team_name1, team_name2, team_score1, team_score2):   
    print(' '*5,'*'*50)
    print(" "*1,f'{ "FINAL SCORE":^50}')
    print(f'{team_name1:^25} {team_name2:^25}')
    print(f'{"-"*10:^26}{"vs"}{"-"*9:^22}')
    print(f'{team_score1:^25} {team_score2:^25}')
    print()
    print('     ', '*'*50)
    
    print()
    
    
#FN3
def game_analysis(team_name1, team_name2, team_score1, team_score2, team1_shots_att, team1_shots_made, team2_shots_att, team2_shots_made):
    if team_score1 >= team_score2:
        diff_in_score = team_score1 - team_score2
        win = team_name1
    elif team_score1 < team_score2:
        diff_in_score = team_score2 - team_score1
        win = team_name2
        
    
    
    shooting_accuracy_team1 = (team1_shots_made/team1_shots_att)*100
    shooting_accuracy_team2 = (team2_shots_made/team2_shots_att)*100
    
    if shooting_accuracy_team1 > shooting_accuracy_team2:
        more_accurate = team_name1
        diff_in_accuracy = shooting_accuracy_team1 - shooting_accuracy_team2
    else:
        more_accurate = team_name2
        diff_in_accuracy = shooting_accuracy_team2 - shooting_accuracy_team1
    print()
    print(" "*5,'-'*50)
    print(" "*5,f'{"GAME ANALYSIS":^45}')
    print(" "*5,'-'*50)
    
    print()
    print(" "*7, ">>> ",win," win by ", diff_in_score, "points!")
    
    print()
    print(" "*14, "Shooting Accuracy")
    print(" "*16, f'{team_name1:8s} : {shooting_accuracy_team1:6,.2f}' f'  ({team1_shots_made}'"/"f'{team1_shots_att})')
    print(" "*16, f'{team_name2:8s}: {shooting_accuracy_team2:6,.2f}' f'  ({team2_shots_made}'"/"f'{team2_shots_att})')
    
    print()
    print(" "*7, ">>> ",more_accurate," more accurate by "f'{diff_in_accuracy:5,.2f}'"%")
    
    print()
    print(" "*5,f'{"GOOD GAME!":^50s}')
    print(" "*5,'-'*50)
       
main()
