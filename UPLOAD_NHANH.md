# 🚀 UPLOAD LÊN GITHUB - HƯỚNG DẪN NHANH

## ⚡ CÁCH NHANH NHẤT - Dùng Script Tự Động

### Bước 1: Tạo repository trên GitHub
1. Vào https://github.com
2. Click **"New"** → **"New repository"**
3. Đặt tên: `QR-Decomposition` (hoặc tên khác)
4. Chọn **Public** hoặc **Private**
5. **KHÔNG** tick "Initialize with README"
6. Click **"Create repository"**

### Bước 2: Chạy script tự động
```bash
cd /home/oc/Downloads/TTKH
bash upload_github.sh
```

### Bước 3: Nhập thông tin khi được hỏi
- GitHub username: `tên_user_của_bạn`
- Repository name: `QR-Decomposition`

### Bước 4: Nhập credentials
- Username: `tên_user_của_bạn`
- Password: **Personal Access Token** (KHÔNG phải password thường!)

---

## 🔐 Tạo Personal Access Token

### Cách tạo:
1. Vào: https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Đặt tên: `QR-Project-Upload`
4. Chọn quyền: ✅ **repo** (tick tất cả)
5. Click **"Generate token"**
6. **COPY TOKEN** (chỉ hiển thị 1 lần!)
7. Dùng token này thay cho password khi push

---

## 📋 HOẶC Upload Thủ Công (Từng Bước)

### Bước 1: Khởi tạo Git
```bash
cd /home/oc/Downloads/TTKH
git init
```

### Bước 2: Cấu hình Git (lần đầu)
```bash
git config --global user.name "Tên của bạn"
git config --global user.email "email@example.com"
```

### Bước 3: Add và Commit
```bash
git add .
git commit -m "Initial commit: QR Decomposition project"
```

### Bước 4: Kết nối GitHub
**Thay USERNAME và REPO_NAME:**
```bash
git remote add origin https://github.com/USERNAME/REPO_NAME.git
git branch -M main
```

### Bước 5: Push
```bash
git push -u origin main
```

---

## 🌐 HOẶC Upload Trên Web (Đơn Giản Nhất)

### Bước 1: Tạo repository trên GitHub (như trên)

### Bước 2: Upload files
1. Vào repository vừa tạo
2. Click **"uploading an existing file"**
3. Kéo thả tất cả file vào (trừ `__pycache__`)
4. Click **"Commit changes"**

**Xong!** ✅

---

## ✅ Kiểm Tra Sau Khi Upload

Truy cập: `https://github.com/USERNAME/REPO_NAME`

Kiểm tra các file:
- ✅ QR.py
- ✅ demo_interactive.py
- ✅ demo_custom.py
- ✅ README.md
- ✅ HUONG_DAN_GITHUB.md
- ✅ CACH_CHAY.md
- ✅ BÁO CÁO TTKH.pdf

---

## 🔄 Cập Nhật Sau Này

```bash
cd /home/oc/Downloads/TTKH
git add .
git commit -m "Cập nhật code"
git push
```

---

## 🆘 Lỗi Thường Gặp

### Lỗi: "Permission denied"
→ Dùng Personal Access Token thay vì password

### Lỗi: "Repository not found"
→ Kiểm tra lại tên repository và username

### Lỗi: "failed to push"
→ Repository chưa được tạo trên GitHub

---

## 📞 TÓM TẮT

### Cách 1 - Script (KHUYẾN NGHỊ):
```bash
bash upload_github.sh
```

### Cách 2 - Thủ công:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/USER/REPO.git
git push -u origin main
```

### Cách 3 - Web:
Upload trực tiếp trên GitHub.com

---

**Chọn cách nào cũng được! Chúc bạn thành công! 🎉**
