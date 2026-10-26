# Tuần 13 — Modules · Packages · Dependencies · CLI · API/HTTP

Tuần 13 giúp bạn chuyển từ các chương trình đơn file sang cấu trúc Python dễ
đọc, chạy, kiểm tra và mở rộng hơn. Bạn sẽ tách logic cốt lõi khỏi CLI và HTTP,
đồng thời học cách kiểm tra phản hồi JSON mà không cần phụ thuộc mạng.

## Mục tiêu sau bài học

- Phân biệt module, package và entry point.
- Import hàm từ module khác và dùng `if __name__ == "__main__":`.
- Hiểu vai trò của môi trường ảo `.venv`, `python -m pip` và `pyproject.toml`.
- Dùng `argparse` để đọc tham số dòng lệnh, đặt kiểu dữ liệu và kiểm tra giá trị.
- Hiểu luồng HTTP request/response: method, status code, body và JSON.
- Từ chối status ngoài nhóm 2xx, JSON không hợp lệ và dữ liệu sai định dạng.
- Giữ Bot Core độc lập với giao diện CLI, network và adapter.
- Viết self-check offline có thể chạy lặp lại.

## Cấu trúc thư mục

```text
week-13-modules-cli-api/
├── README.md
├── notes.md
├── hints.md
├── cli.py
├── bot_course/
│   ├── __init__.py
│   ├── core.py
│   ├── adapter.py
│   └── http_foundation.py
├── exercises/
│   ├── README.md
│   ├── ex01_modules.py
│   ├── ex02_cli.py
│   └── ex03_http.py
├── examples/
│   └── offline_http.py
├── checks/
│   ├── README.md
│   └── check_week.py
└── mini-project/
    └── README.md
```

## Tổng quan kiến thức

### 1. Module và package

Mỗi file `.py` là một module. Package nhóm các module liên quan lại với nhau;
`__init__.py` giúp nhận diện package theo cách tổ chức của bài học. Import nên
chỉ rõ hàm đến từ đâu, ví dụ `from bot_course.core import choose_action`.

Main guard bảo đảm phần demo chỉ chạy khi file được gọi trực tiếp, không chạy
tự động khi module được import.

### 2. Dependencies và môi trường

Môi trường ảo giúp tách dependency theo từng dự án. Dùng `py -m pip` hoặc
`python -m pip` để chắc pip thuộc đúng Python interpreter. `pyproject.toml`
khai báo cấu hình và công cụ của project; nó không có nghĩa mọi thư mục đều
phải được đóng gói để phát hành.

### 3. CLI với argparse

`argparse` chuyển tham số dòng lệnh thành các thuộc tính có tên. Khai báo
`type=int` để chuyển giá trị thành số nguyên; khai báo `required=True` cho
option bắt buộc. Đầu vào hợp cú pháp vẫn cần được kiểm tra theo quy tắc nghiệp vụ.

### 4. HTTP và JSON

Request gửi method và URL; response trả status code cùng body. JSON text cần
được giải mã rồi mới sử dụng như dictionary/list Python. Status thành công không
bảo đảm body là JSON hợp lệ, do đó phải kiểm tra cả hai.

Các ví dụ trong exercise sử dụng fixture và URL trung lập `example.invalid`;
không gửi yêu cầu thực đến dịch vụ bên ngoài. Production API, endpoint, schema
và authentication của VuaCóc vẫn chưa được xác minh trong bài học này.

### 5. Ranh giới trách nhiệm

```text
CLI → Adapter → Bot Core
HTTP foundation: minh họa request/response riêng biệt
```

Bot Core quyết định action từ dữ liệu đầu vào và không tự đọc `sys.argv` hoặc
gọi mạng. Adapter chuyển đổi dữ liệu ở ranh giới giữa các thành phần.

## Cách chạy trên Windows (PowerShell)

Chạy các lệnh sau từ thư mục gốc repository `python-journey`.

### Bước 1 — Chạy chương trình CLI chính

```powershell
py weeks/week-13-modules-cli-api/cli.py --position 1 --goal 4
py weeks/week-13-modules-cli-api/cli.py --position 4 --goal 4
py weeks/week-13-modules-cli-api/cli.py --position 7 --goal 4
```

### Bước 2 — Hoàn thành và chạy từng exercise

```powershell
cd weeks/week-13-modules-cli-api
py -m exercises.ex01_modules
py -m exercises.ex02_cli --turn 3
py -m exercises.ex03_http
cd ../..
```

Lệnh `ex02_cli` phải nhận `--turn`; thử `--turn 0` để xem thông báo lỗi
đầu vào. Chạy exercises bằng `-m` từ thư mục tuần giúp Python tìm được package
`bot_course` ở thư mục bên cạnh.

### Bước 3 — Chạy self-check offline

```powershell
py weeks/week-13-modules-cli-api/checks/check_week.py
```

Kết quả mong đợi:

```text
Week 13 solution checks: PASS
```

Self-check bao phủ core action, GET request, tham số CLI, status không thành công
và JSON sai định dạng. Không cần cài thêm thư viện để chạy self-check này.

## Nếu dùng môi trường ảo

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
```

Tuần 13 dùng thư viện chuẩn ở các phần thực hành chính, nên không cần cài gói
HTTP bên ngoài chỉ để chạy exercises.

## Bản đồ tài liệu

- [Notes](notes.md): giải thích kỹ các khái niệm và import path.
- [Exercises](exercises/README.md): cách chạy ba bài tập.
- [Hints](hints.md): gợi ý khi tự làm.
- [Examples](examples/offline_http.py): minh họa HTTP offline.
- [Checks](checks/README.md): lệnh self-check.
- [Mini-project](mini-project/README.md): bài tổng hợp về CLI, adapter và core.

## Checklist hoàn thành

- [ ] Giải thích được module, package, import và main guard.
- [ ] Chạy được ba exercises mà không còn TODO.
- [ ] Biết dùng `argparse` và từ chối số lượt không hợp lệ.
- [ ] Biết phân biệt lỗi HTTP status và lỗi parse JSON.
- [ ] Self-check chạy ra `PASS`.
- [ ] Có thể giải thích vì sao core không nên phụ thuộc CLI/network.

**Nguyên tắc:** Learn → Build → Test → Debug → Explain.
