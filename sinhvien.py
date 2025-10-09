# Các thuộc tính
class sinhvien:
    # Các phương thức
    def __init__(self, ten_sv, namsinh_sv, diem_sv):
        self.ten_sinh_vien = ten_sv
        self.nam_sinh = namsinh_sv
        self.diem = diem_sv
    def xuat_thong_tin_sv(self):
        print("Tên sinh viên:", self.ten_sinh_vien)
        print("Năm sinh:", self.nam_sinh)
        print("Điểm:", self.diem)

sv1 = sinhvien("duma", 2008, 3)
sv1.xuat_thong_tin_sv()

class sinhvienXLDL(sinhvien):
    def __init__(self, ten_sv, namsinh_sv, diem_sv, lap_trinh):
        sinhvien.__init__(self, ten_sv, namsinh_sv, diem_sv)
        self.lap_trinh = lap_trinh
    def xuat_thong_tin_sv(self):
        print(f"{sinhvien.xuat_thong_tin_sv(self)} và lập trình: {self.lap_trinh}")
sv1 = sinhvienXLDL("duma", 2008, 3, "python")
sv1.xuat_thong_tin_sv()