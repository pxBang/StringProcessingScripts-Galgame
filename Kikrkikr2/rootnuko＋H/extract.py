import os

def process_files(input_directory, output_directory):
    # 获取所有.ks结尾的文件
    files = [f for f in os.listdir(input_directory) if f.endswith('.ks')]

    for file_name in files:
        # 读取文件内容，以shift-jis编码
        with open(os.path.join(input_directory, file_name), 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 找到[np][msgname]所在行的前一行，并存储结果
        output_lines = []
        for i in range(1, len(lines)):
            if '[np][msgname]' in lines[i]:
                output_lines.append(lines[i-1])

        # 输出文件名以.txt结尾，并以utf-8格式保存
        output_file_name = os.path.splitext(file_name)[0] + '.txt'
        with open(os.path.join(output_directory, output_file_name), 'w', encoding='utf-8') as output_file:
            output_file.writelines(output_lines)

# 使用示例
input_directory = 'ja-ks'
output_directory = 'ja-txt'
os.makedirs(output_directory, exist_ok=True)  # 确保输出目录存在
process_files(input_directory, output_directory)
