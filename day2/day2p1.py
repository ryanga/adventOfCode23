import re
DEBUG = False 

#the red, green, blue values to check if a game is possible
check_input = {
    "r": 12,
    "g": 13,
    "b": 14
}

def check_game(line_dict):
    total = 0
    for key in line_dict:
        print("checking game: ", key, " with draws: ", line_dict[key])
        if all(check_input["r"] >= draw[0] and check_input["g"] >= draw[1] and check_input["b"] >= draw[2] for draw in line_dict[key]):
            if DEBUG: print("game: ", key, " is possible, adding to previous total of: ", total)
            total += key
    print("total", total)
    return total


#plan of attack
#each line represents a game, and multiple draws from the bag
#split the line by the semicolon for each draw
#check each draw against the input to see if possible
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

