# AI 开始工作手册

## 项目背景

- 本仓库是基于 `binaryanalysis-ng` 做了少量修改的 BANG 版本。
- 上游参考代码位于 `binaryanalysis-ng-reference/`，通过 Git 子模块固定；上游地址和提交记录在 `.gitmodules` 与子模块指针中。
- 分析当前版本与参考版本的差异时，先按相对路径和文件大小筛选。同名同大小的文件按用户要求跳过，优先检查大小不同和新增、删除、改名的文件，再用 diff 理解实际内容。
- 文件大小相同不保证内容相同；如果结论要求完整性或用户要求精确审查，再检查哈希或内容。

## 扫描范围

- 用户明确本项目只需支持扫描单个文件。保持 `scan` 的文件输入约束，不为目录扫描添加或扩展功能，除非用户另行要求。
- 参考版和当前版都能找到 `scan_directory` 命令；它的存在不代表本项目需要支持目录扫描，也不应把它当成本次需求。

## Parser 生成

- Kaitai parser 的正式生成入口是 `src/Makefile`：从仓库根目录执行 `make -C src`，把 `src/bang/parsers/**/*.ksy` 编成相邻的 `.py`，并修正生成代码的相对导入。
- 默认分支使用 PATH 中的 `kaitai-struct-compiler`。设置 `CONTAINER` 才会走 Makefile 的 Kaitai 容器分支；没有明确要求时不要走该分支，也不要创建临时容器。
- 当前 parser grammars 要求 Kaitai compiler 至少 0.11；生成代码也要求 Kaitai Python runtime 至少 0.11。保持 `setup.cfg` 和 `src/requirements.txt` 的 runtime 版本一致。

## 测试机与同步

- 目标测试机：`192.168.2.201`，SSH 用户：`aglaea`；用户说明 SSH 无需密码。
- 所有代码修改先在本地 `/share/bang` 完成，再从本地执行 `./sync.sh` 同步到服务器。不要直接在测试机上修改代码。
- 当前 `sync.sh` 使用 `rsync`，将 `/share/bang` 同步到 `aglaea@192.168.2.201:/data/vseeker`，并排除 `sync.sh` 本身；默认无需传参数。
- 仅在用户要求的代码修改完成后执行同步；纯分析、文档说明或未要求部署的工作不触发同步。

## 已知改动背景

这些是对比参考版本时识别出的修改意图。处理相关代码前，应重新检查实现和调用方，不要只依据本摘要改代码。

- `src/bang/cli.py`、`src/bang/scan_job.py`：调整多进程任务队列、超时和异常处理，意图是减少并行扫描卡住或意外崩溃，并记录已取出的任务数。
- `src/bang/meta_directory.py`：停用了硬链接、符号链接的创建和记录；README 说明此举是为了避免 NTFS 上的循环和异常。相关解包器仍会调用这些接口，改动可能影响解包结果。
- `src/bang/parsers/executable/elf/UnpackParser.py`：用 `pwnlib.ELF` 替换 `pwn.ELF`，代码注释说明原用法可能导致多进程扫描卡住。
- `src/bang/parser_utils.py`：导入解析器前检查目录内是否有 `UnpackParser.py` 或 `.pyc`，导入失败时输出 `Missed`。
- `.gitignore`、`shell.nix`：忽略 `offline/`，并调整 Nix shell 的 Python 与系统包名。
- `README.md`：记录了部分运行方式调整和上面提到的修改意图；文档内容不一定完全反映代码当前行为。

## 修改时注意

- 先读被改文件及其调用点，保持改动最小；不要顺手重写无关差异。
- 修改多进程调度时，重点检查长任务能否完成、空队列如何退出、worker 是否被提前结束，以及异常是否会导致任务结果丢失。
- 修改链接处理时，检查解析器调用、元数据记录和最终解包产物；不能只看两个方法本身。
- 这次比较中观察到 CLI 的计时退出逻辑可能在长任务完成前结束扫描；`debug_level` 也需要在改动 CLI 时确认定义和来源。不要将这些风险视为已修复。
- 按用户要求报告实际检查范围。若采用文件大小跳过策略，说明同大小内容差异未被发现；不要据此声称完成了全量内容校验。
