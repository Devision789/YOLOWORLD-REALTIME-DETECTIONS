# YOLOWORLD-REALTIME-DETECTIONS
# YOLO-World Object Detection

## Giới Thiệu

YOLO-World là một mô hình phát hiện đối tượng thời gian thực không cần huấn luyện, được phát triển bởi Tencent's AI Lab. Sử dụng kiến trúc YOLO dựa trên CNN, YOLO-World cung cấp hiệu suất nhanh và chính xác cho nhiều ứng dụng thực tế.

## Đặc Điểm

- **Phát hiện không cần huấn luyện:** Sử dụng cặp ảnh-văn bản và khả năng nền tảng.
- **Hiệu suất cao:** Thích hợp cho thiết bị biên, xử lý video, và gán nhãn tự động.
- **Paradigm "prompt-then-detect":** Mã hóa trước các gợi ý người dùng vào từ vựng offline.

## Yêu Cầu Hệ Thống

- Python 3.8+
- Thư viện TensorFlow hoặc PyTorch
- Các thư viện bổ sung: OpenCV, NumPy, Matplotlib

## Hướng Dẫn Cài Đặt

1. **Cloning the Repository**
    ```sh
    git clone https://github.com/yourusername/yoloworld-object-detection.git
    cd yoloworld-object-detection
    ```

2. **Cài Đặt Các Gói Yêu Cầu**
    ```sh
    pip install -r requirements.txt
    ```

## Hướng Dẫn Sử Dụng

1. **Chuẩn Bị Dữ Liệu**
    - Đặt các ảnh vào thư mục `data/images`.

2. **Chạy Mô Hình**
    ```sh
    python main.py 
    ```

3. **Kết Quả**
    - Kết quả phát hiện sẽ được lưu trong thư mục `output`.

## Đóng Góp

1. Fork dự án.
2. Tạo nhánh tính năng mới (`git checkout -b feature/AmazingFeature`).
3. Commit thay đổi của bạn (`git commit -m 'Add some AmazingFeature'`).
4. Push nhánh (`git push origin feature/AmazingFeature`).
5. Tạo pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Liên Hệ

- **Nhóm Phát Triển:** computervision9999@gmail.com
- **Github:** [Devision789](https://github.com/Devision789)
