from os import system
from random import randint
from time import sleep

def say(word):
	command = "say " + word
	system(command)

def read_dict(file):
	dic = []
	with open(file) as f:
	    for line in f:
	       dic.append(line.strip('\n'))
	return dic

def dictate(dictionary):
	for i in range(10):
		index = randint(0, len(dictionary) - 1)
		word = dictionary[index];
		english_only = ''.join(x for x in word if ord(x) < 256)
		say(english_only)
		sleep(5)
		print(word)

if __name__ == "__main__":
	dictionary = read_dict("dict.txt")
	dictate(dictionary)