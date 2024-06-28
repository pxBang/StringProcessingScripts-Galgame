import os

def replace_lines(ks_folder, txt_folder):
    for txt_filename in os.listdir(txt_folder):
        if txt_filename.endswith('.p.txt'):
            ks_filename = txt_filename.replace('.p.txt', '.ks')
            txt_path = os.path.join(txt_folder, txt_filename)
            ks_path = os.path.join(ks_folder, ks_filename)
            
            with open(txt_path, 'r', encoding='utf-8') as txt_file:
                replacement_lines = txt_file.readlines()
            
            with open(ks_path, 'r', encoding='utf-8') as ks_file:
                ks_lines = ks_file.readlines()
            
            replacement_index = 0
            for i, line in enumerate(ks_lines):
                if '[p]' in line:
                    for j in range(i-1, -1, -1):
                        if ks_lines[j].strip():
                            if replacement_index < len(replacement_lines):
                                ks_lines[j] = replacement_lines[replacement_index].strip() + '\n'
                                replacement_index += 1
                            break
            
            with open(ks_path, 'w', encoding='utf-8') as output_file:
                output_file.writelines(ks_lines)

# 设定输入文件夹路径
ks_folder = 'cn-ks'
txt_folder = 'cn-txt-p'

# 运行程序
replace_lines(ks_folder, txt_folder)
