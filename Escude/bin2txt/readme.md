# 使用说明

请仔细阅读**路径说明**和**功能说明**

>一定确保`SacanaWrapper`的`EscudeEditor.dll`插件为`SJS`编码格式。否则一定会乱码！！！
>一定确保`SacanaWrapper`的`EscudeEditor.dll`插件为`SJS`编码格式。否则一定会乱码！！！
>一定确保`SacanaWrapper`的`EscudeEditor.dll`插件为`SJS`编码格式。否则一定会乱码！！！

## 路径说明

1. `bin_directory`目录路径
   - 包含`.bin`文件的目录
   - 可修改
2. `tool_path`文件路径
   - `StringTool.exe`文件路径
   - 可修改

## 功能说明

1. 处理所有 `.bin` 文件
   - 调用外部程序处理 `.bin` 文件
2. 移动和重命名 `.dump.txt` 文件
   - 移动并重命名文件
3. 删除文件中的 `<r>`
   - 此举是为了让AI翻译正确的文本，而不是带有`<r>`的文本，提高翻译质量，减少翻译错误
