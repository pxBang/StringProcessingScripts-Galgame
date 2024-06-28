import os
import re

def extract_text_from_ks(file_path):
    # 以shift-jis编码读取.ks文件
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 使用正则表达式提取text="任意字符"中的任意字符
    matches = re.findall(r'text="(.*?)"', content)
    return matches

def save_to_choice_txt(matches, output_file_path):
    # 以utf-8编码保存到.choice.txt文件
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for match in matches:
            file.write(match + '\n')

def process_files(input_folder, output_folder):
    # 如果输出文件夹不存在，则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.ks'):
            input_file_path = os.path.join(input_folder, file_name)
            output_file_name = os.path.splitext(file_name)[0] + '.choice.txt'
            output_file_path = os.path.join(output_folder, output_file_name)
            matches = extract_text_from_ks(input_file_path)
            save_to_choice_txt(matches, output_file_path)
            print(f"Processed {file_name} and saved to {output_file_path}")

# 使用示例
input_folder = 'ja-ks'
output_folder = 'ja-txt-choice'
process_files(input_folder, output_folder)
