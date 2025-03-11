import json
import os
import shutil

# ชื่อโฟลเดอร์ที่ใช้เก็บไฟล์ภาพ
source_dir = 'data'
target_dir = 'data2'

# ตรวจสอบว่ามีโฟลเดอร์ data2 หรือยัง ถ้ายังไม่มีให้สร้างใหม่
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# อ่านข้อมูลจาก labels2.json
with open('filtered_0_4_7.json', 'r') as file:
    labels2 = json.load(file)

# ดึงชื่อไฟล์ภาพที่ต้องการจาก labels2
target_files = {image['file_name'] for image in labels2['images']}

# คัดลอกภาพที่ตรงกับ target_files ไปยัง data2
copied_count = 0
for file_name in os.listdir(source_dir):
    if file_name in target_files:
        source_path = os.path.join(source_dir, file_name)
        target_path = os.path.join(target_dir, file_name)
        shutil.copy2(source_path, target_path)
        copied_count += 1

print(f"คัดลอกภาพสำเร็จทั้งหมด {copied_count} ภาพไปยังโฟลเดอร์ '{target_dir}'!")
