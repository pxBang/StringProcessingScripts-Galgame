import os
import re

def find_and_remove_strings(folder_path, output_folder):
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 遍历文件夹中的所有.txt文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            file_prefix = os.path.splitext(filename)[0]
            output_file = os.path.join(output_folder, f"{file_prefix}.position.txt")
            
            # 初始化存储结果的列表
            results = []
            modified_lines = []

            # 打开并读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                
                # 遍历文件的每一行
                for line_number, line in enumerate(lines, start=1):
                    while True:
                        # 使用正则表达式查找以[开始，以]结尾的字符串，考虑嵌套情况
                        match = re.search(r'\[.*?\]', line)
                        if match:
                            matched_string = match.group()
                            # 忽略匹配到的[r]
                            if matched_string == '[r]':
                                line = line.replace(matched_string, '', 1)
                            else:
                                results.append(f"Line {line_number}: {matched_string}")
                                # 删除找到的字符串
                                line = line.replace(matched_string, '', 1)
                        else:
                            break
                    modified_lines.append(line)
            
            # 将结果写入到本地文件中
            with open(output_file, 'w', encoding='utf-8') as file:
                for result in results:
                    file.write(result + "\n")
            
            # 将修改后的内容写回源文件
            with open(file_path, 'w', encoding='utf-8') as file:
                for line in modified_lines:
                    file.write(line)

def main():
    # 定义两个文件夹路径和对应的输出文件夹
    folders = {
        'ja-txt': 'position',
        'ja-txt-r': 'position-r'
    }
    
    # 遍历文件夹字典并处理每个文件夹
    for folder_path, output_folder in folders.items():
        find_and_remove_strings(folder_path, output_folder)

if __name__ == "__main__":
    main()
