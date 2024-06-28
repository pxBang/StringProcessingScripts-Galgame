import os
import subprocess

# 要执行的脚本列表
scripts = ['postProcess1.py', 'inject.py', 'inject_r.py', 'inject_p.py', 'inject_choice.py','postProcess.py']

# 当前文件夹路径
current_folder = os.getcwd()

# 依次执行每个脚本
for script in scripts:
    script_path = os.path.join(current_folder, script)
    if os.path.isfile(script_path):
        print(f'正在执行: {script}')
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f'错误: {result.stderr}')
    else:
        print(f'未找到脚本: {script_path}')
