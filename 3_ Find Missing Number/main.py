listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16,5,2,8]
def find_missing_number(list):
    # set: giúp ta loại bỏ các phần tử trùng lặp và tăng hiệu suất tìm kiếm.
    # sorted sẽ sắp xếp set(list) theo thứ tự tăng dần, để ta có thể use vòng lặp for
    numbers = sorted(set(list))
    # missing_number :tạo ra 1 list rỗng để chứa các số bị thiếu
    missing_number =[]
    for i in range(1,numbers[-1]):
        # Kiểm tra xem số i có trong tập hợp numbers hay không.
        # Nếu không có,tức là số i bị thiếu, và chúng ta thêm nó vào list missing_number
        if i not in numbers:
            missing_number.append(i)
    # Trả về danh sách output chứa các số bị thiếu.
    return missing_number

missing_number= find_missing_number(listOfNumbers)
print('missing_number:',missing_number)
print()
merge_number = sorted(list(set(listOfNumbers)).__add__(missing_number))
print(merge_number)