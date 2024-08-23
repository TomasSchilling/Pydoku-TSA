import tkinter as tk

def open_main_menu():
    # Create the main window
    root = tk.Tk()
    root.title("Py- doku Main Menu")
    root.geometry("500x400")
    root.resizable(False, False)  # Prevent resizing

    # Center the window on the screen
    window_width = 400
    window_height = 350
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = int((screen_width/2) - (window_width/2))
    y_coordinate = int((screen_height/2) - (window_height/2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    # Create a variable to store the difficulty selection
    difficulty_var = tk.IntVar(value=1)  # Default difficulty is Easy (1)

    # Title Label
    title_label = tk.Label(root, text="Welkome to Py-doku", font=("Helvetica", 24))
    title_label.pack(pady=20)

    # Difficulty Frame
    difficulty_frame = tk.LabelFrame(root, text="Select Difficulty", font=("Helvetica", 12))
    difficulty_frame.pack(pady=10, padx=20, fill="both", expand="yes")

    # Difficulty Radio Buttons
    tk.Radiobutton(difficulty_frame, text="Easy", variable=difficulty_var, value=1, font=("Helvetica", 12)).pack(anchor='w', padx=20, pady=5)
    tk.Radiobutton(difficulty_frame, text="Medium", variable=difficulty_var, value=2, font=("Helvetica", 12)).pack(anchor='w', padx=20, pady=5)
    tk.Radiobutton(difficulty_frame, text="Hard", variable=difficulty_var, value=3, font=("Helvetica", 12)).pack(anchor='w', padx=20, pady=5)
    tk.Radiobutton(difficulty_frame, text="Hardest", variable=difficulty_var, value=4, font=("Helvetica", 12)).pack(anchor='w', padx=20, pady=5)

    # New Game Button
    new_game_button = tk.Button(root, text="New Game", font=("Helvetica", 14), width=15, command=lambda: start_game(root, difficulty_var))
    new_game_button.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()
    return difficulty_var.get()

def start_game(root, difficulty_var):
    selected_difficulty = difficulty_var.get()
    print(f"Selected Difficulty: {selected_difficulty}")
    root.destroy()
    

