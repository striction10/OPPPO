from src.models.container import Container

def read_file(name_file):
    container = Container()
    try:
        with open(name_file, "r") as file:
            for line in file:
                if not line or line.startswith("#"):
                    continue
                if line.startswith("ADD"):
                    json_data = line[3:].strip()
                    container.add(json_data)
                if line.startswith("REM"):
                    condition = line[3:].strip()
                    container.rem(condition)
                if line.startswith("PRINT"):
                    container.print()
    except FileNotFoundError:
        print("Файл не найден!")

def main():
    name_file = input("Введите путь к файлу: ")
    read_file(name_file)

if __name__ == '__main__':
    main()