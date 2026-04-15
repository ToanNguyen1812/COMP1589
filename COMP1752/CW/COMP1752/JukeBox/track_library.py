from library_item import LibraryItem

# Biến global lưu trữ danh sách bài hát
library = {}
library["01"] = LibraryItem("What a Wonderful World", "Louis Armstrong", 5)
library["02"] = LibraryItem("Here Comes the Sun", "The Beatles", 5)
library["03"] = LibraryItem("Count on Me", "Bruno Mars", 3)
library["04"] = LibraryItem("Three Little Birds", "Bob Marley", 1)
library["05"] = LibraryItem("You've Got a Friend", "James Taylor", 3)

def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output

def get_name(key):
    try: return library[key].name
    except KeyError: return None

def get_artist(key):
    try: return library[key].artist
    except KeyError: return None

def get_rating(key):
    try: return library[key].rating
    except KeyError: return -1

def set_rating(key, rating):
    try:
        item = library[key]
        # Khi gán giá trị mới, nó sẽ kích hoạt @rating.setter ở file library_item.py
        # Nếu rating = 9, nó sẽ ném ra lỗi ValueError và dừng lại ngay lập tức!
        item.rating = rating 
    except KeyError:
        return

def get_play_count(key):
    try: return library[key].play_count
    except KeyError: return -1

def get_item(key):
    # Hàm hỗ trợ lấy toàn bộ đối tượng (Dùng cho Playlist)
    try: return library[key]
    except KeyError: return None