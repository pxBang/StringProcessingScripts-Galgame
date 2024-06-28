# 读取修改后的文件cn.txt
with open("cn.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# 读取保存的行号信息
with open("positions2.txt", "r", encoding="utf-8") as file:
    positions = set(map(int, file.read().split(',')))

# 将''添加到每个指定行的符号」前面
for i in positions:
    if i < len(lines):  # 确保行号没有超出当前文件行数
        lines[i] = lines[i].replace("」", f"」")  # 替换第一个出现的」

# 保存最终内容回同一文件
with open("cn.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

print("已成功将字符添加到指定行的符号」前面，并保存于cn.txt中。")
