def process_word(word):
    special_words = {
        '!ENTER': 'sil',
        '!EXIT': 'sil',
        '<sil>': 'sil',
        '<uzdah>': 'uzdah',
        '<papir>': 'papir',
        '<glazba>': 'glazba',
    }

    for old, new in special_words.items():
        if word == old:
            return new

    # Replace special characters if needed
    # For example, replace '@' with 'at' and '&' with 'and'
    replacements = {
        '{': 'S',
        '~': 'C',
        '^': 'cc',
        '`': 'Z',
        '}': 'dz',
    }

    # Separate every letter by a space
    spaced_word = ' '.join(list(word))
    
    for old, new in replacements.items():
        spaced_word = spaced_word.replace(old, new)
    
    return spaced_word

input_file = 'wlist.txt'
output_file = 'monophones1.txt'

processed_words = []
with open(input_file, 'r') as infile:
    for line in infile:
        word = line.strip()
        processed_word = process_word(word)

        if processed_word not in processed_words:
            processed_words.append(processed_word)

unique_phonems = []
for proce in processed_words:
    columns = proce.split(' ')
    for column in columns:
        if column not in unique_phonems:
            unique_phonems.append(column)

#for nes in unique_phonems:
#    print(nes)

with open(output_file, 'w') as outfile:
    for nes in unique_phonems:
        outfile.write(nes + '\n')