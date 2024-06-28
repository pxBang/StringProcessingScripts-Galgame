# 读取修改后的文件cn.txt
with open("cn.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# 读取保存的行号信息
with open("positions1.txt", "r", encoding="utf-8") as file:
    positions = set(map(int, file.read().split(',')))

# 将'\b'添加到每个指定行的行首
for i in positions:
    lines[i] = "\\b" + lines[i]

# 保存最终内容回同一文件
with open("cn.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

print("已成功将\\b字符添加到指定行首，并保存于cn.txt中。")
