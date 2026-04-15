import pytest
from library_item import LibraryItem

def test_initialization():
    # Kiểm tra xem đối tượng có được khởi tạo đúng dữ liệu không
    item = LibraryItem("Test Song", "Test Artist", 3)
    assert item.name == "Test Song"
    assert item.artist == "Test Artist"
    assert item.rating == 3
    assert item.play_count == 0

def test_play_method():
    # Kiểm tra xem hàm play() có tăng số lượt nghe lên 1 không
    item = LibraryItem("Test Song", "Test Artist", 3)
    item.play()
    assert item.play_count == 1
    item.play()
    assert item.play_count == 2

def test_stars_method():
    # Kiểm tra xem hàm in ra ngôi sao có chuẩn xác không
    item = LibraryItem("Test Song", "Test Artist", 4)
    assert item.stars() == "****"

def test_valid_rating_update():
    # Kiểm tra việc cập nhật rating hợp lệ
    item = LibraryItem("Test Song", "Test Artist", 2)
    item.rating = 5
    assert item.rating == 5

def test_invalid_rating_type():
    # Bắt buộc hệ thống phải ném ra lỗi ValueError nếu nhập chữ
    item = LibraryItem("Test Song", "Test Artist", 2)
    with pytest.raises(ValueError) as excinfo:
        item.rating = "five"
    assert "must be an integer" in str(excinfo.value)

def test_invalid_rating_range():
    # Bắt buộc hệ thống phải ném ra lỗi ValueError nếu rating > 5
    item = LibraryItem("Test Song", "Test Artist", 2)
    with pytest.raises(ValueError) as excinfo:
        item.rating = 9
    assert "between 0 and 5" in str(excinfo.value)