import sys
from pathlib import Path
from colorama import Fore

def main():
    def print_directory(directory):
        counter = 1
        for path in directory.iterdir():
            if path.is_dir():
                counter += 1
                print(f"{Fore.BLUE}{path.name}/")
                print_directory(path)
            else: print(f"{Fore.GREEN}{"    " * counter}{path.name}")

    try:
        directory = Path(sys.argv[1])
        print_directory(directory)
    except FileNotFoundError:
        return "Не вдалося знайти файл з даними"

if __name__ == "__main__":
    main()