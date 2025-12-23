# PHÂN RÃ QR VÀ GIẢI BÀI TOÁN BÌNH PHƯƠNG TỐI THIỂU

## 📋 Mô tả

Chương trình Python giải hệ phương trình Ax = b bằng phương pháp phân rã QR với 4 thuật toán khác nhau:
- **CGS** (Classical Gram-Schmidt)
- **MGS** (Modified Gram-Schmidt)
- **Householder** (Biến đổi Householder)
- **Givens** (Phép quay Givens)

## 🚀 Cài đặt

### Yêu cầu:
- Python 3.x
- NumPy

### Kiểm tra môi trường:
```bash
python3 --version
python3 -c "import numpy; print('NumPy OK')"
```

## 📖 Cách sử dụng

### Cách 1: Chạy tất cả demo mẫu
```bash
python3 QR.py
```

Chương trình sẽ chạy:
- Demo ví dụ 3.4 từ báo cáo
- Demo với ma trận ill-conditioned
- Demo hồi quy tuyến tính
- 2 ví dụ hệ phương trình tùy chỉnh

### Cách 2: Giải hệ phương trình của bạn (ĐƠN GIẢN NHẤT)
```bash
python3 demo_custom.py
```

**Để thay đổi hệ phương trình:**
1. Mở file `demo_custom.py`
2. Sửa ma trận A và vector b
3. Chạy lại

**Ví dụ:** Giải hệ phương trình:
```
x + y = 1
x + 2y = 2
x + 3y = 2
```

Trong file `demo_custom.py`:
```python
A = np.array([
    [1, 1],      # x + y
    [1, 2],      # x + 2y
    [1, 3]       # x + 3y
], dtype=float)

b = np.array([1, 2, 2], dtype=float)
```

### Cách 3: Sử dụng trong code Python khác
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

### Cách 4: Sử dụng từng phương pháp riêng lẻ
```python
import numpy as np
from QR import LeastSquaresSolver

A = np.array([[1, 1], [1, 2], [1, 3]], dtype=float)
b = np.array([1, 2, 2], dtype=float)

# Giải bằng Householder
result = LeastSquaresSolver.solve_qr(A, b, method='householder')

print(f"Nghiệm: {result['x']}")
print(f"Ma trận Q:\n{result['Q']}")
print(f"Ma trận R:\n{result['R']}")
print(f"Thời gian: {result['time']*1000:.4f} ms")
```

## 📊 Kết quả hiển thị

Khi chạy `solve_system()`, chương trình sẽ hiển thị:

### 1. Dữ liệu đầu vào
- Ma trận A
- Vector b
- Số điều kiện κ(A)

### 2. Kết quả từng phương pháp
- **Ma trận Q** (ma trận trực giao)
- **Ma trận R** (ma trận tam giác trên)
- **Nghiệm x**
- **Độ chính xác**: ||Ax - b|| và ||Q^T Q - I||
- **Thời gian thực thi** (ms)

### 3. Bảng so sánh
- **So sánh thời gian** giữa 4 phương pháp
- **So sánh độ chính xác**
- **Kiểm tra tính nhất quán** của nghiệm
- **So sánh với NumPy**

## 🎯 Các phương pháp

| Phương pháp | Ưu điểm | Nhược điểm |
|-------------|---------|------------|
| **CGS** | Nhanh nhất | Kém ổn định số |
| **MGS** | Cân bằng tốc độ & ổn định | - |
| **Householder** | Ổn định nhất (khuyến nghị) | Chậm hơn một chút |
| **Givens** | Tốt cho ma trận thưa | Chậm với ma trận dày |

## 📁 Cấu trúc file

```
TTKH/
├── QR.py              # Code chính với tất cả các thuật toán
├── demo_custom.py     # Demo đơn giản để người dùng tùy chỉnh
├── README.md          # File hướng dẫn này
└── BÁO CÁO TTKH.pdf   # Báo cáo
```

## 💡 Ví dụ nhanh

### Ví dụ 1: Hệ 3 phương trình, 2 ẩn
```python
A = np.array([[1, 1], [1, 2], [1, 3]], dtype=float)
b = np.array([1, 2, 2], dtype=float)
solve_system(A, b)
# Nghiệm: x = [0.6667, 0.5]
```

### Ví dụ 2: Hệ 4 phương trình, 3 ẩn
```python
A = np.array([[1, 2, 1], [2, 1, 3], [1, 1, 1], [3, 2, 1]], dtype=float)
b = np.array([5, 8, 3, 7], dtype=float)
solve_system(A, b)
# Nghiệm: x = [1.07, 1.09, 1.54]
```

## ⚡ So sánh hiệu năng

Thời gian thực thi trung bình (ma trận 3×2):
- CGS: ~0.05 ms ⚡ (Nhanh nhất)
- MGS: ~0.06 ms
- Givens: ~0.07 ms
- Householder: ~0.09 ms
- NumPy: ~0.14 ms

**Lưu ý:** Householder tuy chậm hơn nhưng ổn định nhất với ma trận ill-conditioned.

## 🔍 Kiểm tra code

Chạy test để đảm bảo code hoạt động đúng:
```bash
python3 QR.py
```

Kết quả mong đợi:
- ✅ Tất cả phương pháp cho nghiệm giống nhau
- ✅ Sai số ||Q^T Q - I|| < 10^-15
- ✅ Nghiệm khớp với NumPy
- ✅ Không có lỗi

## 📞 Hỗ trợ

Nếu gặp lỗi:
1. Kiểm tra NumPy đã cài đặt: `pip3 install numpy`
2. Kiểm tra Python version >= 3.6
3. Đảm bảo ma trận A có dtype=float

## 📝 Ghi chú

- Ma trận A có thể có nhiều hàng hơn cột (m > n) - Bài toán bình phương tối thiểu
- Nếu m = n và A khả nghịch, nghiệm là nghiệm chính xác
- Nếu m > n, nghiệm là nghiệm tối ưu theo nghĩa bình phương tối thiểu
