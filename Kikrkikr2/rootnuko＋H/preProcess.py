import os

# 指定输入文件夹和输出文件夹路径
input_folder_path = 'ja-ks-shiftjis'
output_folder_path = 'ja-ks'

# 确保输出文件夹存在
os.makedirs(output_folder_path, exist_ok=True)

# 遍历输入文件夹中的文件
for filename in os.listdir(input_folder_path):
    if filename.endswith('.ks'):
        input_file_path = os.path.join(input_folder_path, filename)
        output_file_path = os.path.join(output_folder_path, filename)
        
        # 读取 Shift_JIS 编码的文件
        with open(input_file_path, 'r', encoding='shift-jis') as file:
            content = file.read()
        
        # 以 UTF-8 编码保存文件
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(content)

print("转换完成！")
