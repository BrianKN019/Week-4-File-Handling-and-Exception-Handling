def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file to read
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (e.g., converting to uppercase)
        modified_content = content.upper()  # Example modification: convert to uppercase

        # Open the output file to write the modified content
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"Content successfully written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read or write the file '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Ask the user for the input and output filenames
input_filename = input("Enter the filename to read from: ")
output_filename = input("Enter the filename to write to: ")

# Call the function
read_and_write_file(input_filename, output_filename)
