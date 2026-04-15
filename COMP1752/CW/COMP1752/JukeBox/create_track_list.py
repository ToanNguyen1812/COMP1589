import tkinter as tk
import tkinter.scrolledtext as tkst
import track_library as lib  # Import thư viện dữ liệu
import font_manager as fonts

def set_text(text_area, content):
    """Hàm hỗ trợ để xóa và ghi chữ mới vào khung Text"""
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class CreateTrackList:
    def __init__(self, window):
        window.geometry("750x350")
        window.title("Create Track List")

        # Khởi tạo một list rỗng để chứa các ID bài hát được thêm vào
        self.playlist = []

        # --- Ô nhập liệu và Nút Thêm bài hát ---
        tk.Label(window, text="Enter Track Number:").grid(row=0, column=0, padx=10, pady=10, sticky="E")
        self.input_txt = tk.Entry(window, width=5)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10, sticky="W")

        add_btn = tk.Button(window, text="Add Track to Playlist", command=self.add_clicked)
        add_btn.grid(row=0, column=2, padx=10, pady=10)

        # --- Khu vực hiển thị danh sách phát (Playlist) ---
        self.playlist_txt = tkst.ScrolledText(window, width=60, height=10, wrap="none")
        self.playlist_txt.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # --- Nút Phát nhạc và Xóa danh sách ---
        play_btn = tk.Button(window, text="Play Playlist", command=self.play_clicked)
        play_btn.grid(row=2, column=0, padx=10, pady=10)

        reset_btn = tk.Button(window, text="Reset Playlist", command=self.reset_clicked)
        reset_btn.grid(row=2, column=1, padx=10, pady=10)

        # --- Thanh trạng thái ---
        self.status_lbl = tk.Label(window, text="Ready to create playlist.", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=3, sticky="W", padx=10, pady=10)

    # ================= CÁC HÀM XỬ LÝ LOGIC =================

    def update_playlist_display(self):
        """Hàm cập nhật hiển thị danh sách các bài hát trong playlist lên giao diện"""
        display_text = ""
        for key in self.playlist:
            item = lib.get_item(key)
            if item is not None:
                display_text += f"{key} - {item.info()}\n"
        set_text(self.playlist_txt, display_text)

    def add_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key) # Kiểm tra xem bài hát có tồn tại không
        
        if name is not None:
            self.playlist.append(key) # Thêm ID vào danh sách
            self.update_playlist_display() # Cập nhật màn hình
            self.status_lbl.configure(text=f"Track {key} added to playlist!")
        else:
            self.status_lbl.configure(text=f"Error: Track {key} not found in library.")
        
        # Xóa trắng ô nhập liệu để tiện nhập bài tiếp theo
        self.input_txt.delete(0, tk.END)

    def play_clicked(self):
        if len(self.playlist) == 0:
            self.status_lbl.configure(text="Playlist is empty! Please add tracks first.")
            return

        # Tăng lượt nghe cho toàn bộ bài hát trong playlist
        for key in self.playlist:
            item = lib.get_item(key)
            if item is not None:
                item.play()
                
        self.status_lbl.configure(text="Played all tracks in the playlist successfully!")

    def reset_clicked(self):
        self.playlist.clear() # Xóa sạch list
        self.update_playlist_display() # Cập nhật màn hình trống
        self.status_lbl.configure(text="Playlist has been reset.")