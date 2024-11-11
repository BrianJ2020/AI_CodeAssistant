import tkinter as tk  # Import the main Tkinter module to create and manage the application's main window
from gui import CodeAnalyzerGUI  # Import the CodeAnalyzerGUI class from gui.py to set up the user interface

# Define the main function that initializes the GUI and runs the application
def main():
    """
    The main function that sets up and launches the Tkinter graphical user interface (GUI) application.
    """
    # Create the main application window using Tkinter's Tk() class
    # - `tk.Tk()` is the starting point for any Tkinter application, creating the root window
    root = tk.Tk()  # Instantiate the main window where all GUI elements will be displayed
    
    # Initialize the GUI by creating an instance of the CodeAnalyzerGUI class
    # - `CodeAnalyzerGUI(root)`: Passes the root window to CodeAnalyzerGUI to attach widgets to this window
    # - The CodeAnalyzerGUI class is responsible for setting up and managing the layout of widgets
    gui = CodeAnalyzerGUI(root)  # Create the GUI interface within the root window
    
    # Start Tkinter's main event loop to keep the window open and responsive to user inputs
    # - `root.mainloop()` is an infinite loop that keeps the application running until the user closes the window
    # - This event loop listens for user interactions, such as button clicks and text input, to trigger corresponding events
    root.mainloop()  # Enter Tkinter's main event loop, running the application continuously

# Check if this script is executed directly (not imported as a module) before running the main function
# - `if __name__ == "__main__"` is a standard Python construct that allows code to run only when the script is executed directly
# - This prevents the main function from running automatically if the script is imported as a module in another file
if __name__ == "__main__":
    main()  # Call the main function to start the application if the script is run directly
