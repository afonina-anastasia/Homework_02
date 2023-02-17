import csv

def sum_of_digits(number_from_csv):
    new_list = []
    while True:
        if number_from_csv.isdigit() and (1 <= len(number_from_csv) <= 10):
            number_from_csv = list(number_from_csv)
            new_list = [int(i) for i in number_from_csv]
            # print(number_from_csv)
            #print(new_list)
            total = sum(new_list)
            return f'{total}'


        elif not number_from_csv.isdigit():
            return "Enter three integers without spaces!"

        elif len(number_from_csv) > 10:
            return "vvedi chislo dlinoi do 10!"


        else:
            break


# sum_of_digits(str())

with open("test_numbers.csv", 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        for number in line:
            print(f' for numbers {line}, the sum  is equal to : {sum_of_digits(number)}')