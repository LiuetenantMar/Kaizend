from time import sleep

def delay(seconds):
    print(f"Sleeping for {seconds} second(s)")
    sleep(seconds)

def main():
    for x in range(5):
    	print(x)
    	# print('a')
    	delay(seconds=2)
    	# print('b')

if __name__ == "__main__":
    main()