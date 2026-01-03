import os
import shutil


os.chdir('C:/Users/AYO_AYO/Documents/Desktop/')

doc_ext = ('.pptx', '.docx', '.pdf', '.psd', '.xlsx')
media_ext = ('.aac', '.ogg', '.mp3')

main = ["Images", "Documents", "Audio", "Others"]

docs = [f for f in os.listdir() if f.endswith(doc_ext)]
audio = [f for f in os.listdir() if f.endswith(media_ext)]
img = [f for f in os.listdir() if f.endswith('.png') or f.endswith('.jpg')]

for file in main:
    os.makedirs(file, exist_ok=True)

for i in docs:
    shutil.move(i, main[1]) 

for i in audio:
    shutil.move(i, main[2])

for i in img:
    shutil.move(i, main[0])
print("Success") 