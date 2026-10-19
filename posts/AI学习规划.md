---
title: AI 学习规划
date: 2026-10-19
category: notes
summary: 浙江大学人工智能专业 · 大一到大二学习路线。
---

# AI 学习规划

> 浙江大学人工智能专业 · 大一到大二学习路线

## 培养方案简述

1. 大一上：Python，同时带一些数据结构与算法内容。 
2. 大一下：概率论与数理统计、机器学习。 
3. 大一下暑假： C++，计划自行了解学习 HPC 高性能计算。 
4. 大二上：系统学习数据结构与算法分析、深度学习、计算架构与存储。
5. 大二下：互联与分布式、大模型基础。
6. 大三：分方向学习，包括理论、模型、系统、工程
## 总体原则

- 不另起炉灶，跟随学校培养方案：**每门课之前补好前置基础，每门课之后做一个能动手的项目**。
- 保研最看重前两年绩点，大一大二绩点是读研的入场券。
- 课外投入控制在每周 8–12 小时，期末周全部让给复习。
- 以不影响课内成绩为前提

## 大一上学期

### 课内重点

- Python

 - 对 AI 来说，Python 是“工具语言”，重点是语法熟练、数据处理、调用库和写脚本，不必一开始就钻研冷门特性。
 - 推荐路径：
   - B 站入门视频：小甲鱼《零基础入门学习 Python》、《Python 从入门到精通教程》。
   - 系统教程：《Python-100-Days》、Python 官方文档、《Python Cookbook》。
   - 大一优先掌握：变量与类型、分支循环、函数、列表/字典、文件读写、异常处理、面向对象基础、NumPy/Pandas 入门。
 - 推荐视频：
   - 小甲鱼零基础入门学习 Python：<https://www.bilibili.com/video/av4050443>
   - Python 从入门到精通教程：<https://www.bilibili.com/video/av14184325>
   - Python 编程从入门到实践：<https://www.bilibili.com/video/av35698354>
 - 推荐教程：
   - Python 官方中文文档：<https://docs.python.org/zh-cn/3/>
   - Python-100-Days：<https://github.com/jackfrued/Python-100-Days>
   - Python Cookbook：<https://python3-cookbook.readthedocs.io/zh_CN/latest/index.html>
- 线性代数
 - 是 AI 最重要的数学基础：矩阵乘法、特征值、奇异值分解
 - 资料：[3Blue1Brown《线性代数的本质》](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

### 尽早开始的工具

- Linux

 - AI 专业不能只会 Windows。Linux 是跑实验、管理环境、使用 GPU、部署模型的基础。

 - #### 要学内容
  1. 基础命令：`cd`、`ls`、`mkdir`、`cp`、`mv`、`rm`、`cat`、`less`、`find`。
  2. 文件权限：`chmod`、`chown`、`sudo`。
  3. Shell：环境变量、`.bashrc`、别名、管道、重定向。
  4. 包与环境：`apt`、`conda`、`pip`、`venv`。
  5. 进程管理：`ps`、`top`、`htop`、`kill`、后台运行。
  6. 远程开发：SSH、SCP、tmux/screen。
  7. Git：clone、commit、branch、merge、rebase、远程协作。
  8. GPU/实验环境：CUDA、驱动、`nvidia-smi`、Docker 入门。

 - #### 推荐视频
  - Linux 零基础入门：<https://www.bilibili.com/video/BV1wyZnY2Ey6/>
  - Linux 操作系统基础到进阶：<https://www.bilibili.com/video/BV1duwReGEp9/>
  - Linux 零基础教程：<https://www.bilibili.com/video/BV1KL411W7KY/>
- Git
 - 所有课程代码放进 Git 仓库，用 Markdown 记笔记
 - 课程：[MIT Missing Semester](https://missing.csail.mit.edu/)（命令行、Shell、Vim、Git、调试工具）（每周看一两节）

### 刷题

- 用 Python 做基础题，熟悉列表、字典、递归、排序
  - 平台：[浙大 PTA](https://pintia.cn/)
  - 课程：陈越《数据结构》（中国大学 MOOC）

## 大一寒假

### C 语言入门（2-3weeks）

- 掌握基本语法、指针、数组、结构体、动态内存分配、多文件编译
- 动手写：链表、简单字符串处理、文件读写
- 目的：为 CSAPP 和 HPC 打基础，暑假学 C++ 时只需补面向对象、模板和 STL

### 轻度预习机器学习

- 建立直觉即可，不要急着上 PyTorch，对”模型、损失函数、梯度下降“有直观印象
- 视频：3Blue1Brown 神经网络系列
- 课程：吴恩达 Machine Learning Specialization 第一门
- 重点：模型、损失函数、梯度下降

## 建立硬件直观认识
- 看 [Nand2Tetris](https://www.nand2tetris.org/)；更深入的计算机组成/体系结构等学校课程再深入即可

## 大一下学期

### 课内

- 概率论与数理统计
- 机器学习

### 课外主线：从零实现课上算法

- 用 NumPy 手写：线性回归、逻辑回归、K 均值聚类、决策树
- 与 scikit-learn 结果对比
- 学期末整理成小型机器学习库（带测试和 README）放上 GitHub
- 真正理解梯度是怎么推导出来的，正则化为什么能防止过拟合，而不只是会调用 fit 和 predict

### 进阶

- Kaggle 入门比赛：e.g.泰坦尼克生存预测、房价预测
- 开始读 CSAPP 第一至三章
  - 信息表示、整数浮点数、机器级表示
  - 实验：Data Lab、Bomb Lab

## 大一下暑假

### HPC101

### C++ 学习

- 资料：[learncpp.com](https://www.learncpp.com/)、《C++ Primer》
- 动手实现：简化版动态数组、哈希表、线程池
- 练习：内存管理、移动语义、多线程

### HPC 入门项目：矩阵乘法优化（强烈推荐）

按以下步骤逐步优化并记录性能变化：

1. 三重循环朴素版本，测量 FLOPS
2. 调整循环顺序
3. 分块（block）优化缓存
4. AVX 指令向量化
5. OpenMP 多线程
6. 与 OpenBLAS 对比
- 对“为什么同样的计算，写法不同速度能差几十倍”有切身体会，而这正是 HPC 和系统方向最核心的直觉
### 并行计算入门

- 课程：[CMU 15-418](https://csd.cmu.edu/course-profiles/parallel-computer-architecture-and-programming-15-418) 前几讲

### CSAPP 续读

- 第五章（优化程序性能）+ 第六章（存储器层次结构）
- 实验：Cache Lab
- 与矩阵乘法优化项目同步进行，效果最好

## 大二上学期

### 课内

- 数据结构与算法分析
- 深度学习
- 计算架构与存储

### 数据结构与算法

- 用 C++ 实现课上的数据结构
- 刷 LeetCode，以中等题为主，每周保持一定量

### 深度学习

- 资料：
  - 李沐《动手学深度学习》
  - [Karpathy: Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)
- 动手项目：
  - **micrograd**：手写自动求导引擎，弄懂反向传播
  - 用 PyTorch 手写 CNN，在 MNIST / CIFAR-10 上完整训练（数据加载 → 训练循环 → 验证 → 保存模型）

### CUDA 入门（如有 GPU）

- 从向量加法、归约到矩阵乘法，写几个核函数
- 书：《Programming Massively Parallel Processors》

### CSAPP 续读

- 第七至九章：链接、异常控制流、虚拟内存
- 实验：Shell Lab、Malloc Lab

### ！！！重要：联系导师进组 ！！！

- 看学院老师主页，挑两三个感兴趣的方向，各读几篇代表论文
- 学期末或寒假前发邮件申请进组
- 保研夏令营在大三下，必须大二进组积累科研经历

## 大二下学期

### 课内

- 互联与分布式
- 大模型基础

### 课外主线：科研 + 大模型项目

- 分布式系统
  - 课程：[MIT 6.5840](https://pdos.csail.mit.edu/6.824/)（原 6.824）
  - 实验：用 Go 实现 MapReduce、Raft 共识算法
- 大模型项目
  - 跟随 [Karpathy nanoGPT](https://github.com/karpathy/nanoGPT)，在小数据集（如中文诗词）上从零训练小型 GPT
  - 自己实现 KV Cache 推理，对比开启/关闭的生成速度
  - 延伸方向：系统方向（若感兴趣） → 推理加速、显存优化；模型方向（若感兴趣） → LoRA 微调
- 大模型应用工程（若感兴趣）
  - 星球项目：PaiCLI-Python（ReAct 循环、工具调用、上下文压缩、多 Agent 协作）
  - 星球项目：派聪明 RAG

### CSAPP 收尾

- 第十至十二章：系统级 I/O、网络编程、并发
- 实验：Proxy Lab

## CSAPP 学习节奏总览

| 时间 | 章节 | 配套实验 |
|------|------|----------|
| 大一下 | 第 1–3 章：信息表示、整数浮点、机器级表示 | Data Lab、Bomb Lab |
| 大一下暑假 | 第 5–6 章：性能优化、存储器层次结构 | Cache Lab |
| 大二上 | 第 7–9 章：链接、异常控制流、虚拟内存 | Shell Lab、Malloc Lab |
| 大二下 | 第 10–12 章：系统 I/O、网络编程、并发 | Proxy Lab |

- 完成标准：每一章对应的实验能独立做完

## 工程能力小项目清单

1. 小型机器学习库（NumPy 从零实现）— 大一下
2. 矩阵乘法优化（HPC 入门）— 大一下暑假
3. 动态数组 / 哈希表 / 线程池（C++）— 大一下暑假
4. micrograd 自动求导引擎 — 大二上
5. PyTorch CNN 训练 — 大二上
6. CUDA 核函数练习 — 大二上
7. nanoGPT 小型 GPT 训练与 KV Cache 推理 — 大二下
8. MIT 6.5840 MapReduce / Raft 实验 — 大二下
9. 星球项目：派聪明 RAG、PaiCLI-Python

## 其他建议

- **竞赛**：喜欢算法可考 CCF CSP 认证（部分夏令营机试参考），但不要为拿奖挤占绩点和科研时间。
- **分方向**：理论 / 模型 / 系统 / 工程，现在不用决定。按路线走完两年，哪个方向做得最有兴趣、成绩最好，答案自然出来。
- **大一最重要**：不是学得多，而是把基础打牢、把习惯养好。
