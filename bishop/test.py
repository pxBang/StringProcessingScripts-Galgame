def find_lines_with_word(file_path, word):
    lines_with_word = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, 1):
            if word in line:
                lines_with_word.append(line_number)
    return lines_with_word

def save_detailed_results(filename, word, lines_in_ja, lines_in_cn):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Results for the word: '{word}'\n")
        file.write("Unique to ja.txt, appears on lines:\n")
        unique_ja = set(lines_in_ja) - set(lines_in_cn)
        file.write(', '.join(map(str, unique_ja)) + '\n')

        file.write("Unique to cn.txt, appears on lines:\n")
        unique_cn = set(lines_in_cn) - set(lines_in_ja)
        file.write(', '.join(map(str, unique_cn)) + '\n')

        file.write("Common in both files, appears on lines:\n")
        common_lines = set(lines_in_ja) & set(lines_in_cn)
        file.write(', '.join(map(str, common_lines)) + '\n')

# 修改这些路径以指向您的文件位置
path_to_ja_txt = 'ja.txt'
path_to_cn_txt = 'cn.txt'
word_to_search = '舞冬'
results_filename = 'detailed_results.txt'  # 输出文件名

# 找到并打印行数
lines_in_ja = find_lines_with_word(path_to_ja_txt, word_to_search)
lines_in_cn = find_lines_with_word(path_to_cn_txt, word_to_search)

# 保存详细结果到文件
save_detailed_results(results_filename, word_to_search, lines_in_ja, lines_in_cn)

print(f"Detailed results have been saved to {results_filename}")
