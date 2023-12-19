from functools import reduce
import operator
import re
DEBUG = True 

#now need to find the lowest number of cubes of each color that would make the game possible
#can determine this by finding the largest # of each color across all draws

def check_game(line_dict):
    total = 0
    for key in line_dict:
        print("checking game: ", key, " with draws: ", line_dict[key])
        max_values = [0, 0, 0]  # Initialize max values at positions 0, 1, and 2
        for draw in line_dict[key]:
            max_values[0] = max(max_values[0], draw[0])  # Update max value at position 0
            max_values[1] = max(max_values[1], draw[1])  # Update max value at position 1
            max_values[2] = max(max_values[2], draw[2])  # Update max value at position 2
        print("for game: ", key, " max values: ", max_values, " which is a power of: ", reduce(operator.mul, max_values, 1))  
        total += reduce(operator.mul, max_values, 1)  
    print("total: ", total)
    return total

# the final output needs to be 
# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.


with open("input_d2p1.txt", "r") as file:
#with open("test_d2p1.txt", "r") as file:
    line_dict = {}
    for line in file:
        if DEBUG: print(line)
        # Split each line into a dictionary
        line_parts = line.strip().split(":")
        gn = re.search(r"(\d+)", line_parts[0])
        game_num = int(gn.group(1))
        values = line_parts[1].split(";")
        line_dict[game_num] = [] #initialize the list
        for val in values:
            # Use regular expressions to extract the integer before "green", "red", or "blue"
            red_match = re.search(r"(\d+)\s*red", val)
            if red_match and DEBUG:
                print("red: ", int(red_match.group(1)))
            green_match = re.search(r"(\d+)\s*green", val)
            if green_match and DEBUG:
                print("green: ", int(green_match.group(1)))
            blue_match = re.search(r"(\d+)\s*blue", val)
            if blue_match and DEBUG:
                print("blue: ", int(blue_match.group(1)))
            
            red = int(red_match.group(1)) if red_match else 0
            green = int(green_match.group(1)) if green_match else 0
            blue = int(blue_match.group(1)) if blue_match else 0

            line_dict[game_num].append([red,green,blue])
        #at this point we have a dictionary of each game, and then one or more arrays of each draws 
    check_game(line_dict)

