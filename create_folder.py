# import sys
import os

# https://www.geeksforgeeks.org/create-a-directory-in-python/
# https://www.geeksforgeeks.org/create-an-empty-file-using-python/
# https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/

# number = sys.argv[1]
number = input("Create folder for day number: ")

def create_new_challenge_dir(number):
    parent_dir = os.getcwd()
    directory  = 'Day {}'.format(number)
    path = os.path.join(parent_dir, directory)
    file = 'README.md'

    os.mkdir(path)
    print("Directory '% s' created" % directory) 
    open(os.path.join(path, file), 'w')

create_new_challenge_dir(number)