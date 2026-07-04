import os

def add_line_to_html_files():
    # Read the line from a.txt
    try:
        with open('a.txt', 'r') as txt_file:
            line_to_add = txt_file.readline().strip()
    except FileNotFoundError:
        print("The file 'a.txt' was not found.")
        return

    # Iterate over all .html files in the current directory
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            try:
                # Read the content of the HTML file
                with open(filename, 'r', encoding='utf-8') as html_file:
                    content = html_file.read()

                # Add the line to the top and save it back
                with open(filename, 'w', encoding='utf-8') as html_file:
                    html_file.write(line_to_add + '\n' + content)

                print(f"Added line to: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    add_line_to_html_files()