import pathlib

def total_salary(path):
    try:
        current_dir = pathlib.Path(__file__).parent
        with open(current_dir / path, "r") as file:
            data = file.readlines()

        salaries = list(map(lambda x: int(x.strip().split(",")[1]), data))
        total = sum(salaries)
        average = total / len(salaries)

        return (total, average)
    except FileNotFoundError:
        return "Не вдалося знайти файл з даними"