# Phân Rã QR và Giải Bài Toán Bình Phương Tối Thiểu

Chương trình Python giải hệ phương trình **Ax = b** bằng phương pháp phân rã QR với 4 thuật toán khác nhau.

## 🚀 Cài Đặt

### Yêu cầu:
- Python 3.x
- NumPy

```bash
pip install numpy
```

## 📖 Cách Sử Dụng

### 1️⃣ Demo Tương Tác - Nhập từ bàn phím (KHUYẾN NGHỊ)

```bash
python3 demo_interactive.py
```

**Các bước:**
1. Chọn `1` để nhập hệ phương trình
2. Nhập số hàng `m` và số cột `n`
3. Nhập từng hàng của ma trận A (các số cách nhau bởi dấu **CÁCH**)
4. Nhập vector b
5. Xem kết quả

**Ví dụ nhập:**
```
Nhập số hàng (m): 3
Nhập số cột (n): 2
Hàng 1: 1 1
Hàng 2: 1 2
Hàng 3: 1 3
Vector b: 1 2 2
```

### 2️⃣ Demo Đơn Giản - Sửa code

```bash
python3 demo_custom.py
```

Mở file `demo_custom.py`, sửa ma trận A và vector b, rồi chạy lại.

### 3️⃣ Chạy Tất Cả Demo Mẫu

```bash
python3 QR.py
```

Chạy tất cả ví dụ từ báo cáo và demo mẫu.

### 4️⃣ Sử Dụng Trong Code Python

```python
import numpy as np
from QR import solve_system

# Định nghĩa hệ phương trình
A = np.array([[1, 1], [1, 2], [1, 3]], dtype=float)
b = np.array([1, 2, 2], dtype=float)

# Giải và hiển thị kết quả
solve_system(A, b)
```

## 🎯 Các Phương Pháp

Chương trình hỗ trợ 4 phương pháp phân rã QR:

| Phương pháp | Tốc độ | Độ ổn định | Khuyến nghị |
|-------------|--------|------------|-------------|
| **CGS** (Classical Gram-Schmidt) | ⚡⚡⚡ Nhanh nhất | ⭐⭐ | Ma trận tốt |
| **MGS** (Modified Gram-Schmidt) | ⚡⚡ Nhanh | ⭐⭐⭐ | Cân bằng |
| **Householder** | ⚡ Trung bình | ⭐⭐⭐⭐ | **Tốt nhất** |
| **Givens** | ⚡ Trung bình | ⭐⭐⭐ | Ma trận thưa |

## 📊 Kết Quả Hiển Thị

Khi chạy `solve_system()`, chương trình sẽ hiển thị:

- ✅ **Ma trận Q** (ma trận trực giao)
- ✅ **Ma trận R** (ma trận tam giác trên)
- ✅ **Nghiệm x**
- ✅ **Độ chính xác**: ||Ax - b|| và ||Q^T Q - I||
- ✅ **Thời gian thực thi** (ms)
- ✅ **Bảng so sánh thời gian** giữa 4 phương pháp
- ✅ **Bảng so sánh độ chính xác**
- ✅ **So sánh với NumPy**

## 📁 Cấu Trúc Thư Mục

```
├── QR.py                   # Code chính với tất cả thuật toán
├── demo_interactive.py     # Demo tương tác - Nhập từ bàn phím
├── demo_custom.py          # Demo đơn giản - Sửa code
├── README.md               # File này
└── BÁO CÁO TTKH.pdf        # Báo cáo
```

## 💡 Ví Dụ Nhanh

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

## 🎓 Tính Năng

- ✅ 4 phương pháp phân rã QR: CGS, MGS, Householder, Givens
- ✅ Giải bài toán bình phương tối thiểu
- ✅ Hiển thị ma trận Q và R
- ✅ Đo và so sánh thời gian thực thi
- ✅ So sánh độ chính xác
- ✅ Demo tương tác - Nhập từ bàn phím
- ✅ Kiểm tra tính nhất quán của nghiệm
- ✅ So sánh với NumPy

## 📝 Ghi Chú

- Ma trận A có thể có nhiều hàng hơn cột (m > n) - Bài toán bình phương tối thiểu
- Nếu m = n và A khả nghịch, nghiệm là nghiệm chính xác
- Nếu m > n, nghiệm là nghiệm tối ưu theo nghĩa bình phương tối thiểu
- Householder là phương pháp ổn định nhất, khuyến nghị cho ma trận ill-conditioned

## 📞 Liên Hệ

- GitHub: https://github.com/vutrantuanminh/QR-Decomposition
- Tác giả: Vũ Trần Tuấn Minh

---

**Chúc bạn sử dụng thành công! 🎉**
