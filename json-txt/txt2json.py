import os
import json

def txt_to_json(txt_folder, json_folder):
    # 确保输出的json文件夹存在
    os.makedirs(json_folder, exist_ok=True)
    
    # 获取txt文件夹中的所有.txt文件
    txt_files = [f for f in os.listdir(txt_folder) if f.endswith('.txt')]
    
    for txt_file in txt_files:
        txt_file_path = os.path.join(txt_folder, txt_file)
        
        # 读取txt文件内容
        with open(txt_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # 构建JSON数据
        json_data = [{"name": "", "message": line.strip()} for line in lines]
        
        # 确定输出的json文件路径
        json_file_path = os.path.join(json_folder, txt_file.replace('.txt', '.json'))
        
        # 将JSON数据写入到.json文件
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    folder_pairs = [
        ('ja-txt', 'ja-json'),
        ('ja-txt-choice', 'ja-json-choice'),
        ('ja-txt-p', 'ja-json-p'),
        ('ja-txt-r', 'ja-json-r')
    ]

    for txt_folder, json_folder in folder_pairs:
        txt_to_json(txt_folder, json_folder)
