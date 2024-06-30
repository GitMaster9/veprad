import re

# Open the input file and read the content
with open('merlin_dict.txt', 'r') as file:
    lines = file.readlines()

# Process each line
modified_lines = []
for line in lines:
    columns = re.split(r'\t+', line.strip())  # Split the line into columns based on 1 to 3 tabs
    if len(columns) == 2:  # Ensure there are exactly 2 columns
        first_col = columns[0]
        second_col = columns[1]
        new_col = f'[{first_col}]'
        modified_line = f'{first_col}\t{new_col}\t{second_col}'
        modified_lines.append(modified_line)

# Write the modified content to a new file
with open('converted_dict.txt', 'w') as file:
    for modified_line in modified_lines:
        file.write(modified_line + '\n')
