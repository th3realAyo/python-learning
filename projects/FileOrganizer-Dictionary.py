import os

main_src = 'C:/Users/AYO_AYO/Desktop/test_folder'

destinations = {
    ".pdf": "Documents",
    ".mp3": "Music",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".mp4": "Videos"
}

# Create destination folders
for folder in set(destinations.values()):
    os.makedirs(os.path.join(main_src, folder), exist_ok=True)

others_path = os.path.join(main_src, "Other_Files")
os.makedirs(others_path, exist_ok=True)

# Organize files
for item in os.listdir(main_src):
    item_path = os.path.join(main_src, item)
    print(item_path)
    if os.path.isdir(item_path):
        continue

    extension = os.path.splitext(item)[1].lower()

    if extension in destinations:
        dst_folder = destinations[extension]
        dst_path = os.path.join(main_src, dst_folder, item)
    else:
        dst_path = os.path.join(others_path, item)

    os.replace(item_path, dst_path)
