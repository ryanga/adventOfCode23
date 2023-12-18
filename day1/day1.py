DEBUG = True 

def extract_calibration_digits(line):
    digits = [int(d) for d in line if d.isdigit()]
    constructed_digit = int(str(digits[0]) + str(digits[-1]))
    if DEBUG:
        print(line + " found digits: " + str(digits) + " constructed digit: " + str(constructed_digit))
    return constructed_digit

with open("input_day1.txt", "r") as file:
#with open("test_day1.txt", "r") as file:
    sum_constructed_digit = 0
    for line in file:
        sum_constructed_digit += extract_calibration_digits(line)
        #print(line + " constructed digit: " + str(constructed_digit))
print("total sum: " + str(sum_constructed_digit))