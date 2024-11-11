import tkinter as tk  # Import the main tkinter module to create and manage the graphical user interface (GUI)
from tkinter import scrolledtext  # Import scrolledtext widget from tkinter to allow text boxes with scrollbars
from analyzer import analyze_code  # Import the analyze_code function from analyzer.py for the core code analysis logic

# Define a class for the GUI, encapsulating the entire graphical interface in a reusable and modular format
class CodeAnalyzerGUI:
    # The initializer (constructor) method of the CodeAnalyzerGUI class, called when an instance of the class is created
    def __init__(self, root):
        """
        Initialize the CodeAnalyzerGUI class by setting up the GUI components.
        Args:
            root: The root window of the Tkinter application (usually the main window).
        """
        self.root = root  # Store the root window reference as an instance variable for later use
        self.root.title("AI Code Analyzer")  # Set the title of the root window to "AI Code Analyzer" to describe the purpose of the window

        # === Input Text Box ===
        # Create a scrolled text widget for inputting code snippets (allows multiline text with scroll capability)
        # Parameters:
        #   - root: Parent window or frame in which the widget will appear
        #   - height: The height of the text box in lines (15 lines)
        #   - width: The width of the text box in characters (70 characters wide)
        #   - wrap: Wrap mode set to tk.WORD to wrap long lines at word boundaries, making text more readable
        self.input_text = scrolledtext.ScrolledText(root, height=15, width=70, wrap=tk.WORD)

        # Pack the input text box into the window
        # - pady: Adds vertical padding of 10 pixels around the widget to prevent it from sticking to other elements
        self.input_text.pack(pady=10)

        # === Analyze Button ===
        # Create a button that will trigger the analysis function when clicked
        # Parameters:
        #   - root: Parent window or frame in which the button will appear
        #   - text: The label shown on the button, here "Analyze Code" to indicate its function
        #   - command: The function to call when the button is clicked, here self.analyze which is defined later
        self.analyze_button = tk.Button(root, text="Analyze Code", command=self.analyze)

        # Pack the analyze button into the window
        # - pady: Adds vertical padding of 10 pixels around the widget
        self.analyze_button.pack(pady=10)

        # === Output Text Box ===
        # Create a second scrolled text widget for displaying the analysis results from OpenAI
        # Parameters (similar to the input box above):
        #   - root: Parent window or frame in which the widget will appear
        #   - height: The height of the text box in lines (15 lines)
        #   - width: The width of the text box in characters (70 characters wide)
        #   - wrap: Wrap mode set to tk.WORD to wrap lines at word boundaries
        self.output_text = scrolledtext.ScrolledText(root, height=15, width=70, wrap=tk.WORD)

        # Pack the output text box into the window
        # - pady: Adds vertical padding of 10 pixels around the widget
        self.output_text.pack(pady=10)

    # Define the analyze function, which is triggered when the "Analyze Code" button is clicked
    def analyze(self):
        """
        Retrieve the code snippet from the input text box, send it for analysis,
        and display the result in the output text box.
        """
        # Get the code snippet text from the input text box
        # - "1.0": This specifies the starting point (line 1, character 0) in the text box
        # - tk.END: This specifies the end point, including all text from the beginning to the end of the input box
        code_snippet = self.input_text.get("1.0", tk.END)

        # Use the analyze_code function (imported from analyzer.py) to analyze the code snippet
        # - Pass code_snippet to the function and store the analysis results in feedback
        feedback = analyze_code(code_snippet)

        # Clear any existing text in the output text box to ensure previous results are removed
        # - "1.0": Starting point (line 1, character 0)
        # - tk.END: End point, which clears everything from start to end
        self.output_text.delete("1.0", tk.END)

        # Insert the feedback (analysis results) into the output text box
        # - tk.END: Place the feedback at the end of the current text, which starts as an empty box
        self.output_text.insert(tk.END, feedback)
