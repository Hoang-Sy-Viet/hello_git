# cach2: use algorithm :sử dụng thuật toán
inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90],[52,75,253],[54,356,76]]
def Group_Elements_of_Same_Indices(list):
    # Khởi tạo list rỗng có tên outputLists để lưu trữ các danh sách con (sublists) 
    # chứa các phần tử cùng vị trí từ danh sách ban đầu.
    outputLists = []
    # i :cột , j : hàng
    # Duyệt qua các chỉ số từ 0 đến độ dài của danh sách con đầu tiên (list[0]).
    # i sẽ xét từng cột của list
    for i in range(len(list[0])):
        # Thêm một list rỗng vào outputLists. 
        outputLists.append([])
        # j sẽ xét từng phần tử tại cột thứ i của các hàng
        for j in range(len(list)):
            # thêm ptu tại hàng j cột i vào list outputLists[i]
            outputLists[i].append(list[j][i])
    return outputLists
print(Group_Elements_of_Same_Indices(inputLists))