# 🚀 HƯỚNG DẪN CHẠY CHƯƠNG TRÌNH - TẤT CẢ CÁC CÁCH

## 📁 Các file trong thư mục

```
TTKH/
├── QR.py                        # Code chính với tất cả thuật toán
├── demo_interactive.py          # Demo TƯƠNG TÁC - Nhập từ bàn phím ⭐
├── demo_custom.py               # Demo đơn giản - Sửa code để thay input
├── README.md                    # Hướng dẫn chi tiết
├── HUONG_DAN_INTERACTIVE.md     # Hướng dẫn demo tương tác
├── SUMMARY.md                   # Tóm tắt cải tiến
├── CACH_CHAY.md                 # File này
└── BÁO CÁO TTKH.pdf             # Báo cáo
```

---

## 🎯 CÁCH 1: DEMO TƯƠNG TÁC (KHUYẾN NGHỊ) ⭐

### Tự nhập input từ bàn phím

```bash
cd /home/oc/Downloads/TTKH
python3 demo_interactive.py
```

### Các bước:
1. Chọn `1` để nhập hệ phương trình
2. Nhập số hàng `m` và số cột `n`
3. Nhập từng hàng của ma trận A (các số cách nhau bởi dấu CÁCH)
4. Nhập vector b
5. Xác nhận và xem kết quả

### Ví dụ nhập:
```
Nhập số hàng của ma trận A (m): 3
Nhập số cột của ma trận A (n): 2
Hàng 1: 1 1
Hàng 2: 1 2
Hàng 3: 1 3
Vector b (3 phần tử): 1 2 2
```

### Tính năng:
- ✅ Nhập từ bàn phím
- ✅ Kiểm tra lỗi input
- ✅ Xem ví dụ mẫu
- ✅ Menu dễ sử dụng
- ✅ Có thể chạy nhiều lần

---

## 🎯 CÁCH 2: DEMO ĐƠN GIẢN

### Sửa code để thay input

```bash
cd /home/oc/Downloads/TTKH
python3 demo_custom.py
```

### Để thay đổi hệ phương trình:
1. Mở file `demo_custom.py`
2. Sửa phần này:
```python
A = np.array([
    [1, 1],
    [1, 2],
    [1, 3]
], dtype=float)

b = np.array([1, 2, 2], dtype=float)
```
3. Lưu file
4. Chạy lại: `python3 demo_custom.py`

---

## 🎯 CÁCH 3: CHẠY TẤT CẢ DEMO MẪU

### Chạy tất cả ví dụ từ báo cáo

```bash
cd /home/oc/Downloads/TTKH
python3 QR.py
```

### Bao gồm:
- Demo ví dụ 3.4 từ báo cáo
- Demo ma trận ill-conditioned
- Demo hồi quy tuyến tính
- 2 ví dụ hệ phương trình tùy chỉnh

---

## 🎯 CÁCH 4: SỬ DỤNG TRONG CODE PYTHON

### Import và sử dụng hàm

```python
import numpy as np
from QR import solve_system

# Định nghĩa hệ phương trình
A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
], dtype=float)

b = np.array([7, 8, 9], dtype=float)

# Giải và hiển thị kết quả
solve_system(A, b)
```

### Hoặc sử dụng từng phương pháp riêng:

```python
from QR import LeastSquaresSolver

# Giải bằng Householder
result = LeastSquaresSolver.solve_qr(A, b, method='householder')

print(f"Nghiệm: {result['x']}")
print(f"Ma trận Q:\n{result['Q']}")
print(f"Ma trận R:\n{result['R']}")
print(f"Thời gian: {result['time']*1000:.4f} ms")
```

---

## 📊 SO SÁNH CÁC CÁCH

| Cách | Ưu điểm | Nhược điểm | Khi nào dùng |
|------|---------|------------|--------------|
| **1. Interactive** | Nhập từ bàn phím, dễ dùng | - | Muốn thử nhiều input khác nhau |
| **2. Custom** | Đơn giản, nhanh | Phải sửa code | Có sẵn input, chạy 1 lần |
| **3. Full demo** | Xem tất cả ví dụ | Không tùy chỉnh | Xem demo, kiểm tra code |
| **4. Import** | Linh hoạt nhất | Cần viết code | Tích hợp vào project |

---

## 🎓 KHUYẾN NGHỊ

### Lần đầu sử dụng:
```bash
python3 demo_interactive.py
```
Chọn `2` để xem ví dụ mẫu trước!

### Khi đã quen:
```bash
python3 demo_custom.py
```
Sửa A và b trong file, rồi chạy lại.

### Để kiểm tra code:
```bash
python3 QR.py
```
Xem tất cả demo và kết quả.

---

## 💡 MẸO

### Nhập số trong demo interactive:
- Các số cách nhau bởi **dấu CÁCH**, không phải dấu phẩy
- Có thể nhập số thập phân: `1.5 2.3 3.7`
- Có thể nhập số âm: `-1 2 -3`

### Ví dụ:
```
Hàng 1: 1 2 3        ✅ ĐÚNG
Hàng 1: 1,2,3        ❌ SAI
Hàng 1: 1  2  3      ✅ ĐÚNG (nhiều dấu cách cũng OK)
```

---

## 🆘 TROUBLESHOOTING

### Lỗi: ModuleNotFoundError: No module named 'numpy'
```bash
pip3 install numpy
```

### Lỗi: Permission denied
```bash
chmod +x demo_interactive.py
python3 demo_interactive.py
```

### Muốn thoát chương trình:
- Nhấn `Ctrl + C`
- Hoặc chọn `3` trong menu

---

## 📞 TÓM TẮT NHANH

```bash
# Cách dễ nhất - Nhập từ bàn phím
python3 demo_interactive.py

# Cách nhanh - Sửa code
# 1. Mở demo_custom.py
# 2. Sửa A và b
# 3. Chạy:
python3 demo_custom.py

# Xem tất cả demo
python3 QR.py
```

**Chúc bạn sử dụng thành công! 🎉**
