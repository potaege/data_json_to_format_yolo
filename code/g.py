import json
import os

# กำหนด mapping ใหม่สำหรับ category_id ตามที่ระบุ
category_mapping = {
    0: 2,  # Ascaris lumbricoides → 2
    4: 1,  # Hookworm egg → 1
    7: 0   # Opisthorchis viverrine → 0
}

# อ่านข้อมูลจากไฟล์ labels.json
with open('filtered_0_4_7.json', 'r') as file:
    data = json.load(file)

# สร้างไฟล์ classes.txt
classes = ["Opisthorchis viverrine", "Hookworm egg", "Ascaris lumbricoides"]
with open('classes.txt', 'w') as f:
    for cls in classes:
        f.write(cls + "\n")

# สร้างไดเรกทอรีสำหรับเก็บไฟล์ .txt ในโฟลเดอร์ new_labels
os.makedirs('new_labels', exist_ok=True)

# สร้างไฟล์ .txt สำหรับแต่ละภาพในโฟลเดอร์ new_labels
for image in data['images']:
    image_id = image['id']
    image_width = image['width']
    image_height = image['height']
    label_file = f"new_labels/{image['file_name'].replace('.jpg', '.txt')}"
    
    # ค้นหา annotation ที่ตรงกับภาพนี้
    annotations = [anno for anno in data.get('annotations', []) if anno['image_id'] == image_id]
    
    with open(label_file, 'w') as f:
        for anno in annotations:
            category_id = anno['category_id']
            # ตรวจสอบว่ามี mapping หรือไม่
            if category_id in category_mapping:
                new_category_id = category_mapping[category_id]
                
                # ดึงข้อมูล bbox
                x, y, w, h = anno['bbox']
                
                # คำนวณ normalized coordinates
                x_center = (x + w / 2) / image_width
                y_center = (y + h / 2) / image_height
                norm_width = w / image_width
                norm_height = h / image_height
                
                # เขียนข้อมูลลงไฟล์
                f.write(f"{new_category_id} {x_center:.6f} {y_center:.6f} {norm_width:.6f} {norm_height:.6f}\n")

print("แปลงข้อมูลเป็น YOLO format สำเร็จ! ไฟล์ถูกบันทึกในโฟลเดอร์ new_labels")
