# TODO импортировать необходимые модули

import csv
import json
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f:
        lines = [line for line in csv.DictReader(f)]

    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(lines, f, indent=4)


if __name__ == '__main__':
    #Для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
