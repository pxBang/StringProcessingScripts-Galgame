import os

def insert_text(ja_ks_folder, cn_txt_folder, cn_ks_folder):
    # 确保输出文件夹存在
    if not os.path.exists(cn_ks_folder):
        os.makedirs(cn_ks_folder)

    # 获取文件列表
    ja_ks_files = sorted([f for f in os.listdir(ja_ks_folder) if f.endswith('.ks')])
    cn_txt_files = sorted([f for f in os.listdir(cn_txt_folder) if f.endswith('.txt')])

    for ja_ks_file, cn_txt_file in zip(ja_ks_files, cn_txt_files):
        # 读取原始ks文件
        with open(os.path.join(ja_ks_folder, ja_ks_file), 'r', encoding='utf-8') as file:
            ja_ks_lines = file.readlines()

        # 读取修改后的文本文件
        with open(os.path.join(cn_txt_folder, cn_txt_file), 'r', encoding='utf-8') as file:
            cn_txt_lines = file.readlines()

        # 替换相应行
        cn_txt_index = 0
        for i in range(1, len(ja_ks_lines)):
            if '[np][msgname]' in ja_ks_lines[i] and cn_txt_index < len(cn_txt_lines):
                ja_ks_lines[i-1] = cn_txt_lines[cn_txt_index]
                cn_txt_index += 1

        # 输出到新的ks文件
        output_ks_file = os.path.join(cn_ks_folder, ja_ks_file)
        with open(output_ks_file, 'w', encoding='utf-8') as file:
            file.writelines(ja_ks_lines)

# 设置文件夹路径
ja_ks_folder = 'ja-ks'  # 日文ks文件的文件夹路径
cn_txt_folder = 'cn-txt'  # 中文txt文件的文件夹路径
cn_ks_folder = 'cn-ks'  # 输出的中文ks文件的文件夹路径

# 执行函数
insert_text(ja_ks_folder, cn_txt_folder, cn_ks_folder)

print("处理完成！")
