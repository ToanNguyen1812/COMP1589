import tkinter as tk    # standard GUI library in Python
import tkinter.scrolledtext as tkst # scrolledText widget for multi-line text with a scrollbar


import track_library as lib     # Import the data manager (backend) to interact with tracks
import font_manager as fonts    # Import the font manager to apply consistent typography


def set_text(text_area, content):
    #A helper function to clear a text area and insert new content.
    # text_area: The tk.Text or tkst.ScrolledText widget to be updated.
    #content: The string to insert into the text area.
    # Delete all existing text from line 1, character 0 ("1.0") to the end (tk.END)
    text_area.delete("1.0", tk.END)
    # Insert the new content starting at line 1, character 0
    text_area.insert(1.0, content)


class TrackViewer():
    def __init__(self, window):
        # Constructor of the TrackViewer class. Initializes the GUI layout.
        # window: The parent window (Toplevel) passed from the main application.
        # Set the dimensions of the window (width x height in pixels)
        window.geometry("750x350")
        # Set the title of the window
        window.title("View Tracks")

        # --- Create and place the 'List All Tracks' button ---
        # command=self.list_tracks_clicked binds the button to the event handler method
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        # Place the button in the grid layout at row 0, column 0 with some padding (padx, pady)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        # --- Create and place the instruction label ---
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # --- Create and place the Entry widget (text box) for user input ---
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # --- Create and place the 'View Track' button ---
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        # --- Create and place the ScrolledText area to display the full list of tracks ---
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        # columnspan=3 means this widget will span across 3 columns. sticky="W" aligns it to the West (left)
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # --- Create and place the Text area to display details of a specific track ---
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        # sticky="NW" aligns it to the North-West (top-left) within its grid cell
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # --- Create and place the status label to display system messages to the user ---
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Automatically call this method to display all tracks as soon as the window opens
        self.list_tracks_clicked()

    def view_tracks_clicked(self):
        # Event handler for the 'View Track' button.
        # Retrieves the track ID from the entry, fetches data from the library, and displays it.
        # Get the track ID entered by the user in the input text box
        key = self.input_txt.get()
        # Fetch the track name from the library using the entered key
        name = lib.get_name(key)

        # Check if the track exists (if name is not None)
        if name is not None:
            # Fetch remaining details of the track
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)

            # Format the details into a single string using f-strings
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
            # Display the formatted string in the track text area
            set_text(self.track_txt, track_details)
        else:
            # If the track doesn't exist, display an error message in the text area
            set_text(self.track_txt, f"Track {key} not found")

        # Update the status label to inform the user that the action was performed
        self.status_lbl.configure(text="View Track button was clicked!")

    def list_tracks_clicked(self):
        # Event handler for the 'List All Tracks' button.
        # Fetches the entire track list from the library and displays it.
        # Fetch the formatted string containing all tracks from the library
        track_list = lib.list_all()
        # Display the list in the ScrolledText area
        set_text(self.list_txt, track_list)
        # Update the status label
        self.status_lbl.configure(text="List Tracks button was clicked!")

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
