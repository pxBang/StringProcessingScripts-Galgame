import os

# 定义文件夹路径
input_folder = 'cn-ks'
output_folder = 'cn-ks-16le'

# 如果输出文件夹不存在，则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取所有.ks文件
ks_files = [f for f in os.listdir(input_folder) if f.endswith('.ks')]

# 处理每个.ks文件
for ks_file in ks_files:
    input_path = os.path.join(input_folder, ks_file)
    output_path = os.path.join(output_folder, ks_file)
    
    # 以utf-8编码读取文件
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 以utf-16le编码保存文件
    with open(output_path, 'w', encoding='utf-16le') as f:
        f.write(content)

print("文件已成功转换并保存到cn-ks-16le文件夹中")
