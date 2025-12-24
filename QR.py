import numpy as np
import time
from typing import Tuple, Dict

class QRDecomposition:
    """Class chứa các phương pháp phân rã QR"""
    
    @staticmethod
    def gram_schmidt_classical(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Phân rã QR bằng phương pháp Gram-Schmidt cổ điển (CGS)
        
        Args:
            A: Ma trận m×n
            
        Returns:
            Q: Ma trận m×n với các cột trực chuẩn
            R: Ma trận tam giác trên n×n
        """
        m, n = A.shape
        Q = np.zeros((m, n))
        R = np.zeros((n, n))
        
        for j in range(n):
            v = A[:, j].copy()
            
            # Trừ đi các thành phần chiếu lên các vector trước đó
            for i in range(j):
                R[i, j] = np.dot(Q[:, i], A[:, j])
                v = v - R[i, j] * Q[:, i]
            
            # Chuẩn hóa
            R[j, j] = np.linalg.norm(v)
            if R[j, j] > 1e-10:
                Q[:, j] = v / R[j, j]
            else:
                Q[:, j] = v
        
        return Q, R
    
    @staticmethod
    def gram_schmidt_modified(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Phân rã QR bằng phương pháp Gram-Schmidt cải tiến (MGS)
        Ổn định số hơn CGS
        
        Args:
            A: Ma trận m×n
            
        Returns:
            Q: Ma trận m×n với các cột trực chuẩn
            R: Ma trận tam giác trên n×n
        """
        m, n = A.shape
        Q = A.copy().astype(float)
        R = np.zeros((n, n))
        
        for j in range(n):
            # Loại bỏ dần các thành phần chiếu
            for i in range(j):
                R[i, j] = np.dot(Q[:, i], Q[:, j])
                Q[:, j] = Q[:, j] - R[i, j] * Q[:, i]
            
            # Chuẩn hóa
            R[j, j] = np.linalg.norm(Q[:, j])
            if R[j, j] > 1e-10:
                Q[:, j] = Q[:, j] / R[j, j]
        
        return Q, R
    
    @staticmethod
    def householder(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Phân rã QR bằng biến đổi Householder
        Phương pháp ổn định số nhất, được khuyến nghị cho thực tế
        
        Args:
            A: Ma trận m×n
            
        Returns:
            Q: Ma trận m×n với các cột trực chuẩn
            R: Ma trận tam giác trên n×n
        """
        m, n = A.shape
        Q = np.eye(m)
        R = A.copy().astype(float)
        
        for k in range(n):
            # Lấy cột k từ hàng k trở xuống
            x = R[k:, k]
            
            # Tính vector Householder
            e = np.zeros_like(x)
            e[0] = np.linalg.norm(x) * (1 if x[0] >= 0 else -1)
            u = x - e
            
            norm_u = np.linalg.norm(u)
            if norm_u > 1e-10:
                v = u / norm_u
                
                # Áp dụng phép phản xạ Householder: H = I - 2vv^T
                # R[k:, k:] = R[k:, k:] - 2 * v * (v^T * R[k:, k:])
                R[k:, k:] = R[k:, k:] - 2.0 * np.outer(v, np.dot(v, R[k:, k:]))
                
                # Cập nhật Q: Q = Q * H
                Q[:, k:] = Q[:, k:] - 2.0 * np.outer(np.dot(Q[:, k:], v), v)
        
        return Q[:, :n], R[:n, :]
    
    @staticmethod
    def givens(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Phân rã QR bằng phép quay Givens
        Tốt cho ma trận thưa và cập nhật từng phần
        
        Args:
            A: Ma trận m×n
            
        Returns:
            Q: Ma trận m×n với các cột trực chuẩn
            R: Ma trận tam giác trên n×n
        """
        m, n = A.shape
        Q = np.eye(m)
        R = A.copy().astype(float)
        
        for j in range(n):
            for i in range(m-1, j, -1):
                # Kiểm tra nếu phần tử dưới đường chéo đã bằng 0
                if abs(R[i, j]) < 1e-10:
                    continue
                
                # Tính cos và sin cho phép quay Givens
                a = R[i-1, j]
                b = R[i, j]
                r = np.sqrt(a**2 + b**2)
                
                if r > 1e-10:
                    c = a / r
                    s = -b / r
                    
                    # Áp dụng phép quay lên R
                    G = np.eye(m)
                    G[i-1, i-1] = c
                    G[i, i] = c
                    G[i-1, i] = -s
                    G[i, i-1] = s
                    
                    R = G @ R
                    Q = Q @ G.T
        
        return Q[:, :n], R[:n, :]


class LeastSquaresSolver:
    """Class giải bài toán bình phương tối thiểu"""
    
    @staticmethod
    def back_substitution(R: np.ndarray, c: np.ndarray) -> np.ndarray:
        """
        Giải hệ phương trình tam giác trên Rx = c bằng phương pháp thế ngược
        
        Args:
            R: Ma trận tam giác trên n×n
            c: Vector n×1
            
        Returns:
            x: Nghiệm của hệ phương trình
        """
        n = len(c)
        x = np.zeros(n)
        
        for i in range(n-1, -1, -1):
            if abs(R[i, i]) < 1e-10:
                raise ValueError(f"Ma trận R suy biến tại hàng {i}")
            
            x[i] = (c[i] - np.dot(R[i, i+1:], x[i+1:])) / R[i, i]
        
        return x
    
    @staticmethod
    def solve_qr(A: np.ndarray, b: np.ndarray, method: str = 'householder') -> Dict:
        """
        Giải bài toán bình phương tối thiểu bằng phân rã QR
        
        Args:
            A: Ma trận m×n
            b: Vector m×1
            method: Phương pháp phân rã QR ('cgs', 'mgs', 'householder', 'givens')
            
        Returns:
            Dict chứa nghiệm và các thông tin khác
        """
        start_time = time.perf_counter()
        
        # Chọn phương pháp phân rã QR
        qr_methods = {
            'cgs': QRDecomposition.gram_schmidt_classical,
            'mgs': QRDecomposition.gram_schmidt_modified,
            'householder': QRDecomposition.householder,
            'givens': QRDecomposition.givens
        }
        
        if method not in qr_methods:
            raise ValueError(f"Phương pháp không hợp lệ. Chọn từ: {list(qr_methods.keys())}")
        
        # Bước 1: Phân rã QR
        Q, R = qr_methods[method](A)
        
        # Bước 2: Tính Q^T b
        c = Q.T @ b
        
        # Bước 3: Giải hệ tam giác trên Rx = c
        x = LeastSquaresSolver.back_substitution(R, c)
        
        # Tính sai số
        residual = A @ x - b
        residual_norm = np.linalg.norm(residual)
        
        # Kiểm tra độ trực giao của Q
        orthogonality_error = np.linalg.norm(Q.T @ Q - np.eye(Q.shape[1]))
        
        elapsed_time = time.perf_counter() - start_time
        
        return {
            'x': x,
            'Q': Q,
            'R': R,
            'residual': residual,
            'residual_norm': residual_norm,
            'orthogonality_error': orthogonality_error,
            'time': elapsed_time,
            'method': method
        }
    
    @staticmethod
    def solve_normal_equation(A: np.ndarray, b: np.ndarray) -> Dict:
        """
        Giải bài toán bình phương tối thiểu bằng phương trình chuẩn
        A^T A x = A^T b
        
        Args:
            A: Ma trận m×n
            b: Vector m×1
            
        Returns:
            Dict chứa nghiệm và các thông tin khác
        """
        start_time = time.perf_counter()
        
        # Tính A^T A và A^T b
        ATA = A.T @ A
        ATb = A.T @ b
        
        # Giải hệ phương trình
        x = np.linalg.solve(ATA, ATb)
        
        # Tính sai số
        residual = A @ x - b
        residual_norm = np.linalg.norm(residual)
        
        # Số điều kiện
        cond_A = np.linalg.cond(A)
        cond_ATA = np.linalg.cond(ATA)
        
        elapsed_time = time.perf_counter() - start_time
        
        return {
            'x': x,
            'residual': residual,
            'residual_norm': residual_norm,
            'cond_A': cond_A,
            'cond_ATA': cond_ATA,
            'time': elapsed_time,
            'method': 'normal_equation'
        }


def demo_example_3_4():
    """Demo với ví dụ 3.4 trong báo cáo"""
    print("="*70)
    print("VÍ DỤ 3.4 - BÀI TOÁN HỒI QUY TUYẾN TÍNH")
    print("="*70)
    
    # Dữ liệu từ ví dụ 3.4
    A = np.array([
        [1, 1],
        [1, 2],
        [1, 3]
    ], dtype=float)
    
    b = np.array([1, 2, 2], dtype=float)
    
    print("\nMa trận A:")
    print(A)
    print("\nVector b:")
    print(b)
    
    # Giải bằng các phương pháp khác nhau
    methods = ['householder', 'mgs', 'cgs', 'givens']
    results = {}
    
    print("\n" + "-"*70)
    print("KẾT QUẢ PHÂN RÃ QR VÀ GIẢI BÀI TOÁN")
    print("-"*70)
    
    for method in methods:
        results[method] = LeastSquaresSolver.solve_qr(A, b, method=method)
        
        print(f"\n{method.upper()}:")
        print(f"  Nghiệm x = {results[method]['x']}")
        print(f"  ||Ax - b|| = {results[method]['residual_norm']:.10f}")
        print(f"  ||Q^T Q - I|| = {results[method]['orthogonality_error']:.10e}")
        print(f"  Thời gian: {results[method]['time']*1000:.4f} ms")
    
    # So sánh với phương trình chuẩn
    result_normal = LeastSquaresSolver.solve_normal_equation(A, b)
    print(f"\nNORMAL EQUATION:")
    print(f"  Nghiệm x = {result_normal['x']}")
    print(f"  ||Ax - b|| = {result_normal['residual_norm']:.10f}")
    print(f"  κ(A) = {result_normal['cond_A']:.4f}")
    print(f"  κ(A^T A) = {result_normal['cond_ATA']:.4f}")
    print(f"  Thời gian: {result_normal['time']*1000:.4f} ms")
    
    # So sánh với numpy
    x_numpy = np.linalg.lstsq(A, b, rcond=None)[0]
    print(f"\nNUMPY LSTSQ (tham chiếu):")
    print(f"  Nghiệm x = {x_numpy}")
    print(f"  ||Ax - b|| = {np.linalg.norm(A @ x_numpy - b):.10f}")
    
    print("\n" + "="*70)
    print("Nghiệm lý thuyết: x = [2/3, 1/2] = [0.66666667, 0.5]")
    print("="*70)


def demo_ill_conditioned():
    """Demo với ma trận ill-conditioned"""
    print("\n\n" + "="*70)
    print("DEMO VỚI MA TRẬN ILL-CONDITIONED")
    print("="*70)
    
    # Tạo ma trận Hilbert (ill-conditioned)
    n = 5
    A = np.array([[1.0/(i+j+1) for j in range(n)] for i in range(n+2)])
    b = A @ np.ones(n)
    
    print(f"\nMa trận Hilbert {A.shape[0]}×{n}")
    print(f"Số điều kiện: κ(A) = {np.linalg.cond(A):.2e}")
    
    # Giải bằng QR (Householder)
    result_qr = LeastSquaresSolver.solve_qr(A, b, method='householder')
    
    # Giải bằng Normal Equation
    result_normal = LeastSquaresSolver.solve_normal_equation(A, b)
    
    print("\nSo sánh sai số:")
    print(f"  QR (Householder):  ||x - x_true|| = {np.linalg.norm(result_qr['x'] - 1):.10e}")
    print(f"  Normal Equation:   ||x - x_true|| = {np.linalg.norm(result_normal['x'] - 1):.10e}")
    print(f"\n  κ(A^T A) / κ(A) = {result_normal['cond_ATA'] / result_normal['cond_A']:.2f}")
    print(f"  (Lý thuyết: ≈ κ(A) = {result_normal['cond_A']:.2f})")


def demo_linear_regression():
    """Demo với bài toán hồi quy tuyến tính thực tế"""
    print("\n\n" + "="*70)
    print("DEMO HỒI QUY TUYẾN TÍNH VỚI DỮ LIỆU NHIỄU")
    print("="*70)
    
    # Tạo dữ liệu tổng hợp: y = 2 + 3x + nhiễu
    np.random.seed(42)
    n_points = 50
    x_data = np.linspace(0, 10, n_points)
    y_true = 2 + 3 * x_data
    y_noisy = y_true + np.random.normal(0, 2, n_points)
    
    # Ma trận thiết kế cho mô hình y = β₀ + β₁x
    A = np.column_stack([np.ones(n_points), x_data])
    b = y_noisy
    
    # Giải bằng QR
    result = LeastSquaresSolver.solve_qr(A, b, method='householder')
    
    beta_0, beta_1 = result['x']
    
    print(f"\nDữ liệu: {n_points} điểm với nhiễu σ = 2")
    print(f"Mô hình thực: y = 2 + 3x")
    print(f"\nKết quả hồi quy:")
    print(f"  β₀ (intercept) = {beta_0:.4f}  (thực: 2.0)")
    print(f"  β₁ (slope)     = {beta_1:.4f}  (thực: 3.0)")
    print(f"  ||Ax - b||     = {result['residual_norm']:.4f}")
    print(f"  RMSE           = {result['residual_norm'] / np.sqrt(n_points):.4f}")


def solve_system(A: np.ndarray, b: np.ndarray):
    """
    Giải hệ phương trình Ax = b và hiển thị kết quả chi tiết
    So sánh thời gian giữa các phương pháp QR
    
    Args:
        A: Ma trận hệ số m×n
        b: Vector vế phải m×1
    """
    print("\n" + "="*80)
    print("GIẢI HỆ PHƯƠNG TRÌNH Ax = b BẰNG PHÂN RÃ QR")
    print("="*80)
    
    # Hiển thị input
    print("\n📊 DỮ LIỆU ĐẦU VÀO:")
    print("-" * 80)
    print(f"Ma trận A ({A.shape[0]}×{A.shape[1]}):")
    print(A)
    print(f"\nVector b ({len(b)}×1):")
    print(b)
    print(f"\nSố điều kiện κ(A) = {np.linalg.cond(A):.4e}")
    
    # Danh sách các phương pháp
    methods = ['householder', 'mgs', 'cgs', 'givens']
    results = {}
    
    print("\n" + "="*80)
    print("⚙️  PHÂN RÃ QR VÀ GIẢI HỆ PHƯƠNG TRÌNH")
    print("="*80)
    
    # Giải bằng từng phương pháp
    for method in methods:
        results[method] = LeastSquaresSolver.solve_qr(A, b, method=method)
        
        print(f"\n{'─'*80}")
        print(f"🔹 PHƯƠNG PHÁP: {method.upper()}")
        print(f"{'─'*80}")
        
        # Hiển thị ma trận Q
        print(f"\nMa trận Q ({results[method]['Q'].shape[0]}×{results[method]['Q'].shape[1]}):")
        print(results[method]['Q'])
        
        # Hiển thị ma trận R
        print(f"\nMa trận R ({results[method]['R'].shape[0]}×{results[method]['R'].shape[1]}):")
        print(results[method]['R'])
        
        # Hiển thị nghiệm
        print(f"\n✅ NGHIỆM x:")
        print(results[method]['x'])
        
        # Thông tin về độ chính xác
        print(f"\n📈 ĐỘ CHÍNH XÁC:")
        print(f"  • ||Ax - b||           = {results[method]['residual_norm']:.10e}")
        print(f"  • ||Q^T Q - I||        = {results[method]['orthogonality_error']:.10e}")
        print(f"  • ⏱️  Thời gian         = {results[method]['time']*1000:.4f} ms")
    
    # Bảng so sánh thời gian
    print("\n" + "="*80)
    print("⏱️  BẢNG SO SÁNH THỜI GIAN THỰC THI")
    print("="*80)
    print(f"{'Phương pháp':<20} {'Thời gian (ms)':<20} {'Tốc độ tương đối':<20}")
    print("-" * 80)
    
    # Tìm phương pháp nhanh nhất
    min_time = min(r['time'] for r in results.values())
    
    # Kiểm tra nếu thời gian quá nhỏ (có thể bằng 0 do làm tròn)
    if min_time < 1e-9:  # Nhỏ hơn 1 nanosecond
        print("\n⚠️  Cảnh báo: Thời gian đo quá nhỏ, kết quả có thể không chính xác.")
        print("   Khuyến nghị: Sử dụng ma trận lớn hơn để đo thời gian chính xác hơn.\n")
    
    for method in methods:
        time_ms = results[method]['time'] * 1000
        
        # Xử lý trường hợp min_time = 0 hoặc quá nhỏ
        if min_time > 0:
            relative_speed = results[method]['time'] / min_time
        else:
            relative_speed = 1.0  # Nếu tất cả đều = 0, coi như bằng nhau
        
        fastest = " ⚡ (Nhanh nhất)" if results[method]['time'] == min_time else ""
        print(f"{method.upper():<20} {time_ms:<20.4f} {relative_speed:<20.2f}x{fastest}")
    
    # So sánh độ chính xác
    print("\n" + "="*80)
    print("📊 BẢNG SO SÁNH ĐỘ CHÍNH XÁC")
    print("="*80)
    print(f"{'Phương pháp':<20} {'||Ax - b||':<25} {'||Q^T Q - I||':<25}")
    print("-" * 80)
    
    for method in methods:
        residual = results[method]['residual_norm']
        ortho_error = results[method]['orthogonality_error']
        print(f"{method.upper():<20} {residual:<25.10e} {ortho_error:<25.10e}")
    
    # Kiểm tra tính nhất quán của nghiệm
    print("\n" + "="*80)
    print("🔍 KIỂM TRA TÍNH NHẤT QUÁN CỦA NGHIỆM")
    print("="*80)
    
    x_ref = results['householder']['x']
    print(f"Nghiệm tham chiếu (Householder): {x_ref}")
    print("\nSai khác so với Householder:")
    
    for method in methods:
        if method != 'householder':
            diff = np.linalg.norm(results[method]['x'] - x_ref)
            print(f"  • {method.upper():<15}: ||x - x_ref|| = {diff:.10e}")
    
    # So sánh với NumPy
    print("\n" + "="*80)
    print("🔬 SO SÁNH VỚI NUMPY.LINALG.LSTSQ")
    print("="*80)
    
    start_time = time.perf_counter()
    x_numpy = np.linalg.lstsq(A, b, rcond=None)[0]
    numpy_time = time.perf_counter() - start_time
    
    print(f"Nghiệm NumPy: {x_numpy}")
    print(f"Thời gian: {numpy_time*1000:.4f} ms")
    print(f"Sai khác với Householder: ||x_numpy - x_householder|| = {np.linalg.norm(x_numpy - x_ref):.10e}")
    
    print("\n" + "="*80)
    print("✅ HOÀN THÀNH")
    print("="*80)


if __name__ == "__main__":
    # ============================================================================
    # PHẦN 1: DEMO VÍ DỤ TỪ BÁO CÁO
    # ============================================================================
    demo_example_3_4()
    demo_ill_conditioned()
    demo_linear_regression()
    
    # ============================================================================
    # PHẦN 2: GIẢI HỆ PHƯƠNG TRÌNH TÙY CHỈNH
    # ============================================================================
    
    # Ví dụ 1: Hệ phương trình đơn giản 3x2
    print("\n\n" + "🔷"*40)
    print("VÍ DỤ 1: HỆ PHƯƠNG TRÌNH ĐƠN GIẢN")
    print("🔷"*40)
    
    A1 = np.array([
        [1, 1],
        [1, 2],
        [1, 3]
    ], dtype=float)
    
    b1 = np.array([1, 2, 2], dtype=float)
    
    solve_system(A1, b1)
    
    # Ví dụ 2: Hệ phương trình 4x3
    print("\n\n" + "🔷"*40)
    print("VÍ DỤ 2: HỆ PHƯƠNG TRÌNH 4×3")
    print("🔷"*40)
    
    A2 = np.array([
        [1, 2, 1],
        [2, 1, 3],
        [1, 1, 1],
        [3, 2, 1]
    ], dtype=float)
    
    b2 = np.array([5, 8, 3, 7], dtype=float)
    
    solve_system(A2, b2)
    
    # ============================================================================
    # HƯỚNG DẪN SỬ DỤNG
    # ============================================================================
    print("\n\n" + "📖"*40)
    print("HƯỚNG DẪN SỬ DỤNG HÀM solve_system()")
    print("📖"*40)
    print("""
Để giải hệ phương trình của bạn, sử dụng như sau:

import numpy as np
from QR import solve_system

# Bước 1: Định nghĩa ma trận A và vector b
A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
], dtype=float)

b = np.array([7, 8, 9], dtype=float)

# Bước 2: Gọi hàm solve_system
solve_system(A, b)

Hàm sẽ tự động:
  ✅ Hiển thị ma trận Q và R từ 4 phương pháp QR
  ✅ Hiển thị nghiệm x của hệ phương trình
  ✅ So sánh thời gian thực thi giữa các phương pháp
  ✅ So sánh độ chính xác giữa các phương pháp
    """)
    
    print("\n" + "="*80)
    print("✅ HOÀN THÀNH TẤT CẢ CÁC DEMO")
    print("="*80)