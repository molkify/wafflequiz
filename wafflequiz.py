print('Hello, Welcome to the waffle quiz! this quiz is all about waffles')

ans = input('are you ready to take this quiz? (yes/no)')
score = 0
total_q = 4

if ans.lower() == 'yes!':
    ans = input('1. What do people put on their waffles? ')
    if ans.lower() == 'Syrup':
        score += 1
        print('Correct!')
       else:
        print('Incorrect!')

    ans = input('2. Are waffles flat or in a square shape? ')
    if ans.lower() == 'Square Shape':
        score += 1
        print('Correct!')
       else:
        print('Incorrect!')

ans = input('3. Who made waffles? ')
    if ans.lower() == 'Maximilien Consael':
        score += 1
        print('Correct!')
       else:
        print('Incorrect!')

ans = input('4. Do waffles have a history behind them? ')
    if ans.lower() == 'Yes':
        score += 1
        print('Correct!')
       else:
        print('Incorrect!')

print('Thanks for playing! you got ', score " questions correct")
mark = (score/total_q) * 100

print("Mark:", str (mark) + '%')
print('bye bye!')
