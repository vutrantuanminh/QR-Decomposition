#!/bin/bash

# Script tự động upload project lên GitHub
# Tác giả: Auto-generated
# Ngày: 2025-12-23

echo "========================================================================"
echo "🚀 SCRIPT TỰ ĐỘNG UPLOAD LÊN GITHUB"
echo "========================================================================"
echo ""

# Kiểm tra Git đã cài đặt chưa
if ! command -v git &> /dev/null; then
    echo "❌ Git chưa được cài đặt!"
    echo "Cài đặt bằng lệnh: sudo apt install git"
    exit 1
fi

echo "✅ Git đã được cài đặt: $(git --version)"
echo ""

# Hỏi thông tin GitHub
echo "📝 Nhập thông tin GitHub của bạn:"
echo "------------------------------------------------------------------------"
read -p "GitHub username: " GITHUB_USER
read -p "Repository name (ví dụ: QR-Decomposition): " REPO_NAME

echo ""
echo "------------------------------------------------------------------------"
echo "Thông tin repository:"
echo "  URL: https://github.com/$GITHUB_USER/$REPO_NAME"
echo "------------------------------------------------------------------------"
read -p "Thông tin đã đúng? (y/n): " CONFIRM

if [ "$CONFIRM" != "y" ]; then
    echo "❌ Hủy bỏ. Vui lòng chạy lại script!"
    exit 1
fi

echo ""
echo "========================================================================"
echo "⚙️  BẮT ĐẦU UPLOAD"
echo "========================================================================"

# Bước 1: Kiểm tra xem đã init chưa
if [ ! -d ".git" ]; then
    echo ""
    echo "📦 Bước 1: Khởi tạo Git repository..."
    git init
    echo "✅ Đã khởi tạo Git repository"
else
    echo "✅ Git repository đã tồn tại"
fi

# Bước 2: Cấu hình Git (nếu chưa có)
echo ""
echo "🔧 Bước 2: Kiểm tra cấu hình Git..."
GIT_USER=$(git config --global user.name)
GIT_EMAIL=$(git config --global user.email)

if [ -z "$GIT_USER" ] || [ -z "$GIT_EMAIL" ]; then
    echo "⚠️  Chưa cấu hình Git user"
    read -p "Nhập tên của bạn: " USER_NAME
    read -p "Nhập email của bạn: " USER_EMAIL
    git config --global user.name "$USER_NAME"
    git config --global user.email "$USER_EMAIL"
    echo "✅ Đã cấu hình Git user"
else
    echo "✅ Git đã được cấu hình:"
    echo "   Name: $GIT_USER"
    echo "   Email: $GIT_EMAIL"
fi

# Bước 3: Add files
echo ""
echo "📁 Bước 3: Thêm tất cả file vào Git..."
git add .
echo "✅ Đã thêm tất cả file"

# Bước 4: Commit
echo ""
echo "💾 Bước 4: Commit changes..."
COMMIT_MSG="Initial commit: QR Decomposition project with interactive demo"
git commit -m "$COMMIT_MSG"
echo "✅ Đã commit với message: $COMMIT_MSG"

# Bước 5: Kiểm tra remote
echo ""
echo "🔗 Bước 5: Kết nối với GitHub repository..."
if git remote | grep -q "origin"; then
    echo "⚠️  Remote 'origin' đã tồn tại. Xóa và tạo lại..."
    git remote remove origin
fi

REPO_URL="https://github.com/$GITHUB_USER/$REPO_NAME.git"
git remote add origin "$REPO_URL"
echo "✅ Đã kết nối với: $REPO_URL"

# Bước 6: Đổi tên branch thành main
echo ""
echo "🌿 Bước 6: Đổi tên branch thành 'main'..."
git branch -M main
echo "✅ Đã đổi tên branch thành 'main'"

# Bước 7: Push lên GitHub
echo ""
echo "🚀 Bước 7: Push lên GitHub..."
echo "⚠️  Bạn sẽ được yêu cầu nhập GitHub credentials"
echo "   - Username: $GITHUB_USER"
echo "   - Password: Dùng Personal Access Token (không phải password thường)"
echo ""
echo "📖 Cách tạo Personal Access Token:"
echo "   1. Vào: https://github.com/settings/tokens"
echo "   2. Click 'Generate new token (classic)'"
echo "   3. Chọn quyền 'repo'"
echo "   4. Copy token và paste vào đây"
echo ""
read -p "Nhấn Enter để tiếp tục..."

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================================================"
    echo "✅ UPLOAD THÀNH CÔNG!"
    echo "========================================================================"
    echo ""
    echo "🎉 Repository của bạn:"
    echo "   https://github.com/$GITHUB_USER/$REPO_NAME"
    echo ""
    echo "📝 Các file đã upload:"
    echo "   - QR.py"
    echo "   - demo_interactive.py"
    echo "   - demo_custom.py"
    echo "   - README.md"
    echo "   - Các file hướng dẫn khác"
    echo "   - BÁO CÁO TTKH.pdf"
    echo ""
    echo "🔄 Để cập nhật sau này, chạy:"
    echo "   git add ."
    echo "   git commit -m 'Mô tả thay đổi'"
    echo "   git push"
    echo ""
else
    echo ""
    echo "========================================================================"
    echo "❌ UPLOAD THẤT BẠI"
    echo "========================================================================"
    echo ""
    echo "Có thể do:"
    echo "  1. Repository chưa được tạo trên GitHub"
    echo "  2. Sai username/password"
    echo "  3. Chưa có quyền truy cập"
    echo ""
    echo "📖 Xem hướng dẫn chi tiết trong file: HUONG_DAN_GITHUB.md"
    echo ""
    exit 1
fi
