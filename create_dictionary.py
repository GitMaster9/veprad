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
output_file = 'dict.txt'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        word = line.strip()
        processed_word = process_word(word)
        outfile.write(word + '\t' + "[" + word + "]" + '\t' + processed_word + '\n')