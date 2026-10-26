# Exercises — Tuần 13

Hoàn thành theo thứ tự: module/import → CLI với `argparse` → HTTP/JSON offline.

## Cách chạy (Windows PowerShell)

Mở terminal tại thư mục gốc repository `python-journey` rồi chạy:

```powershell
cd weeks/week-13-modules-cli-api
py -m exercises.ex01_modules
py -m exercises.ex02_cli --turn 3
py -m exercises.ex03_http
cd ../..
```

Kết quả chính:
- `ex01_modules`: in action tương ứng với vị trí 1, 4 và 7 so với mục tiêu 4.
- `ex02_cli --turn 3`: in `turn=3`; nếu nhập số âm hoặc 0 thì CLI báo lỗi.
- `ex03_http`: xác minh GET request, parse JSON thành công và phát hiện status 500 / JSON hỏng.

## Bài 1 — Modules và main guard
Trong `ex01_modules.py`, import `choose_action` từ package `bot_course.core`, đặt phần demo trong `main()`, và dùng main guard để import file không tự chạy demo.

## Bài 2 — argparse
Trong `ex02_cli.py`, khai báo `--turn` là option bắt buộc kiểu `int`. Kiểm tra thêm quy tắc nghiệp vụ: turn phải lớn hơn hoặc bằng 1.

## Bài 3 — HTTP/JSON offline
Trong `ex03_http.py`, tạo request GET trung lập; dùng fixture cục bộ để kiểm thử status 200 và JSON; xác nhận status không phải 2xx hoặc body không phải JSON hợp lệ sẽ bị từ chối. Không cần kết nối Internet.

## Self-check tổng
Trở về thư mục gốc repository rồi chạy:

```powershell
py weeks/week-13-modules-cli-api/checks/check_week.py
```

Kết quả mong đợi: `Week 13 solution checks: PASS`.

**Lưu ý import:** nên chạy exercise qua `py -m exercises.<tên_module>` từ thư mục Tuần 13. Cách này đưa thư mục tuần vào import path để tìm được package `bot_course`.