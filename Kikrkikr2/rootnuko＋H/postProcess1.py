import os

def read_position_files(position_folder):
    # 初始化存储位置和字符串的字典
    positions = {}

    # 遍历文件夹中的所有.position.txt文件
    for filename in os.listdir(position_folder):
        if filename.endswith(".position.txt"):
            file_prefix = os.path.splitext(filename)[0].split(".position")[0]
            file_path = os.path.join(position_folder, filename)
            
            # 初始化存储该文件的行号和字符串的字典
            position_dict = {}
            
            # 打开并读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                
                # 遍历文件的每一行
                for line in lines:
                    # 提取行号和字符串
                    line_number, string = line.strip().split(': ', 1)
                    line_number = int(line_number.split()[1])
                    
                    if line_number not in position_dict:
                        position_dict[line_number] = []
                    position_dict[line_number].append(string)
            
            # 将该文件的字典存储到总字典中
            positions[file_prefix] = position_dict

    return positions

def modify_cn_files(cn_folder, positions):
    # 遍历文件夹中的所有.txt文件
    for filename in os.listdir(cn_folder):
        if filename.endswith(".txt"):
            file_prefix = os.path.splitext(filename)[0]
            file_path = os.path.join(cn_folder, filename)
            
            # 检查是否有对应的.position.txt文件
            if file_prefix in positions:
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                
                # 修改对应行的内容
                modified_lines = []
                for line_number, line in enumerate(lines, start=1):
                    if line_number in positions[file_prefix]:
                        for string in positions[file_prefix][line_number]:
                            if line.strip().endswith("」"):
                                line = line.strip()[:-1] + string + "」\n"
                            else:
                                line = line.strip() + string + '\n'
                    modified_lines.append(line)
                
                # 将修改后的内容写回文件
                with open(file_path, 'w', encoding='utf-8') as file:
                    for line in modified_lines:
                        file.write(line)

def main():
    # 定义文件夹路径
    position_folders = ['position', 'position-r']
    cn_folders = ['cn-txt', 'cn-txt-r']
    
    for position_folder, cn_folder in zip(position_folders, cn_folders):
        positions = read_position_files(position_folder)
        modify_cn_files(cn_folder, positions)

if __name__ == "__main__":
    main()
