'''
Practice
1. Write a program that generate 26 text files named
A.txt, B.txt, and so on up to Z.txt.To each file append a
random number between 1 and 100. Create a summary file
(summary.txt) that contains name of the file and number in
that file:
A.txt: 67
B.txt: 12
...
Z.txt: 98
'''
import csv
import string
import random as rd

file_names = []
for letter in string.ascii_uppercase:
    new_file = letter+'.txt'
    file_names.append(new_file)

    with open(new_file, 'w') as file:
        file.write(str(rd.randint(1, 100)))

file_txt = []
for item in file_names:
    line = open(item, 'r')
    file_txt.append(line.read())

index = 0
with open('summary.txt', 'w') as f:
    for line in file_txt:
        f.write(f"\n {file_names[index]} : {file_txt[index]}")
        index = index + 1

'''
2. Create file with some content. As example you can take this one
Тому що ніколи тебе не вирвеш,
ніколи не забереш,
тому що вся твоя свобода
складається з меж,
тому що в тебе немає
жодного вантажу,
тому що ти ніколи не слухаєш,
оскільки знаєш i так,
що я скажу,
Create second file and copy content of the first file to the second
file in upper case.
'''

with open('poem.txt', 'r+') as poem, open('upper_poem.txt', 'a') as up_poem:
    poem.write('''Тому що ніколи тебе не вирвеш,
ніколи не забереш,
тому що вся твоя свобода
складається з меж,
тому що в тебе немає
жодного вантажу,
тому що ти ніколи не слухаєш,
оскільки знаєш i так,
що я скажу
''')
    for line in poem:
        up_poem.write(line.upper())
'''
3.Write a program that will simulate user score in a game.
Create a list with 5 player's names. After that simulate
100 games for each player. As a result of the game create
a list with player's name and his score (0-1000 range).
And save it to a CSV file. File should looks like this:

Player name, Score
Josh, 56
Luke, 784
Kate, 90
Mark, 125
Mary, 877
Josh, 345
...

'''

games = 100
names = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']
results = [dict(zip((name,), [rd.randint(0, 1000)])) for score in range(games) for name in names]

header_list = ['Player name', 'Score']
with open('results.csv', 'w', newline='\n') as file:
    writer = csv.DictWriter(file, delimiter=',', fieldnames=header_list)
    writer.writeheader()

    for i in results:
        for key in i.keys():
            file.write("%s,%s\n" % (key, i[key]))

'''
4. Write a script that reads the data from previous CSV file
and creates a new file called high_scores.csv where each row
contains the player name and their highest score. Final score
should sorted by descending of highest score

The output CSV file should look like this:

Player name, Highest score
Kate, 907
Mary, 897
Luke, 784
Mark, 725
Josh, 345
#sort_list = sorted(reader, reverse=True)
'''


with open('results.csv', mode='r') as file_1, open('high_scores.csv', mode='w') as file_2:
    writer = csv.writer(file_2, delimiter=',')
    reader = csv.reader(file_1, delimiter=',')
    sorted_list = sorted(list(reader)[1:], key=lambda row: ((row[0]), int(row[1])))

    index = [99, 199, 299, 399, 499]
    high_score = sorted([x for x in sorted_list if sorted_list.index(x) in index], key=lambda row: (int(row[1])), reverse=True)
    print(high_score)
    writer.writerow(['Player name', 'Highest score'])
    for score in high_score:
        writer.writerow(score)

# Task 4. Считать файл hw.csv и посчитать средний рост, средний вес
#  в см и кг соответственно
