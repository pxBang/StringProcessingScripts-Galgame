import os
import re

def read_choice_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def replace_text_in_ks(content, replacements):
    def replacement_function(match):
        nonlocal replacements
        return f'text="{replacements.pop(0)}"'

    new_content = re.sub(r'text="(.*?)"', replacement_function, content, count=len(replacements))
    return new_content

def process_files(choice_folder, ks_folder):
    for choice_file in os.listdir(choice_folder):
        if choice_file.endswith('.choice.txt'):
            base_name = os.path.splitext(choice_file)[0].replace('.choice', '')
            ks_file = base_name + '.ks'
            choice_file_path = os.path.join(choice_folder, choice_file)
            ks_file_path = os.path.join(ks_folder, ks_file)

            if os.path.exists(ks_file_path):
                replacements = read_choice_file(choice_file_path)
                
                with open(ks_file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                new_content = replace_text_in_ks(content, replacements)
                
                with open(ks_file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                
                print(f"Updated {ks_file_path}")
            else:
                print(f"KS file {ks_file_path} not found for {choice_file_path}")

# 使用示例
choice_folder = 'cn-txt-choice'
ks_folder = 'cn-ks'
process_files(choice_folder, ks_folder)
