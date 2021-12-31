#!/home/ben/miniconda3/envs/photo-wallpaper/bin/python

# Download Bing Wallpaper
# To "install", run:
# sudo echo "@daily  5       wallpaper.daily /home/ben/Pictures/photo-wallpaper/download.py" >> /etc/anacrontab

import numpy as np
import requests
import subprocess
import cv2

locale = 'en'
metadata = requests.get(f'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt={locale}').json()
metadata = metadata['images'][0]
caption = metadata['copyright'].replace('©', '(c)')

link = 'https://www.bing.com' + metadata['url']
print('Downloading', link)

resp = requests.get(link)
raw_img = np.frombuffer(resp.content, dtype=np.uint8)
img = cv2.imdecode(raw_img, -1)

overlay = img.copy()
offset = np.array((100, 100))

h, w, c = img.shape
img_sz = np.array((w, h))

s, y = cv2.getTextSize(caption, cv2.FONT_HERSHEY_DUPLEX, 0.5, 1)
txt_sz = np.array(s)

text_pos = tuple(img_sz - offset - txt_sz)
cv2.putText(img, caption, text_pos, cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

alpha = 0.4
cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)

img_path = f'/home/ben/Pictures/photo-wallpaper/img.jpg'
cv2.imwrite(img_path, img)

# subprocess.run(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', 'file:///' + img_path], check=True, capture_output=True)
