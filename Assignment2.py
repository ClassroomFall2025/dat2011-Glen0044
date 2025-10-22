from quanlynv import *
ql = Quanlynv()
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
            print("---Thoát chương trình---")
            break
        case "1":
            print("---nhập thông tin nhân viên---")
            ql.nhap_dsnv()
        case "2":
            print("---Đọc thông tin nhân viên---")
            ql.xuat_dsnv()
        case "3":
            print("---Tìm nhân viên theo mã---")
            ql.tim_nhan_vien_theo_ma()
        case "4":
            print("---Xóa nhân viên---")
            ma_nv = input("Nhập mã nhân viên cần xóa: ")
            ql.xoa_nhan_vien(ma_nv)
        case "5":
            print("---Cập nhật thông tin nhân viên---")
            ql.cap_nhat_thong_tin_nhan_vien()
        case "6":
            print("---Tìm nhân viên theo khoảng lương---")
            ql.tim_nhan_vien_theo_khoang_luong()
        case "7":
            print("---Sắp xếp nhân viên theo họ và tên---")
            ql.sap_xep_theo_ho_ten()
        case "8":
            print("---Sắp xếp nhân viên theo thu nhập---")
            ql.sap_xep_theo_thu_nhap()
        case "9":
            print("---5 nhân viên có thu nhập cao nhất---")
            ql.xuat_5_nhan_vien_thu_nhap_cao_nhat()
        case _:
            print("---Lựa chọn không hợp lệ, vui lòng chọn lại.---")