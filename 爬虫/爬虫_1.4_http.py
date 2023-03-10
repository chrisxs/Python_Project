import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse, urljoin

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from tqdm import tqdm

# 检查文件名是否为Windows和Linux的合法文件名
def is_valid_filename(filename):
    if not re.match(r'^[^<>:"/\\|?*\x00-\x1F]*$', filename):
        return False
    if len(filename) > 255:
        return False
    if filename in {'.', '..'}:
        return False
    return True

# 下载图片文件
def download_image(url, directory):
    response = requests.get(url, stream=True)
    filename = os.path.basename(urlparse(url).path)
    if not is_valid_filename(filename):
        filename = f"{time.time():.0f}{os.path.splitext(filename)[1]}"
    filepath = os.path.join(directory, filename)
    with open(filepath, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    return filename

# 获取网页标题
def get_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string

# 获取网页所有链接
def get_links(url, base_url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            full_url = urljoin(base_url, href)
            links.append(full_url)
    return links

# 获取网页所有图片链接
def get_image_links(url, base_url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_links = []
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            full_url = urljoin(base_url, src)
            image_links.append(full_url)
    return image_links

# 获取网站所有标题、所有链接、所有图片链接
def get_all(url):
    base_url = f"{url.scheme}://{url.netloc}"
    title = get_title(url.geturl())
    links = get_links(url.geturl(), base_url)
    image_links = get_image_links(url.geturl(), base_url)
    return title, links, image_links

# 将信息记录到Excel文件中
def record_to_excel(title, links, image_links):
    filename = f"{time.strftime('%Y%m%d_%H%M%S')}.xlsx"
    wb = Workbook()
    ws = wb.active
    ws.title = "Links"
    ws.append(["Title", "Link"])
    for link in links:
        ws.append([title, link])
    ws = wb.create_sheet(title="Images")
    ws.append(["Image"])
    for image_link in image_links:
        ws.append([image_link])
    wb.save(filename)
    return filename

# 显示进度条并
