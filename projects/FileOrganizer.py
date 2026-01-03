import os

# print(os.getcwd())
os.chdir('C:/Users/AYO_AYO/Desktop/test_folder')
# print(os.getcwd())

main_src = 'C:/Users/AYO_AYO/Desktop/test_folder/'
doc_dst = 'C:/Users/AYO_AYO/Desktop/test_folder/Documents'
music_dst = 'C:/Users/AYO_AYO/Desktop/test_folder/Music'
img_dst = 'C:/Users/AYO_AYO/Desktop/test_folder/Image'
vid_dst = 'C:/Users/AYO_AYO/Desktop/test_folder/Video'
others = 'C:/Users/AYO_AYO/Desktop/test_folder/Other_Files'

os.makedirs(doc_dst, exist_ok=True)
os.makedirs(music_dst, exist_ok=True)
os.makedirs(img_dst, exist_ok=True)
os.makedirs(vid_dst, exist_ok=True)
os.makedirs(others, exist_ok=True)

# print(os.listdir())
for filename in os.listdir(main_src):
    if os.path.splitext(filename)[1] == ".pdf":
        src_path = os.path.join(main_src, filename)
        dst_path = os.path.join(doc_dst, filename)
        os.replace(src_path, dst_path)
    elif os.path.splitext(filename)[1] == ".mp3":
        m_src_path = os.path.join(main_src, filename)
        m_dst_path = os.path.join(music_dst, filename)
        os.replace(m_src_path, m_dst_path)
    elif os.path.splitext(filename)[1] in [".jpg", ".jpeg", ".png"]:
        i_src_path = os.path.join(main_src, filename)
        i_dst_path = os.path.join(img_dst, filename)
        os.replace(i_src_path, i_dst_path)
    elif os.path.splitext(filename)[1] == ".mp4":
        v_src_path = os.path.join(main_src, filename)
        v_dst_path = os.path.join(img_dst, filename)
        os.replace(v_src_path, v_dst_path)
    else:
        o_src_path = os.path.join(main_src, filename)
        o_dst_path = os.path.join(others, filename)
        os.replace(o_src_path, o_dst_path)