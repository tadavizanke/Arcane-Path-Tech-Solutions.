def copy_file(source, destination):
    try:
        with open(source, 'r') as source_file, open(destination, 'w') as destination_file:
            destination_file.write(source_file.read())
        print(f"Contents of '{source}' copied to '{destination}' Successfully.")
    except FileNotFoundError:
        print("One or both files not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def search_word(name, word):
    try:
        with open(name, 'r') as file_name:
            for line_number, line in enumerate(file_name, start=1):
                if word in line:
                    print(f"Found '{word}' at line {line_number}: {line.strip()}")
        print(f"'{word}' search in {name} complete.")
    except FileNotFoundError:
        print(f"File '{name}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

while True:
    print("\nOptions:")
    print("1. Copy contents from one file to another.")
    print("2. Search for a specific word in a file.")
    print("3. Exit")
    option = input("Enter your option (1/2/3): ")

    if option == '1':
        source = input('Enter the name of source file: ')
        destination = input('Enter the name of destination file: ')
        copy_file(source, destination)
    elif option == '2':
        name = input('Enter the name of file to be searched in: ')
        word = input('Enter the word to search for: ')
        search_word(name, word)
    elif option == '3':
        print('Exit.')
        break
    else:
        print('Invalid option.')

