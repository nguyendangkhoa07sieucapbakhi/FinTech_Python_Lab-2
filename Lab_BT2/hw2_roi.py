print("---  Tỷ suất sinh lời trên vốn đầu tư ---")
tong_von_ban_dau = float(input("Nhập tổng vốn ban đầu: "))
tong_gia_tri_ban_ra = float(input("Nhập tổng giá trị bán ra: "))

loi_nhuan_rong = tong_gia_tri_ban_ra - tong_von_ban_dau
ROI = (loi_nhuan_rong / tong_von_ban_dau) * 100

print(f"Lợi nhuận ròng: {loi_nhuan_rong}")
print(f"Tỷ lệ ROI: {ROI}%")