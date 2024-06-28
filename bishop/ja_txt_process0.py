# 读取ja.txt文件
with open("ja.txt", "r", encoding="utf-8") as file:
    content = file.read()

# 删除'\n'
content = content.replace("\\n", "")

# 替换'\A'为'久藤'，替换'\B'为'宗二'
content = content.replace("\\A", "久藤").replace("\\B", "宗二")

# 处理完毕后，写回文件
with open("ja.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("文件处理完毕。")
