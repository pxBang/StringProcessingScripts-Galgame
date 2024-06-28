import os

# 定义文件夹路径
input_folder = 'ja-ks'
output_folder = 'ja-txt-r'

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 遍历输入文件夹中的所有.ks文件
for filename in os.listdir(input_folder):
    if filename.endswith('.ks'):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename.replace('.ks', '.txt'))

        with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
            for line in infile:
                if line.strip().endswith('[r]'):
                    # 删除行尾的[r]并写入输出文件
                    outfile.write(line.strip()[:-3] + '\n')

print("处理完成！")
