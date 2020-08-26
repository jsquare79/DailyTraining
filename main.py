# Daily Training App
import random

print("Opening file")
training_list = open("item_list.txt", "r")

print("Reading the file into memory")
file = training_list.readlines()
print("Reading list length")
list_length = len(file)
print("The file contains", list_length, "lines.")

'''
print("File contents:")
for line in file:
    print(line)
'''

num_topics = int(input("How many topics would you like to learn? "))

print("Choosing %d random topics to learn" % num_topics)
input("PRESS ENTER TO START LEARNING")


for i in range(1, num_topics + 1):
    random_pick = random.randrange(1, list_length + 1)
    print("Your random pick is", random_pick)
    # print("Pick %d is" % i, random_pick)

    print("EXERCISE:", file[random_pick - 1])
    input("Do the exercise and press ENTER to continue")



training_list.close()

'''
CODE BELOW HERE WAS FOR TESTING
# Open a file to store training topics, create if does not exist
training_list = open("training_list.txt", "w+")

# write some text lines to the file
for i in range(10):
    training_list.write("This is line %d\r\n" % (i + 1))

# close file
training_list.close()

# open file again, for append, using new variable
training_list2 = open("training_list.txt", "a+")

# write some more text
for i in range(2):
    training_list2.write("Appended line %d\r\n" % (i + 1))

training_list2.close()

# read that file's lines
training_list3 = open("training_list.txt", "r")

print("#######READING THE FILE#######")

if training_list3.mode == 'r':
    contents = training_list3.read()
    print(contents)

training_list3.close()

# single line reading of file

training_list4 = open("training_list.txt", "r")

print("#######READING LINES#######")

f1 = training_list4.readlines()
for x in f1:
    print(x)

training_list4.close()
'''