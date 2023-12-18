DEBUG = True 
#like day 1 but look for spelled out words

number_lookup = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}

def extract_calibration_digits(line):
    digits = []
    line = line.lower()
    for i in range(len(line)):
        #if its a digit, append to the array
        if line[i].isdigit(): 
            digits.append(int(line[i]))
        else:
            for num, dig in number_lookup.items():
                if num in line[i:i+len(num)]:
                    digits.append(dig)
                    continue

    constructed_digit = int(str(digits[0]) + str(digits[-1]))
    if DEBUG:
        print(line + " found digits: " + str(digits) + " constructed digit: " + str(constructed_digit))
    return constructed_digit

with open("input_day1.txt", "r") as file:
#with open("test_day1p2.txt", "r") as file:
    sum_constructed_digit = 0
    for line in file:
        sum_constructed_digit += extract_calibration_digits(line)
        #print(line + " constructed digit: " + str(constructed_digit))
print("total sum: " + str(sum_constructed_digit))