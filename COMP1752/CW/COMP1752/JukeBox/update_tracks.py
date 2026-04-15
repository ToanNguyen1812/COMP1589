import tkinter as tk
import track_library as lib  # Kết nối với tầng dữ liệu
import font_manager as fonts

class UpdateTracks:
    def __init__(self, window):
        window.geometry("450x250")
        window.title("Update Tracks")

        # --- Nhập ID bài hát ---
        tk.Label(window, text="Enter Track Number:").grid(row=0, column=0, padx=10, pady=10, sticky="E")
        self.input_id = tk.Entry(window, width=5)
        self.input_id.grid(row=0, column=1, padx=10, pady=10, sticky="W")

        # --- Nhập Rating mới ---
        tk.Label(window, text="Enter New Rating (0-5):").grid(row=1, column=0, padx=10, pady=10, sticky="E")
        self.input_rating = tk.Entry(window, width=5)
        self.input_rating.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        # --- Nút Cập nhật ---
        update_btn = tk.Button(window, text="Update Track", command=self.update_clicked)
        update_btn.grid(row=2, column=0, columnspan=2, pady=10)

        # --- Thanh trạng thái hiển thị kết quả ---
        self.status_lbl = tk.Label(window, text="Ready to update.", font=("Helvetica", 10), fg="blue")
        self.status_lbl.grid(row=3, column=0, columnspan=2, pady=10)

    # ================= LOGIC XỬ LÝ =================
    def update_clicked(self):
        key = self.input_id.get()
        rating_str = self.input_rating.get()

        # 1. Kiểm tra xem ID bài hát có tồn tại không
        name = lib.get_name(key)
        if name is None:
            self.status_lbl.configure(text=f"Error: Track '{key}' not found in library.", fg="red")
            return

        # 2. Kiểm tra xem người dùng có nhập nhầm "chữ" vào ô số không
        try:
            new_rating = int(rating_str)
        except ValueError:
            self.status_lbl.configure(text="Error: Rating must be an integer number.", fg="red")
            return

        # 3. Cập nhật Rating và bắt lỗi Logic từ Class LibraryItem (Kỹ thuật Week 7 & Week 4)
        try:
            lib.set_rating(key, new_rating)
            
            # Nếu thành công, lấy số Play count ra và in thông báo
            play_count = lib.get_play_count(key)
            success_msg = f"Success! '{name}' updated.\nNew Rating: {new_rating} stars | Plays: {play_count}"
            self.status_lbl.configure(text=success_msg, fg="green")
            
            # Xóa trống các ô nhập liệu
            self.input_id.delete(0, tk.END)
            self.input_rating.delete(0, tk.END)
            
        except ValueError as e:
            # Bắt chính xác lỗi ném ra từ @rating.setter trong file library_item.py
            self.status_lbl.configure(text=f"Validation Error: {e}", fg="red")