import csv


def sum_of_digits(number_from_csv: int):
    if (
        not isinstance(number_from_csv, int)
        and (1 > len(str(number_from_csv)) > 10)
        and number_from_csv > 0
    ):
        return "it is not an integer or an incorrect number of digits."

    else:
        digits = [int(number) for number in str(number_from_csv)]
        return sum(digits)


with open("test_numbers.csv", "r") as f:
    reader = csv.reader(f)
    for line in reader:
        for number in line:
            print(
                f" for numbers {line}, the sum  is equal to : {sum_of_digits(int(number))}"
            )
