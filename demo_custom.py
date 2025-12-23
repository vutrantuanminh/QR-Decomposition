#!/usr/bin/env python3
"""
Demo đơn giản để giải hệ phương trình Ax = b
Chỉ cần thay đổi ma trận A và vector b bên dưới
"""

import numpy as np
from QR import solve_system

# ============================================================================
# NHẬP HỆ PHƯƠNG TRÌNH CỦA BẠN Ở ĐÂY
# ============================================================================

# Ví dụ: Giải hệ phương trình
# x + y = 1
# x + 2y = 2
# x + 3y = 2

A = np.array([
    [1, 1],      # Hệ số của phương trình 1: x + y
    [1, 2],      # Hệ số của phương trình 2: x + 2y
    [1, 3]       # Hệ số của phương trình 3: x + 3y
], dtype=float)

b = np.array([1, 2, 2], dtype=float)  # Vế phải của các phương trình

# ============================================================================
# GIẢI HỆ PHƯƠNG TRÌNH
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("GIẢI HỆ PHƯƠNG TRÌNH TÙY CHỈNH")
    print("="*80)
    
    # Gọi hàm giải hệ phương trình
    solve_system(A, b)
    
    print("\n" + "="*80)
    print("💡 HƯỚNG DẪN:")
    print("="*80)
    print("""
Để giải hệ phương trình của bạn:
1. Mở file demo_custom.py
2. Thay đổi ma trận A và vector b
3. Chạy lại: python3 demo_custom.py

Ví dụ khác:
-----------
Giải hệ:
  2x + 3y = 5
  4x + 5y = 8
  6x + 7y = 11

A = np.array([
    [2, 3],
    [4, 5],
    [6, 7]
], dtype=float)

b = np.array([5, 8, 11], dtype=float)
    """)
