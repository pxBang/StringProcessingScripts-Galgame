import os
import subprocess
import shutil
import glob

def process_bin_files(bin_directory, tool_path):
    # 自动确定 txt_directory，假设它与 bin_directory 同级
    txt_directory = os.path.join(os.path.dirname(bin_directory), 'data_txt')
    
    # 确保 txt_directory 存在，如果不存在，则创建它
    if not os.path.exists(txt_directory):
        os.makedirs(txt_directory)
        print(f"Created directory {txt_directory}")

    # Step 1: 处理所有 .bin 文件
    bin_files = glob.glob(os.path.join(bin_directory, '*.bin'))
    for bin_file in bin_files:
        # 构建命令行命令
        command = f'"{tool_path}" "{bin_file}"'
        try:
            # 调用外部程序处理 .bin 文件
            subprocess.run(command, check=True)
            print(f"Processed {bin_file} successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to process {bin_file}: {e}")

    # Step 2: 移动和重命名 .dump.txt 文件
    dump_txt_files = glob.glob(os.path.join(bin_directory, '*.dump.txt'))
    for dump_txt_file in dump_txt_files:
        base_name = os.path.splitext(os.path.basename(dump_txt_file))[0]
        new_name = base_name.replace('.dump', '') + '.txt'
        new_path = os.path.join(txt_directory, new_name)
        
        # 移动并重命名文件
        shutil.move(dump_txt_file, new_path)
        print(f"Moved and renamed {dump_txt_file} to {new_path}")

        # Step 3: 删除文件中的 "<r>"
        remove_symbols(new_path)

def remove_symbols(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 删除所有 "<r>" 符号
    updated_content = content.replace('<r>', '')

    # 重写文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    print(f"Removed '<r>' from {file_path}")

# 目录和工具路径
bin_directory = r'D:\temp\Escude\Escude游戏\アストロノーツ\なつドキッ\Escude_Txt-Bin\bin2txt\data_bin'
tool_path = r'D:\temp\Escude\Escude工具\SacanaWrapper\StringTool.exe'

# 调用函数
process_bin_files(bin_directory, tool_path)
