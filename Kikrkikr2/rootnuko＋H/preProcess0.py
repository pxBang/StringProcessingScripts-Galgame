import os
import re

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 使用正则表达式匹配并替换
    # 正则表达式解释：匹配 [eruby str="任意字符(非贪婪)" 任意字符直到]
    processed_content = re.sub(r'\[eruby str="([^"]*)" [^\]]*\]', r'\1', content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(processed_content)

def process_txt_files(directories):
    for directory in directories:
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                process_file(os.path.join(directory, filename))

# 指定目录列表
directories = ['ja-txt', 'ja-txt-r']
process_txt_files(directories)
