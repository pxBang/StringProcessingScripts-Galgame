# 使用须知

请仔细阅读`txt2bin.py`的**路径说明**和**功能说明**

>请确保`SacanaWrapper`的`EscudeEditor.dll`插件为`GBK`编码，否则会乱码！！！
>请确保`SacanaWrapper`的`EscudeEditor.dll`插件为`GBK`编码，否则会乱码！！！
>请确保`SacanaWrapper`的`EscudeEditor.dll`插件为`GBK`编码，否则会乱码！！！

## 路径说明

1. `base_folder`目录
   - 当前工作目录
   - 目录路径可修改
2. `data_bin&txt` 文件夹
    - 包含原始`bin`文件
    - 包含翻译后的`txt`文件
    - 文件夹名可修改
3. `target_folder`文件夹
   - 包含输出后的`bin`文件
   - 文件夹名不可修改
4. `tool_path`文件路径
    - `StringTool.exe`文件路径
    - 文件路径可修改

## 功能说明

1. 功能 1
   - 重命名`_translated.txt` 为 `.dump.txt`
   - `_translated.txt`后缀可修改
2. 功能 2
   - 修改 .dump.txt 文件 添加空行和删除最后一行
   - 因为`GBK`编码里没有`♪`，因此替换字符`♪`为`！`
3. 功能 3
   - 使用 `StringTool.exe` 打开所有 `.dump.txt` 文件
4. 功能 4
   - 移动 `.bin.new` 文件并重命名为 `.bin`

## 总结

>需严格遵守以上规则，方可正确使用该`py`文件

该工具可有效提高`txt`转`bin`的效率，防止误操作，实现自动化
