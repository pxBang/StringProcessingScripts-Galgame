import re

# 正则表达式，匹配以◆B...◆开头的行
pattern = re.compile(r'^(◆B[^◆]+◆)')

# 读取修改后的内容
with open('cn.txt', 'r', encoding='utf-8') as modified_file:
    modified_lines = modified_file.readlines()

# 初始化计数器
index = 0

# 打开原始文件和目标文件进行处理
with open('bsxx.dat.txt', 'r', encoding='utf-8') as infile, open('bsxx_cn.dat.txt', 'w', encoding='utf-8') as outfile:
    for line in infile:
        # 查找并保留标记行
        match = pattern.match(line)
        if match:
            # 检查是否有足够的修改行
            if index < len(modified_lines):
                # 写入标记加上修改后的文本
                outfile.write(match.group(1) + modified_lines[index])
                index += 1
            else:
                # 如果没有足够的修改行，输出原行
                outfile.write(line)
        else:
            outfile.write(line)

print("文件处理完成，并已保存到 bsxx_cn.dat.txt。")
