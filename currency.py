
money=input('Enter money :')
reversed_money=money[-3:][::-1]+','
for i in range(3,len(money),2):
    reversed_money+= money[::-1][i:i+2]+','

Indian_money=reversed_money[::-1][1:]

print(Indian_money)

# print(indian_currency[::-1])
