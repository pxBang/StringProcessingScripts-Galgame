import re

# 正则表达式，匹配以◆B...◆开头的行
pattern = re.compile(r'^◆B[^◆]+◆(.*)')

# 打开原始文件和目标文件
with open('bsxx.dat.txt', 'r', encoding='utf-8') as infile, open('ja.txt', 'w', encoding='utf-8') as outfile:
    # 逐行读取文件
    for line in infile:
        # 使用正则表达式查找匹配
        match = pattern.match(line)
        if match:
            # 将匹配到的内容写入新文件
            outfile.write(match.group(1) + '\n')

print("文件处理完成，并已保存到 ja.txt。")
