def extract_and_sort_unique_words(file_path):
    with open(file_path, 'r') as file:
        # Read the lines from the file
        lines = file.readlines()

    # Initialize a set to store unique words
    unique_words = set()

    # Extract words from each transcription and add them to the set
    for line in lines:
        # Split the line into filename and transcription
        parts = line.split(maxsplit=1)
        if len(parts) > 1:
            transcription = parts[1].strip()
            # Split the transcription into words and add them to the set
            words = transcription.split()
            unique_words.update(words)

    # Sort the words alphabetically
    sorted_unique_words = sorted(unique_words)

    return sorted_unique_words

def write_words_to_file(words, output_file_path):
    with open(output_file_path, 'w') as file:
        for word in words:
            file.write(f"{word}\n")

# Define the path to the prompts.txt file
file_path = 'prompts.txt'
# Define the path to the output wlist.txt file
output_file_path = 'wlist.txt'

# Extract and sort the unique words
sorted_unique_words = extract_and_sort_unique_words(file_path)

wlist = []
wlist.append("SENT-END")
wlist.append("SENT-START")
wlist.extend(sorted_unique_words)

# Print the sorted unique words
#for word in wlist:
#    print(word)

# Write the sorted unique words to the output file
write_words_to_file(wlist, output_file_path)