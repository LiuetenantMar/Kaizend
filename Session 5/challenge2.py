from time import sleep
import random

def get_random_number():
	return random.randint(1, 5)

def delay(seconds):
    print(f"Sleeping for {seconds} second(s)")
    sleep(seconds)

def main():
    for x in range(5):
    	print(x)
    	# print('a')
    	delay(seconds = get_random_number())
    	# print('b')

if __name__ == "__main__":
    main()