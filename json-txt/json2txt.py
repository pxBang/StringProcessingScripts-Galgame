import os
import json

def json_to_txt(json_folder, txt_folder):
    # 确保输出的txt文件夹存在
    os.makedirs(txt_folder, exist_ok=True)
    
    # 获取json文件夹中的所有.json文件
    json_files = [f for f in os.listdir(json_folder) if f.endswith('.json')]
    
    for json_file in json_files:
        json_file_path = os.path.join(json_folder, json_file)
        
        # 读取json文件内容
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # 确定输出的txt文件路径
        txt_file_path = os.path.join(txt_folder, json_file.replace('.json', '.txt'))
        
        # 将JSON数据转换为txt格式并写入到.txt文件
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            for item in data:
                txt_file.write(item["message"] + '\n')

if __name__ == "__main__":
    folder_pairs = [
        ('cn-json', 'cn-txt'),
        ('cn-json-choice', 'cn-txt-choice'),
        ('cn-json-p', 'cn-txt-p'),
        ('cn-json-r', 'cn-txt-r')
    ]
    
    for json_folder, txt_folder in folder_pairs:
        json_to_txt(json_folder, txt_folder)
