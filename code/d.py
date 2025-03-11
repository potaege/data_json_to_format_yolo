import os

# โฟลเดอร์ต้นทางและปลายทาง
source_dir = 'new_labels'
target_dir = 'new_labels2'

# ตรวจสอบว่ามีโฟลเดอร์ new_labels2 หรือยัง ถ้ายังไม่มีให้สร้างใหม่
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# อ่านไฟล์ทั้งหมดในโฟลเดอร์ new_labels
for file_name in os.listdir(source_dir):
    if file_name.endswith('.txt'):
        source_file = os.path.join(source_dir, file_name)
        target_file = os.path.join(target_dir, file_name)

        # อ่านข้อมูลจากไฟล์ต้นทาง
        with open(source_file, 'r') as file:
            lines = file.readlines()

        # แก้ไขข้อมูลจาก 0 เป็น 1 ในบรรทัดแรกสุด
        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if parts[0] == '0':
                parts[0] = '1'
            new_lines.append(' '.join(parts))

        # บันทึกข้อมูลที่แก้ไขแล้วลงไฟล์ใหม่ในโฟลเดอร์ new_labels2
        with open(target_file, 'w') as file:
            file.write('\n'.join(new_lines))

print(f"แก้ไขข้อมูลสำเร็จ! ไฟล์ใหม่ถูกบันทึกในโฟลเดอร์ '{target_dir}'")
