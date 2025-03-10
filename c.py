import json
import os

# ชื่อไฟล์และโฟลเดอร์
input_file = 'labels2.json'
output_dir = 'new_labels'

# ตรวจสอบว่ามีโฟลเดอร์ new_labels หรือยัง ถ้ายังไม่มีให้สร้างใหม่
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# อ่านข้อมูลจาก labels2.json
with open(input_file, 'r') as file:
    data = json.load(file)

# ดึงขนาดของภาพจากข้อมูล images
image_info = {img['id']: img for img in data['images']}

# ดึง class id จาก categories
category_mapping = {cat['id']: idx for idx, cat in enumerate(data['categories'])}

# แปลงข้อมูล annotations เป็น YOLO format
for annotation in data['annotations']:
    image_id = annotation['image_id']
    category_id = annotation['category_id']
    bbox = annotation['bbox']

    # ดึงขนาดภาพ
    img_width = image_info[image_id]['width']
    img_height = image_info[image_id]['height']

    # แปลงข้อมูล bbox เป็น YOLO format (normalized)
    x_min, y_min, width, height = bbox
    x_center = (x_min + width / 2) / img_width
    y_center = (y_min + height / 2) / img_height
    norm_width = width / img_width
    norm_height = height / img_height

    # สร้างบรรทัดข้อมูลใน YOLO format
    yolo_line = f"{category_mapping[category_id]} {x_center:.6f} {y_center:.6f} {norm_width:.6f} {norm_height:.6f}"

    # ชื่อไฟล์ .txt สำหรับเก็บ YOLO label
    file_name = image_info[image_id]['file_name'].replace('.jpg', '.txt')
    output_file = os.path.join(output_dir, file_name)

    # บันทึกข้อมูลลงไฟล์
    with open(output_file, 'a') as out_file:
        out_file.write(yolo_line + '\n')

print(f"แปลงข้อมูลสำเร็จ! YOLO labels ถูกบันทึกในโฟลเดอร์ '{output_dir}'")
