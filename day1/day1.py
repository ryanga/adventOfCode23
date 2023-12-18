with open("input_day1.txt", "r") as file:
    sum_constructed_digit = 0
    for line in file:
        line = file.readline()
        digits = [int(d) for d in line if d.isdigit()]
        constructed_digit = int(str(digits[0]) + str(digits[-1]))
        sum_constructed_digit += constructed_digit
        print(line + " found digits: " + str(digits) + " constructed digit: " + str(constructed_digit))
    print(sum_constructed_digit)