---
title: NumPy 知识点总结
date: 2026-11-18
category: notes
subject: python
summary: FIP W10 Question and broadcast
---



## FIP W10 Question

### 题目描述

m 名用户对 k 类影目的评分矩阵（每行一名用户，评分整数 1–5）。为用户 user_id（编号 1..m）找出余弦相似度最高的另一用户 best_id（best_id ≠ user_id）。

  
请实现函数 best_match()：先对每行归一化，再用向量化方式计算相似度；禁止双重 for 构造完整相似度矩阵（可用 normalized @ normalized.T）。

约定：保证存在唯一的 best_id。

  
函数接口定义：

def best_match(ratings, user_id):

参数 ratings 为 shape (m, k) 整数数组，user_id 为 1 基用户编号。返回元组 (best_id, similarity)，best_id 为 1 基编号，similarity 为浮点数。

测试程序样例：
```python
import numpy as np

best_match(ratings, user_id):
	#这里输入答案

m, k, user_id = map(int, input().split())

ratings = np.array([list(map(int, input().split())) for _ in range(m)])

best_id, sim = best_match(ratings, user_id)

print(f"{best_id} {sim:.3f}")
```

### 解析

```python

import numpy as np

def best_match(ratings, user_id):
	# 归一化（单位化）
    ratings = ratings.astype(float)

    norms = np.linalg.norm(ratings, axis=1, keepdims=True)

    normalized = ratings / norms  
    
    # 获取相似度矩阵
    sims = normalized @ normalized.T

    i = user_id - 1

    sims[i, i] = -np.inf

    best_idx = int(np.argmax(sims[i]))

    return best_idx + 1, float(sims[i, best_idx])
```

**注**：
- 首先要让`ratings`通过`astype`变成`dtype`为`float`的矩阵，方便归一化
 - 归一化需要计算每一行向量的范数，沿`axis=1`进行取模，并且要`keepdims=True`，否则后续进行`normalized = ratings / norms`会无法广播
- `sims=normalized @ normalized.T`
- 与`user_id`产生相似度，只需看`user_id-1` 那一行
- 并且需要让`user_id`与自己的相似度归为负无穷
- `np.argmax`取最大值的下标

**掌握如何归一化，如何算得这个相似度矩阵，如何返回最大值的下标**


## NumPy的广播机制


### 广播特性

NumPy 的广播是让不同 `shape` 的数组在运算时自动对齐的机制。它有几个关键特性：

- 从**右往左**逐个维度比较。
- 某一维度相等，可以广播。
- 某一维度一边是 `1`，可以广播。
- 某一边缺少这个维度，也可以广播。
- 广播不会真的复制数据，只是逻辑上按扩展后的形状参与运算。
- 两个数组都不能单独决定结果时才报错，比如一边是 `3`，另一边是 `4`。

**判断方法**

假设两个数组的 shape 分别是：

```
a.shape = (5, 1, 3)
b.shape = (   4, 3)
```

判断时从右往左补齐：

```
a: 5 1 3
b:   4 3
```

补齐后相当于：

```
a: 5 1 3
b: 1 4 3
```

逐列比较：

```
5 和 1：可以，结果 5
1 和 4：可以，结果 4
3 和 3：可以，结果 3
```

所以结果 shape 是：

```
(5, 4, 3)
```

**结果规则**

广播后的 shape 按每一维取“**较大值**”：

```
结果维度 = max(a 的维度, b 的维度)
```

但前提是每一维都满足：

```
相等，或者其中一边是 1，或者其中一边缺失
```

**例子**

例 1：

```
a = np.ones((2, 3))
b = np.ones((3,))

a + b
```

比较：

```
a: 2 3
b:   3
```

补齐：

```
a: 2 3
b: 1 3
```

结果：

```
(2, 3)
```

也就是每一行都加 `b`。

例 2：

```
a = np.ones((2, 3))
b = np.ones((2, 1))

a + b
```

比较：

```
a: 2 3
b: 2 1
```

结果：

```
(2, 3)
```

也就是每一列都分别加 `b` 中的值。

例 3：

```
a = np.ones((2, 3))
b = np.ones((2,))

a + b
```

比较：

```
a: 2 3
b:   2
```

补齐：

```
a: 2 3
b: 1 2
```

最后比较：

```
3 和 2 不相等，且都不是 1
```

所以不能广播，会报：

```
ValueError: operands could not be broadcast together
```

如果想按列广播，要改成：

```
b = b.reshape(2, 1)
```

**再看 `norms` 的例子**

`ratings.shape = (m, k)`，计算每行模长时：

```
norms = np.linalg.norm(ratings, axis=1, keepdims=True)
```

`norms.shape = (m, 1)`，所以：

```
ratings / norms
```

比较：

```
ratings: m k
norms:   m 1
```

结果：

```
(m, k)
```

表示每一行都除以自己的模长。

如果 `keepdims=False`：

```
norms.shape = (m,)
```

就变成：

```
ratings: m k
norms:     m
```

补齐：

```
ratings: m k
norms:   1 m
```

要求 `k == m`，否则不能广播；即使刚好相等，语义也通常不是你想要的。

**一句话总结**

- 能否广播：从右往左比较，每维必须相等或一边是 `1` 或缺失。
- 广播结果：每个维度取较大值。
- 最常见坑：`(m,)` 和 `(m, 1)` 不是同一个含义；前者是一维向量，后者是列向量。