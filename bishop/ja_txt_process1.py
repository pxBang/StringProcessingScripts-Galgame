# 读取ja.txt文件
with open("ja.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# 记录含有'\b'的行数
positions = []
new_lines = []

for i, line in enumerate(lines):
    if "\\b" in line:
        positions.append(str(i))  # 保存行号，从0开始计数
    new_lines.append(line.replace("\\b", ""))  # 删除'\b'

# 保存修改后的内容回同一文件
with open("ja.txt", "w", encoding="utf-8") as file:
    file.writelines(new_lines)

# 保存行号信息
with open("positions1.txt", "w", encoding="utf-8") as file:
    file.write(','.join(positions))

print("已处理文件并保存行号信息。")
