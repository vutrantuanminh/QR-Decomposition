# 🚀 HƯỚNG DẪN UPLOAD LÊN GITHUB

## 📋 Chuẩn bị

### Bước 1: Tạo repository mới trên GitHub
1. Truy cập https://github.com
2. Đăng nhập vào tài khoản của bạn
3. Click nút **"New"** hoặc **"+"** → **"New repository"**
4. Đặt tên repository: `QR-Decomposition` (hoặc tên bạn muốn)
5. Chọn **Public** hoặc **Private**
6. **KHÔNG** chọn "Initialize this repository with a README"
7. Click **"Create repository"**

---

## 🔧 Cách 1: Upload bằng dòng lệnh (KHUYẾN NGHỊ)

### Bước 1: Khởi tạo Git repository
```bash
cd /home/oc/Downloads/TTKH
git init
```

### Bước 2: Cấu hình Git (nếu chưa làm)
```bash
git config --global user.name "Tên của bạn"
git config --global user.email "email@example.com"
```

### Bước 3: Thêm tất cả file vào Git
```bash
git add .
```

### Bước 4: Commit
```bash
git commit -m "Initial commit: QR Decomposition project"
```

### Bước 5: Kết nối với GitHub repository
**Thay `USERNAME` và `REPO_NAME` bằng thông tin của bạn:**
```bash
git remote add origin https://github.com/USERNAME/REPO_NAME.git
```

Ví dụ:
```bash
git remote add origin https://github.com/john/QR-Decomposition.git
```

### Bước 6: Push lên GitHub
```bash
git branch -M main
git push -u origin main
```

**Lưu ý:** Bạn sẽ được yêu cầu nhập username và password (hoặc Personal Access Token)

---

## 🔧 Cách 2: Upload bằng GitHub Desktop

### Bước 1: Tải GitHub Desktop
- Truy cập: https://desktop.github.com/
- Tải và cài đặt

### Bước 2: Đăng nhập
- Mở GitHub Desktop
- Đăng nhập vào tài khoản GitHub

### Bước 3: Add repository
- File → Add Local Repository
- Chọn thư mục: `/home/oc/Downloads/TTKH`
- Click "Create Repository"

### Bước 4: Commit và Push
- Nhập commit message
- Click "Commit to main"
- Click "Publish repository"

---

## 🔧 Cách 3: Upload trực tiếp trên web (ĐƠN GIẢN NHẤT)

### Bước 1: Tạo repository trên GitHub (như hướng dẫn ở trên)

### Bước 2: Upload files
1. Vào repository vừa tạo
2. Click **"uploading an existing file"** hoặc **"Add file"** → **"Upload files"**
3. Kéo thả tất cả file từ thư mục `TTKH` vào
4. Nhập commit message: "Initial commit"
5. Click **"Commit changes"**

**Lưu ý:** Cách này đơn giản nhưng không upload được thư mục `__pycache__` (đã được loại bỏ trong .gitignore)

---

## 🔐 Xác thực với GitHub

### Nếu dùng HTTPS (khuyến nghị cho người mới):

#### Option 1: Personal Access Token (PAT)
1. Vào GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Chọn quyền: `repo` (full control)
4. Copy token (chỉ hiển thị 1 lần!)
5. Khi push, dùng token thay cho password

#### Option 2: GitHub CLI
```bash
# Cài đặt GitHub CLI
sudo apt install gh

# Đăng nhập
gh auth login
```

### Nếu dùng SSH:
```bash
# Tạo SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Copy public key
cat ~/.ssh/id_ed25519.pub

# Thêm vào GitHub: Settings → SSH and GPG keys → New SSH key
```

Sau đó dùng SSH URL:
```bash
git remote add origin git@github.com:USERNAME/REPO_NAME.git
```

---

## 📝 Script tự động (NHANH NHẤT)

Tôi đã tạo sẵn script cho bạn. Chạy:

```bash
cd /home/oc/Downloads/TTKH
bash upload_github.sh
```

Script sẽ hỏi:
1. GitHub username
2. Repository name
3. Tự động init, add, commit, push

---

## ✅ Kiểm tra sau khi upload

1. Truy cập: `https://github.com/USERNAME/REPO_NAME`
2. Kiểm tra các file:
   - ✅ QR.py
   - ✅ demo_interactive.py
   - ✅ demo_custom.py
   - ✅ README.md
   - ✅ Các file .md khác
   - ✅ BÁO CÁO TTKH.pdf

---

## 🔄 Cập nhật sau này

Khi có thay đổi:
```bash
cd /home/oc/Downloads/TTKH
git add .
git commit -m "Mô tả thay đổi"
git push
```

---

## 🆘 Troubleshooting

### Lỗi: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/USERNAME/REPO_NAME.git
```

### Lỗi: "Permission denied"
- Kiểm tra username/password
- Hoặc dùng Personal Access Token thay vì password

### Lỗi: "failed to push some refs"
```bash
git pull origin main --rebase
git push origin main
```

---

## 📖 Tóm tắt nhanh

### Cách đơn giản nhất (Web):
1. Tạo repo trên GitHub
2. Upload files trực tiếp trên web

### Cách chuyên nghiệp (CLI):
```bash
cd /home/oc/Downloads/TTKH
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

### Cách tự động (Script):
```bash
bash upload_github.sh
```

---

**Chọn cách nào phù hợp với bạn và bắt đầu! 🚀**
