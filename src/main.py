"""Start."""
from src.models.container import Container

class Processor:
    """Processor class."""

    def __init__(self):
        """Constructor class."""
        self.container = Container()

    def get_container(self) -> Container:
        """Get the container instance."""
        return self.container

    def read_file(self, name_file: str) -> None:
        """Read the name_file file."""
        try:
            with open(name_file, "r", encoding="utf-8") as file:
                for line in file:
                    if not line or line.startswith("#"):
                        continue
                    if line.startswith("ADD"):
                        json_data = line[3:].strip()
                        self.container.add(json_data)
                    if line.startswith("REM"):
                        condition = line[3:].strip()
                        self.container.rem(condition)
                    if line.startswith("PRINT"):
                        self.container.print()
        except FileNotFoundError:
            print("Файл не найден!")

def main() -> None:
    """Main function."""
    name_file = input("Введите путь к файлу: ")
    processor = Processor()
    processor.read_file(name_file)

if __name__ == '__main__':
    main()
