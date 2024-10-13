 # ReadingASM

# Importing system module
import sys

# Make a variable for the out to be a file
OUTPUT = "TranslatingAdd.txt"

# Make a list for the translated lines
translated_instructions = []

# Check the fiie with open while taking care of the detials
# use py .\ReadASM.py .\MaxL.asm or file name in the Terminal

# Using with to work with properly handle resources need to use the open function to read a 
# sys module arguement and call the outcome as file_input
with open(sys.argv[1], "r") as file_input:
    # Create a variable call lines to be a list of each line in the file_input
    lines = file_input.readlines()

# Have a dictionary to store the predefined labels and their addresses, along with adding new labels and variables with address.
symbol_table = {"SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
        "R0": 0, "R1": 1, "R2": 2, "R3": 3, "R4": 4, "R5": 5, "R6": 6, "R7": 7,
        "R8": 8, "R9": 9, "R10": 10, "R11": 11, "R12": 12, "R13": 13, "R14": 14, "R15": 15,
        "SCREEN": 16384, "KBD": 24576}

# Have a dictionary to store the predefined behavior of Destination, Comparsion and Jump!

comparsion = {"0": "0101010", "1": "011111", "-1": "0111010", "D":"0001100", 
            "A": "0110000", "!D": "0001101", "!A":"0110001", "-D": "0001111", "-A": "0110011",
            "D+1": "0011111",  "A+1":"0110111", "D-1":"0001110",
            "A-1": "0110010", "M-1": "1110010", "D+A":"0000010", "D-A": "0010011",
            "A-D": "0000111", "D&A": "0000000", "D|A":"0010101", "M": "1110000",
            "!M": "1110001", "-M": "1110011", "M+1": "1110111", "M-1": "110010","D+M": "1000010",
            "D-M": "1010011", "M-D": "1000111", "D&M": "1000000", "D|M": "1010101", "M+D": "1000010"}

destination = {"null": "000",
               "M": "001", 
               "D": "010",
               "DM":"011",
               "A":"100",
               "AM":"101",
               "AD":"110",
               "ADM":"111"}

jump = {"null": "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE":"101",
        "JLE":"110",
        "JMP":"111"}


# For after the first parse of the lines
first_parser = []

# The Rom Address 
rom_address = 0

# The Ram Address
RAM_variable_address = 16

# For the first run, check for labels=
for line in lines:
    # For each line, make a striped down version of itself. ie remove the spaces!
    striped_line = line.strip()
    # Check if the line is a comment or extra space 
    # if so, then continue the loop and don't do anything 
    # else if the line is a label, then assign it a rom_address value
    # else, add the line to first_parser and increment the rom_address by 1
    if len(striped_line) > 0:
        if striped_line[0] == "/" and striped_line[1] == "/":
            # Continue: Let us move forward in the loop!
            continue
        elif striped_line[0] == "(" and striped_line[-1] == ")":
            label = striped_line[1:-1]
            symbol_table[label] = rom_address
        else:
            first_parser.append(striped_line)
            rom_address += 1
    else:
        continue

# For the second run, start translating the lines to binary from the first_parser!
for line in first_parser:
    # If first character in a line is @, then do A-Instruction
    # Else treat the line as a C-Instruction
    if line[0] == "@":
        print("An A instruction!")
        symbol = line[1:]
        if symbol.isdigit():
            address = int(symbol)
        else: 
            if symbol not in symbol_table:
                symbol_table[symbol] = RAM_variable_address
                RAM_variable_address += 1
            address = symbol_table[symbol]
        # Convert the address to binary
        binary_form = format(address, '016b')
        # Append the binary line to the list of translated instructions
        translated_instructions.append(binary_form)
        print(binary_form)         
    else:
        print("A C instruction!")
        # d = destination
        # c = comparsions
        # j = jumps

        # Check if there is an equal, assign a value
        if "=" in line:
            d, c = line.split("=")
            print(d + " " + c)
            j = "null"
        # Check if there is an semicolon, jump statement
        elif ";" in line:
            d = "null"
            c, j = line.split(";")
            print(c + " " + j)
        
        binary_form = "111" + comparsion[c] + destination[d] + jump[j]
        translated_instructions.append(binary_form)




# Using with to handle resources to write a file using the name of OUTPUT!
with open(OUTPUT, "w") as file_output:
    for line in translated_instructions:
        file_output.write(line + "\n")


        