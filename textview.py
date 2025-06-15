text = "This is a sample text to test the calculator program. The text contains various words and phrases that can be searched. You can navigate through the text using the calculator keys. The fx-CG50 calculator has a limited display but this program allows you to view all content in an organized way."

# Variables
pos = 0
search = ""
found = []
index = -1
show_menu_flag = True  # Show menu only first time

def clear():
    print("")
    print("")
    print("")
    print("")
    print("")

def wait():
    input("Press EXE...")

def show():
    global pos, search
    clear()
    
    # Take 126 characters (6 rows x 21)
    end = pos + 126
    if end > len(text):
        end = len(text)
    
    part = text[pos:end]
    
    # Print 6 rows of 21 characters without borders
    for i in range(6):
        start = i * 21
        row_end = start + 21
        if start < len(part):
            row = part[start:row_end]
            
            # Highlight search word if present
            if search and len(search) > 0:
                # Find search word in this row (case insensitive)
                search_lower = search.lower()
                row_lower = row.lower()
                search_pos = row_lower.find(search_lower)
                if search_pos != -1:
                    # Replace with uppercase to highlight
                    before = row[:search_pos]
                    word = row[search_pos:search_pos+len(search)].upper()
                    after = row[search_pos+len(search):]
                    row = before + word + after
            
            # Fill with spaces if needed
            while len(row) < 21:
                row = row + " "
            print(row)
        else:
            print("                     ")

def find_word(word):
    global search, found, index, pos
    
    search = word
    found = []
    index = -1
    
    # Search for the word
    i = 0
    while i < len(text):
        if text[i:i+len(word)].lower() == word.lower():
            found.append(i)
        i = i + 1
    
    # Go to first and center it
    if len(found) > 0:
        index = 0
        # Center the word in the display (63 chars before the word)
        word_pos = found[0]
        pos = word_pos - 63
        if pos < 0:
            pos = 0
        # Make sure we don't go past the end
        if pos + 126 > len(text):
            pos = len(text) - 126
            if pos < 0:
                pos = 0

def next_match():
    global index, pos
    
    if len(found) == 0:
        return
    
    index = index + 1
    if index >= len(found):
        index = 0
    
    # Center the word in the display
    word_pos = found[index]
    pos = word_pos - 63
    if pos < 0:
        pos = 0
    # Make sure we don't go past the end
    if pos + 126 > len(text):
        pos = len(text) - 126
        if pos < 0:
            pos = 0

def prev_match():
    global index, pos
    
    if len(found) == 0:
        return
    
    index = index - 1
    if index < 0:
        index = len(found) - 1
    
    # Center the word in the display
    word_pos = found[index]
    pos = word_pos - 63
    if pos < 0:
        pos = 0
    # Make sure we don't go past the end
    if pos + 126 > len(text):
        pos = len(text) - 126
        if pos < 0:
            pos = 0

def forward():
    global pos
    
    pos = pos + 126
    if pos >= len(text):
        pos = len(text) - 126
        if pos < 0:
            pos = 0

def backward():
    global pos
    
    pos = pos - 126
    if pos < 0:
        pos = 0

def show_menu():
    print("")
    print("0: Exit")
    print("1: Find word (custom)")
    print("2: Next match")
    print("3: Previous match")
    print("4: Forward")
    print("5: Backward")
    print("6: Start")

wait()

while True:
    show()
    
    # Show menu only first time
    if show_menu_flag:
        show_menu()
        show_menu_flag = False
    
    # Show command prompt with next function number
    next_cmd = "1"  # Default next command
    if len(found) > 0:
        if index < len(found) - 1:
            next_cmd = "2"  # Next match available
        else:
            next_cmd = "4"  # Forward navigation
    
    cmd = input("Command: " + next_cmd + " > ")
    
    # If user just presses enter, use the suggested command
    if cmd == "":
        cmd = next_cmd
    
    if cmd == "0":
        break
    elif cmd == "1":
        word = input("Word to find: ")
        find_word(word)
    elif cmd == "2":
        next_match()
    elif cmd == "3":
        prev_match()
    elif cmd == "4":
        forward()
    elif cmd == "5":
        backward()
    elif cmd == "6":
        pos = 0
    else:
        # Invalid command - do nothing, just continue
        pass 