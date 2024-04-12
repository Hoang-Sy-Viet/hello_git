from collections import defaultdict
words = ["tea", "eat", "bat", "ate", "arc", "car",'team']

def group_anagrams(x):
    # Khởi tạo một từ điển mặc định (defaultdict) có tên dfdict. 
    dfdict = defaultdict(list)
    # Duyệt qua từng item trong list x
    for item in x:
        # sorted(item): Sắp xếp các ký tự của từ item theo thứ tự bảng chữ cái
        # ' '.join(sorted(item)) :Kết hợp các ký tự đã sắp xếp thành một chuỗi mới
        # sort_item: sẽ là key đại diện cho đảo từ của từ item
        sort_item = ' '.join(sorted(item))
        # Thêm từ item vào danh sách tương ứng với khóa sorted_item trong dfdict
        # Nếu key sorted_item chưa tồn tại, một list mới sẽ được tạo ra và item sẽ được thêm vào là values
        dfdict[sort_item].append(item)
    # Trả về danh sách các giá trị trong từ điển dfdict
    return dfdict
print(group_anagrams(words))
