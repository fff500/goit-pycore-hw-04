import pathlib

def get_cats_info(path):
    try:
        current_dir = pathlib.Path(__file__).parent
        with open(current_dir / path, "r") as file:
            data = file.readlines()

        def map_cats_info(cat):
            cat = cat.strip().split(",")
            return {
                "id": cat[0],
                "name": cat[1],
                "age": cat[2],
            }

        return list(map(map_cats_info, data))

    except FileNotFoundError:
        return "Не вдалося знайти файл з даними"