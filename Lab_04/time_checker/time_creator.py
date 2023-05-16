import os
import time


directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "time_file")
# directory = os.path.dirname(os.path.abspath(__file__).replace("creator", "time_file"))
# directory = "../time_checker/time_file/"

def main():
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    filename = os.path.join(directory, f"{current_time}.txt")
    with open(filename, "w") as file:
        file.write(current_time)


if __name__ == "__main__":
    while True:
        main()
        time.sleep(10)