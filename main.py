# Daily Training App
import random

print("WELCOME TO THE DAILY TRAINING PICKER 9000!!!")
# Opening file
training_list = open("item_list.txt", "r")

# Reading the file into memory
file = training_list.readlines()
# Reading list length
list_length = len(file)
# print("The file contains", list_length, "lines.")

num_topics = int(input("How many topics would you like to learn? (1-%d" % list_length + ") "))

if (num_topics <= list_length):
    print("Choosing %d random topics to learn" % num_topics)
    input("PRESS ENTER TO START LEARNING")

    for i in range(1, num_topics + 1):
        print("%d topics to go" % num_topics)
        print("The file contains", list_length, "lines.")
        #print(file)
        random_pick = random.randrange(1, list_length + 1)
        #print("Your random pick is", random_pick)
        # print("Pick %d is" % i, random_pick)
        current_item = file.pop(random_pick - 1)
        print("EXERCISE %d:" % i, current_item)
        # print("EXERCISE %d:" % i, file[random_pick - 1])
        input("Do the exercise and press ENTER to continue\n")
        num_topics -= 1
        list_length -= 1

    print("Thanks for training today!")
    print("NOW EXITING PROGRAM")

    training_list.close()

else:
    print("The training list doesn't include that many topics. Choose again.")
