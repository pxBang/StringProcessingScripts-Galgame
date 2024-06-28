import os

def process_ks_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.ks'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace('.ks', '.p.txt'))
            
            with open(input_path, 'r', encoding='utf-8') as infile:
                lines = infile.readlines()
                
            output_lines = []
            for i, line in enumerate(lines):
                if '[p]' in line:
                    for j in range(i-1, -1, -1):
                        if lines[j].strip():
                            non_empty_line = lines[j].strip()
                            output_lines.append(non_empty_line)
                            break
            
            with open(output_path, 'w', encoding='utf-8') as outfile:
                outfile.write("\n".join(output_lines))

# 设定输入和输出文件夹路径
input_folder = 'ja-ks'
output_folder = 'ja-txt-p'

# 运行程序
process_ks_files(input_folder, output_folder)
