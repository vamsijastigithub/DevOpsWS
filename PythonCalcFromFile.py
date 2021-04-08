def findnth(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)

calc_from_file = open("calcsourcefile.txt", mode='r') 
calc_from_file_lines = calc_from_file.read().splitlines()
calc_from_file.close()
file_line_count = len(calc_from_file_lines)
print("File Line Count = " + str(file_line_count))
file_line_read = 0
calc_value = 0
while file_line_read < file_line_count:
    file_line_string = calc_from_file_lines[file_line_read]
    first_occurance = findnth(file_line_string,' ',0)
    second_occurance = findnth(file_line_string,' ',1)
    third_occurance = findnth(file_line_string,' ',2)
    operator = file_line_string[first_occurance+1:second_occurance]
    first_num = int(file_line_string[second_occurance+1:third_occurance])
    second_num = int(file_line_string[third_occurance+1])
    calc_line_value = 0
    if operator == '+':
        calc_line_value = first_num+second_num
    elif operator == '-':
        calc_line_value = first_num-second_num
    elif operator == 'x':
        calc_line_value = first_num*second_num
    elif operator == '/':
        calc_line_value = first_num/second_num
    elif operator == '%':
        calc_line_value = first_num%second_num
    calc_value = calc_value + calc_line_value
    file_line_read = file_line_read + 1
print("Calcualted Value from file = " + str(calc_value))