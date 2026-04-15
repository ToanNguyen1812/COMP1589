class LibraryItem:
    def __init__(self, name, artist, rating=0):
        # Đóng gói dữ liệu (Private)
        self.__name = name
        self.__artist = artist
        self.__play_count = 0
        self.rating = rating  # Dòng này sẽ gọi thẳng xuống hàm setter bên dưới

    @property
    def name(self): return self.__name

    @property
    def artist(self): return self.__artist

    @property
    def play_count(self): return self.__play_count

    # --- ĐÂY CHÍNH LÀ CHỐT CHẶN BẮT LỖI SỐ 9 CỦA BẠN ---
    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int):
            raise ValueError("Rating must be an integer number.")
        if value < 0 or value > 5:
            raise ValueError("Rating must be between 0 and 5.")
        self.__rating = value

    def play(self):
        self.__play_count += 1

    def info(self):
        return f"{self.__name} - {self.__artist} {self.stars()}"

    def stars(self):
        return "*" * self.__rating