Test_case=int(input('Enter the number of test cases : '))
assert 1<=Test_case<=105,'Test cases can not exceed 105'
start=0
player_count=0
while start!=Test_case:
    minimum_dead_players=0
    Total_players=int(input('Enter the total no of players : '))
    player_count+=Total_players
    if 5<=player_count<=105:
        pass
    else:
        print('Total number of players must be between 5 and 105')
        continue
    Gi_Hun_Ali_height=int(input('Enter the Heights  of Gi-Hun and Ali : '))
    if 1<=Total_players<=105:
        if 1<=Gi_Hun_Ali_height<=106:
            height=list(map(float,input('Enter the height of each player seperated by space: ').split()))
            if len(height)==Total_players:
                for i in height:
                    if 1<=i<=106:
                        if i > Gi_Hun_Ali_height:
                            minimum_dead_players+=1
                        
                    else:
                        print('Height can not exceed 106')
                        continue
            else:
                print('Incorrect number of total players')
                continue
        else:
            print('Height cannot exceed 106')
            continue
    else:
        print('Total players cannot exceed 105')
        continue
    print('Minimum number of players who need to get shot are : ',minimum_dead_players)
    start+=1





         

