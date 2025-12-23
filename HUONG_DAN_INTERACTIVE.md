# HƯỚNG DẪN SỬ DỤNG DEMO TƯƠNG TÁC

## 🎯 Chạy chương trình

```bash
cd /home/oc/Downloads/TTKH
python3 demo_interactive.py
```

## 📝 Cách sử dụng

### Bước 1: Chọn menu
```
1. Nhập hệ phương trình mới
2. Xem ví dụ mẫu
3. Thoát
```

### Bước 2: Nhập ma trận A
```
Nhập số hàng của ma trận A (m): 3
Nhập số cột của ma trận A (n): 2
```

### Bước 3: Nhập từng hàng của ma trận A
```
Hàng 1: 1 1
Hàng 2: 1 2
Hàng 3: 1 3
```
**Lưu ý:** Các số cách nhau bởi dấu CÁCH

### Bước 4: Nhập vector b
```
Vector b (3 phần tử): 1 2 2
```

### Bước 5: Xác nhận và xem kết quả
Chương trình sẽ hiển thị:
- Ma trận Q và R từ 4 phương pháp
- Nghiệm x
- Bảng so sánh thời gian
- Bảng so sánh độ chính xác

## 📚 Ví dụ mẫu

### Ví dụ 1: Hệ 3×2
```
Hệ phương trình:
  x + y = 1
  x + 2y = 2
  x + 3y = 2

Nhập:
  m = 3, n = 2
  Hàng 1: 1 1
  Hàng 2: 1 2
  Hàng 3: 1 3
  Vector b: 1 2 2

Nghiệm: x = [0.6667, 0.5]
```

### Ví dụ 2: Hệ 4×3
```
Hệ phương trình:
  x + 2y + z = 5
  2x + y + 3z = 8
  x + y + z = 3
  3x + 2y + z = 7

Nhập:
  m = 4, n = 3
  Hàng 1: 1 2 1
  Hàng 2: 2 1 3
  Hàng 3: 1 1 1
  Hàng 4: 3 2 1
  Vector b: 5 8 3 7

Nghiệm: x = [1.07, 1.09, 1.54]
```

### Ví dụ 3: Hệ vuông 2×2
```
Hệ phương trình:
  2x + 3y = 5
  4x + 5y = 8

Nhập:
  m = 2, n = 2
  Hàng 1: 2 3
  Hàng 2: 4 5
  Vector b: 5 8

Nghiệm: x = [-3.5, 4]
```

## 💡 Mẹo

1. **Các số cách nhau bởi dấu CÁCH**, không phải dấu phẩy
2. Có thể nhập số thập phân: `1.5 2.3 3.7`
3. Có thể nhập số âm: `-1 2 -3`
4. Nhấn `Ctrl+C` để thoát bất cứ lúc nào

## ⚠️ Lưu ý

- Nếu m < n (ít phương trình hơn ẩn), hệ có vô số nghiệm
- Nếu m = n (hệ vuông), có thể có nghiệm duy nhất
- Nếu m > n (nhiều phương trình hơn ẩn), tìm nghiệm bình phương tối thiểu

## 🚀 Demo nhanh

Chạy lệnh này và làm theo hướng dẫn:
```bash
python3 demo_interactive.py
```

Chọn `2` để xem ví dụ mẫu trước khi bắt đầu!
