# Import neccessary libraries
import json
from difflib import get_close_matches

# Create the function for loading json file to dictionary
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Create the function to get definition of words.
def get_definition(word, data):
    word = word.lower()  # Convert input word to lowercase for case insensitivity
    if word in data:
        return data[word]
    elif word.title() in data:  # Check for title case (e.g., converting rain to Rain)
        return data[word.title()]
    elif word.upper() in data:  # Check for uppercase (e.g., converting rain to RAIN)
        return data[word.upper()]
    else:
        close_matches = get_close_matches(word, data.keys())
        if close_matches:
            suggestion = close_matches[0]
            yes_or_no = input(f"Did you mean '{suggestion}' instead? Enter Y if yes, or N if no: ").upper()
            if yes_or_no == 'Y':
                return data[suggestion]
            else:
                return "Word not found. Please double-check your spelling."
        else:
            return "Word not found. Please double-check your spelling."

if __name__ == "__main__":
    file_path = "data.json"  # Path to your JSON file containing dictionary data
    dictionary_data = load_data(file_path)

    while True:
        search_word = input("Enter a word to search for its definition (type 'exit' to quit): ")
        if search_word.lower() == 'exit':
            print("Exiting the program...")
            break
        else:
            definition = get_definition(search_word, dictionary_data)
            print(definition)
   