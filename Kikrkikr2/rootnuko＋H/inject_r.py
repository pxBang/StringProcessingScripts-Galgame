import os

# 定义文件夹路径
ks_folder = 'cn-ks'
txt_folder = 'cn-txt-r'

# 遍历ks文件夹中的所有.ks文件
for filename in os.listdir(ks_folder):
    if filename.endswith('.ks'):
        ks_file_path = os.path.join(ks_folder, filename)
        txt_file_path = os.path.join(txt_folder, filename.replace('.ks', '.txt'))

        if not os.path.exists(txt_file_path):
            print(f"对应的txt文件 {txt_file_path} 不存在，跳过。")
            continue

        with open(ks_file_path, 'r', encoding='utf-8') as ks_file, open(txt_file_path, 'r', encoding='utf-8') as txt_file:
            ks_lines = ks_file.readlines()
            txt_lines = txt_file.readlines()

        txt_line_index = 0
        new_ks_lines = []

        for line in ks_lines:
            if line.strip().endswith('[r]') and txt_line_index < len(txt_lines):
                new_line = txt_lines[txt_line_index].strip() + '[r]\n'
                new_ks_lines.append(new_line)
                txt_line_index += 1
            else:
                new_ks_lines.append(line)

        with open(ks_file_path, 'w', encoding='utf-8') as ks_file:
            ks_file.writelines(new_ks_lines)

print("处理完成！")
