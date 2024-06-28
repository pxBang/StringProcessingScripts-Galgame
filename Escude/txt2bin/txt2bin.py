import os
import shutil
import subprocess

# 设置文件夹路径
base_folder = r'D:\temp\Escude\Escude游戏\アストロノーツ\なつドキッ\Escude_Txt-Bin\txt2bin'
folder_path = os.path.join(base_folder, 'data_bin&txt')
target_folder = os.path.join(base_folder, 'data_bin')
tool_path = r'D:\temp\Escude\Escude工具\SacanaWrapper\StringTool.exe'

# 确保目标文件夹存在
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 功能 1: 重命名 _translated.txt 为 .dump.txt
for filename in os.listdir(folder_path):
    if filename.endswith('_translated.txt'):
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, filename.replace('_translated.txt', '.dump.txt'))
        os.rename(old_path, new_path)
        print(f"Renamed '{filename}' to '{filename.replace('_translated.txt', '.dump.txt')}'")

# 功能 2: 修改 .dump.txt 文件，添加空行和删除最后一行，替换字符
for filename in os.listdir(folder_path):
    if filename.endswith('.dump.txt'):
        file_path = os.path.join(folder_path, filename)
        
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # 修改文件内容
        if lines:  # 确保文件不是空的
            lines = ["\n"] + lines[:-1]  # 添加空行在首行并删除最后一行
            lines = [line.replace("♪", "！") for line in lines]  # 替换字符
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)

# 功能 3: 使用 StringTool.exe 打开所有 .dump.txt 文件
for filename in os.listdir(folder_path):
    if filename.endswith('.dump.txt'):
        file_path = os.path.join(folder_path, filename)
        command = f'"{tool_path}" "{file_path}"'
        subprocess.run(command, shell=True)
        print(f"Opened file: {filename}")

# 功能 4: 移动 .bin.new 文件并重命名为 .bin
for filename in os.listdir(folder_path):
    if filename.endswith('.bin.new'):
        source_path = os.path.join(folder_path, filename)
        target_path = os.path.join(target_folder, filename)
        shutil.move(source_path, target_path)
        print(f"Moved '{filename}' to '{target_folder}'")

        new_target_path = os.path.join(target_folder, filename[:-4])  # 移除最后的 ".new"
        os.rename(target_path, new_target_path)
        print(f"Renamed '{filename}' to '{filename[:-4]}'")

print("All operations completed successfully.")
