test = ['Что ты несешь?','Ой, да ты заебал.','Даже не удивлен, что ты такое спизданул(']
my_file = open("some.txt", "w")
for x in test:
    my_file.write(x + '\n')

my_file.close()

test2 = []
my_file = open("some.txt", "r")
test2 = my_file.readlines()
print(test2)
print(test)