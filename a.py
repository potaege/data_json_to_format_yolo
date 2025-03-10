import json

# อ่านข้อมูลจากไฟล์ data.json
with open('labels.json', 'r') as file:
    data = json.load(file)

# กรอง annotations ที่มี category_id = 7
filtered_annotations = [anno for anno in data['annotations'] if anno['category_id'] == 7]

# กรอง images ที่มี image_id ตรงกับ annotations ที่คัดเลือก
filtered_image_ids = {anno['image_id'] for anno in filtered_annotations}
filtered_images = [img for img in data['images'] if img['id'] in filtered_image_ids]

# สร้างข้อมูลใหม่ที่มีแค่ category_id = 7
filtered_data = {
    "info": data['info'],
    "licenses": data['licenses'],
    "categories": [cat for cat in data['categories'] if cat['id'] == 7],
    "images": filtered_images,
    "annotations": filtered_annotations
}

# บันทึกข้อมูลที่กรองแล้วลงไฟล์ใหม่
output_file = 'filtered_Opisthorchis_viverrine.json'
with open(output_file, 'w') as outfile:
    json.dump(filtered_data, outfile, indent=4)

print(f"กรองข้อมูลสำเร็จ! ข้อมูลที่กรองถูกบันทึกในไฟล์ {output_file}")
