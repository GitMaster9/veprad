def process_word(word):
    special_words = {
        'SENT-END': 'sil',
        'SENT-START': 'sil',
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
    
    for old, new in replacements.items():
        word = word.replace(old, new)
    
    # Separate every letter by a space
    spaced_word = ' '.join(list(word))
    
    return spaced_word

input_file = 'wlist.txt'
output_file = 'source_dict.txt'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        word = line.strip()
        processed_word = process_word(word)
        outfile.write(word + '\t' + processed_word + '\n')