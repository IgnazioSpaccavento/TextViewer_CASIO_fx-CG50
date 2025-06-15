# Text Viewer for fx-CG50

A text viewer optimized for Casio fx-CG50 calculators with search and navigation features.

## Features

- **Optimized display**: 6 rows × 21 characters to maximize readability
- **Smart search**: Find words in text (case-insensitive)
- **Smooth navigation**: Scroll forward/backward through text
- **Highlighting**: Found words are displayed in UPPERCASE
- **Auto-centering**: Found occurrences are automatically centered
- **Clean interface**: No unnecessary borders, maximum space for content
- **Smart commands**: Program suggests the next logical command

## How to use

### Available commands:

- **0**: Exit program
- **1**: Search for custom word
- **2**: Go to next occurrence
- **3**: Go to previous occurrence
- **4**: Move forward in text
- **5**: Move backward in text
- **6**: Go to beginning of text

### Usage example:

1. Start the program
2. Press `1` to search for a word
3. Type the word to search (e.g. "text")
4. Use `2` and `3` to navigate between occurrences
5. Use `4` and `5` to scroll freely through text
6. Press `0` to exit

## Advanced features

### Case-insensitive search
Search doesn't distinguish between uppercase and lowercase:
- Searching "TEXT" will find "text", "Text", "TEXT", etc.

### Smart prompt
The program automatically suggests the next command:
- After a search → suggests "2" (next occurrence)
- At last occurrence → suggests "4" (forward in text)
- By default → suggests "1" (new search)

### Automatic navigation
- Pressing only ENTER executes the suggested command
- Found words are automatically centered in display
- Navigation is smooth without interruptions

## Installation

1. Download the `textview.py` file
2. Modify the `text` variable with your content
3. Transfer the file to your fx-CG50 calculator
4. Run the program

## Customization

### Change the text
Modify the first line of the file:
```python
text = "Your text here..."
```

### Modify display dimensions
To adapt the program to different displays, modify these values:
- Rows: change `range(6)` in the `show()` function
- Characters per row: change `21` in all calculations
- Total characters: update `126` (rows × characters)

## Compatibility

- **Calculator**: Casio fx-CG50
- **Language**: Python
- **Display**: Optimized for 6 rows × 21 characters
- **Memory**: Minimal memory usage

## Contributing

Contributions, bug reports and suggestions are welcome! Open an issue or submit a pull request.

---

**Note**: This program was designed specifically for the hardware limitations of the fx-CG50 calculator, with focus on ease of use and maximum display efficiency. 
