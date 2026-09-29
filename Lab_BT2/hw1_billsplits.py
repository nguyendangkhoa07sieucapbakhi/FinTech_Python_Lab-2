print("--- CHIA TIỀN THEO HOÁ ĐƠN ---")
#1. NHẬP LIỆU VÀ ÉP KIỂU 
X = float(input("Nhập tổng hóa đơn: "))
Y = float(input("Nhập % tiền tip: "))
N = int(input("Nhập số người: "))

#2. TÍNH TOÁN 
tien_tip = X * Y / 100
tong_tien = X + tien_tip
moi_nguoi = tong_tien / N

print(f"Mỗi người phải trả  :{round(moi_nguoi)} đồng")
