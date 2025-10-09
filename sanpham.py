# Code lab 5 bài 1 ở đây
class sanpham:
    def __init__(self, ten_san_pham, don_gia, giam_gia):
        self.ten_san_pham = ten_san_pham
        self.don_gia = don_gia
        self.giam_gia = giam_gia

    def doc_giam_gia(self):
        return self. giam_gia
    def ghi_giam_gia(self, giam_gia_moi):
        self.giam_gia = giam_gia_moi
    def thue_nhap_khau(self):
        return self.don_gia * 0.1
    def nhap_thong_tin_sp(self):
        self.ten_san_pham = input("Nhập tên sản phẩm: ")
        self.don_gia = float(input("Nhập đơn giá: "))
        self.giam_gia = float(input("Nhập giảm giá: ")) 
    def xuat_thong_tin_sp(self):
        print(f"Sản phẩm {self.ten_san_pham} có giá {self.don_gia} giảm giá {self.giam_gia} Thuế nhập khẩu {self.thue_nhap_khau()}")
    def __str__(self):
        return f"Sản phẩm {self.ten_san_pham} có giá {self.don_gia} giảm giá {self.giam_gia} Thuế nhập khẩu {self.thue_nhap_khau()}"

