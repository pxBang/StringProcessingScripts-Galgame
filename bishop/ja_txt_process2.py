# 读取ja.txt文件
with open("ja.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# 记录含有''的行数
positions = []
new_lines = []

for i, line in enumerate(lines):
    if "" in line:
        positions.append(str(i))  # 保存行号，从0开始计数
    new_lines.append(line.replace("", ""))  # 删除''

# 保存修改后的内容回同一文件
with open("ja.txt", "w", encoding="utf-8") as file:
    file.writelines(new_lines)

# 保存行号信息
with open("positions2.txt", "w", encoding="utf-8") as file:
    file.write(','.join(positions))

# 输出行号的数量
print(f"已处理文件并保存行号信息。总共保存了 {len(positions)} 行的位置信息。")
