from PIL import Image
import os

# ระบุโฟลเดอร์ที่มีไฟล์ต้นฉบับ
source_folder = "class0_sharpk"
destination_folder = "converted_images"

# สร้างโฟลเดอร์ปลายทางถ้ายังไม่มี
os.makedirs(destination_folder, exist_ok=True)

# วนลูปเพื่อแปลงไฟล์ทั้งหมดในโฟลเดอร์
for filename in os.listdir(source_folder):
    if filename.endswith(".png"):
        # ดึงเลขดั้งเดิมจากชื่อไฟล์ เช่น 0000 จาก 0000.png
        original_number = os.path.splitext(filename)[0]
        
        # เปิดไฟล์ภาพ
        img_path = os.path.join(source_folder, filename)
        img = Image.open(img_path)
        
        # แปลงไฟล์เป็น JPG และบันทึกด้วยชื่อใหม่
        new_filename = f"etc_{original_number}.jpg"
        new_path = os.path.join(destination_folder, new_filename)
        img.convert("RGB").save(new_path, "JPEG")
        
        print(f"แปลงไฟล์ {filename} -> {new_filename} เสร็จสิ้น")

print("แปลงไฟล์ทั้งหมดเสร็จสิ้น!")
