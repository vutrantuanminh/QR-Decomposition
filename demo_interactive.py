#!/usr/bin/env python3
"""
Demo tương tác - Nhập hệ phương trình từ bàn phím
"""

import numpy as np
from QR import solve_system

def input_matrix():
    """Nhập ma trận A từ bàn phím"""
    print("\n" + "="*80)
    print("NHẬP MA TRẬN A")
    print("="*80)
    
    while True:
        try:
            m = int(input("Nhập số hàng của ma trận A (m): "))
            n = int(input("Nhập số cột của ma trận A (n): "))
            
            if m <= 0 or n <= 0:
                print("❌ Số hàng và số cột phải > 0. Vui lòng nhập lại!")
                continue
            
            if m < n:
                print(f"⚠️  Cảnh báo: m ({m}) < n ({n}) - Hệ có thể không có nghiệm duy nhất")
                confirm = input("Bạn có muốn tiếp tục? (y/n): ")
                if confirm.lower() != 'y':
                    continue
            
            break
        except ValueError:
            print("❌ Vui lòng nhập số nguyên hợp lệ!")
    
    print(f"\nNhập các phần tử của ma trận A ({m}×{n}):")
    print("Mỗi hàng nhập các số cách nhau bởi dấu cách")
    print("Ví dụ: 1 2 3")
    
    A = []
    for i in range(m):
        while True:
            try:
                row_input = input(f"Hàng {i+1}: ")
                row = [float(x) for x in row_input.split()]
                
                if len(row) != n:
                    print(f"❌ Cần {n} số, bạn nhập {len(row)} số. Vui lòng nhập lại!")
                    continue
                
                A.append(row)
                break
            except ValueError:
                print("❌ Vui lòng nhập các số hợp lệ, cách nhau bởi dấu cách!")
    
    return np.array(A, dtype=float)

def input_vector(m):
    """Nhập vector b từ bàn phím"""
    print("\n" + "="*80)
    print("NHẬP VECTOR b")
    print("="*80)
    
    print(f"Nhập {m} phần tử của vector b (vế phải của hệ phương trình)")
    print("Các số cách nhau bởi dấu cách")
    print("Ví dụ: 1 2 3")
    
    while True:
        try:
            b_input = input(f"Vector b ({m} phần tử): ")
            b = [float(x) for x in b_input.split()]
            
            if len(b) != m:
                print(f"❌ Cần {m} số, bạn nhập {len(b)} số. Vui lòng nhập lại!")
                continue
            
            return np.array(b, dtype=float)
        except ValueError:
            print("❌ Vui lòng nhập các số hợp lệ, cách nhau bởi dấu cách!")

def show_examples():
    """Hiển thị các ví dụ mẫu"""
    print("\n" + "📚"*40)
    print("VÍ DỤ MẪU")
    print("📚"*40)
    
    print("""
VÍ DỤ 1: Hệ phương trình đơn giản
    x + y = 1
    x + 2y = 2
    x + 3y = 2

Nhập:
    m = 3, n = 2
    Hàng 1: 1 1
    Hàng 2: 1 2
    Hàng 3: 1 3
    Vector b: 1 2 2

VÍ DỤ 2: Hệ phương trình 4×3
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

VÍ DỤ 3: Hệ phương trình vuông 2×2
    2x + 3y = 5
    4x + 5y = 8

Nhập:
    m = 2, n = 2
    Hàng 1: 2 3
    Hàng 2: 4 5
    Vector b: 5 8
    """)

def main():
    """Hàm chính"""
    print("="*80)
    print("CHƯƠNG TRÌNH GIẢI HỆ PHƯƠNG TRÌNH Ax = b")
    print("Sử dụng phân rã QR với 4 phương pháp")
    print("="*80)
    
    while True:
        print("\n" + "🔷"*40)
        print("MENU")
        print("🔷"*40)
        print("1. Nhập hệ phương trình mới")
        print("2. Xem ví dụ mẫu")
        print("3. Thoát")
        
        choice = input("\nChọn (1/2/3): ").strip()
        
        if choice == '1':
            # Nhập ma trận A
            A = input_matrix()
            
            # Nhập vector b
            b = input_vector(A.shape[0])
            
            # Xác nhận
            print("\n" + "="*80)
            print("XÁC NHẬN DỮ LIỆU")
            print("="*80)
            print(f"\nMa trận A ({A.shape[0]}×{A.shape[1]}):")
            print(A)
            print(f"\nVector b ({len(b)}×1):")
            print(b)
            
            confirm = input("\nDữ liệu đã đúng? Bắt đầu giải? (y/n): ")
            
            if confirm.lower() == 'y':
                # Giải hệ phương trình
                solve_system(A, b)
                
                # Hỏi có muốn tiếp tục không
                print("\n" + "="*80)
                continue_choice = input("Bạn có muốn giải hệ phương trình khác? (y/n): ")
                if continue_choice.lower() != 'y':
                    break
            else:
                print("Hủy bỏ. Vui lòng nhập lại!")
        
        elif choice == '2':
            show_examples()
        
        elif choice == '3':
            print("\n" + "="*80)
            print("👋 Cảm ơn bạn đã sử dụng chương trình!")
            print("="*80)
            break
        
        else:
            print("❌ Lựa chọn không hợp lệ. Vui lòng chọn 1, 2 hoặc 3!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + "="*80)
        print("⚠️  Chương trình bị ngắt bởi người dùng (Ctrl+C)")
        print("="*80)
    except Exception as e:
        print(f"\n❌ Lỗi: {e}")
        print("Vui lòng kiểm tra lại dữ liệu đầu vào!")
