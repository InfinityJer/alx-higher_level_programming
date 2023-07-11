def write_file(filename="", text=""):
    """
    This function writes a string to a text file (UTF8) and returns the number of characters written.
    
    Parameters:
    filename (str): The name of the file to write to
    text (str): The string to write to the file
    
    Returns:
    int: The number of characters written to the file
    """
    try:
        # Open the file in write mode using the 'with' statement
        with open(filename, 'w', encoding='utf8') as file:
            # Write the text to the file
            file.write(text)
            
            # Return the number of characters written
            return len(text)
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
        return 0
