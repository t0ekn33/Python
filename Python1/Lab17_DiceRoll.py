"""
Lab 17 - Dice Roll
Use the randrange function in the random module to simulate
rolling a pair of dice. Simulate 10,000 rolls and calculate the
percentage of the rolls that are sevens and the percentage of the
rolls that are twos. Express your results to one decimal place.
Mathematically, the percentage of sevens will be 16.7% and the
twos will be 2.8%. Your answers should close to these values.
Use Python Help or Pydoc3 to determine what the difference is
between the randrange and randint functions in the Random
module.
"""

from random import randrange as rr
cnt = 0
seven = 0
two = 0

for rolls in range(1,10000):
    roll = rr(1,7) + rr(1,7)
    #print(roll)
    cnt += 1
    if(roll == 7):
        seven += 1
        avg7 = seven / cnt * 100
    if(roll == 2):
        two += 1
        avg2 = two / cnt * 100



        
print('{0:.1f}%'.format(avg7))
print('{0:.1f}%'.format(avg2))

