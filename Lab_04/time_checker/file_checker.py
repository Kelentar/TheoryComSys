import glob
import os
import time

directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "time_file")
# directory = os.path.dirname(os.path.abspath(__file__).replace("file_checker", "time_file")) + '\\'
# directory = "../time_checker/time_file/"

def all_directory():
    print("Файли у каталозі:")
    files = os.listdir(directory)
    for file_name in files:
        with open(os.path.join(directory, file_name), 'r') as file:
            print(f"{file_name}: \n{file.read()}")


def get_latest_file():
    files = glob.glob(os.path.join(directory, "*"))
    files_sorted = sorted(files, key=os.path.getctime, reverse=True)
    if files_sorted:
        return files_sorted[0]
    else:
        return None


def main():
    latest_file = get_latest_file()
    if latest_file:
        with open(latest_file, "r") as file:
            latest_file_name = latest_file.split("/")[-1]
            print(f"{latest_file_name}: \n{file.read()}")


if __name__ == "__main__":
    all_directory()
    while True:
        main()
        time.sleep(10)