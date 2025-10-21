from quanlynv import *
ql = QuanLynv()
menu = """
1. Nhập danh sách nhân viên
2. Đọc thông tin nhân viên
3. Tìm và hiển thị nhân viên theo mã
4. Xóa nhân viên
5. Cập nhật thông tin nhân viên
6. Tìm các nhân viên theo khoảng lương
7. Sắp xếp nhân viên theo họ và tên
8. Sắp xếp nhân viên theo thu nhập
9. Xuất 5 nhân viên có thu nhập cao nhất
"""
while True:
    print(menu)
    lua_chon = input("Nhập lựa chọn của bạn (nhấn 0 để thoát): ")
    match lua_chon:
        case "0":
            print("Thoát chương trình")
            break
        case "1":
            print("xuất thông tin nhân viên")
            ql.nhap_dsnv()
        case "2":
            print("Đọc thông tin nhân viên")
        case "3":
            ql.tim_nhan_vien_theo_ma()
        case "4":
            pass
        case "5":
            pass
        case "6":
            ql.tim_nhan_vien_theo_khoang_luong()
        case "7":
            ql.sap_xep_theo_ho_ten()
        case "8":
            ql.sap_xep_theo_thu_nhap()
        case "9":
            ql.xuat_5_nhan_vien_thu_nhap_cao_nhat()
        case _:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")