import os

# ระบุโฟลเดอร์ที่มีไฟล์ภาพ
image_folder = "converted_images"
# ระบุโฟลเดอร์สำหรับเก็บไฟล์ .txt
txt_folder = "labels_train_etc"

# สร้างโฟลเดอร์ปลายทางสำหรับไฟล์ .txt ถ้ายังไม่มี
os.makedirs(txt_folder, exist_ok=True)

# วนลูปเพื่อสร้างไฟล์ .txt ว่างเปล่าสำหรับทุกภาพในโฟลเดอร์
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg"):
        # ดึงชื่อไฟล์โดยไม่เอานามสกุล เช่น etc_0000 จาก etc_0000.jpg
        file_name_without_ext = os.path.splitext(filename)[0]
        
        # สร้างไฟล์ .txt ว่างเปล่าในโฟลเดอร์ labels
        txt_file_path = os.path.join(txt_folder, f"{file_name_without_ext}.txt")
        
        # สร้างไฟล์ .txt ว่างเปล่า
        open(txt_file_path, 'w').close()
        
        print(f"สร้างไฟล์ {file_name_without_ext}.txt ในโฟลเดอร์ labels เรียบร้อยแล้ว")

print("สร้างไฟล์ .txt ทั้งหมดเสร็จสิ้น!")
