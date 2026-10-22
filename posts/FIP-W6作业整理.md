---
title: FIP-W6作业整理
date: 2026-10-22
category: notes
subject: python
summary: 作业整理
---




# 6-3 6C02-杨辉哨塔

## 题目描述
哨塔坐标 (n,k) 的兵力等于杨辉三角第 n 行第 k 列（从 0 计）：两端为 1，中间 C(n,k)=C(n−1,k−1)+C(n−1,k)。递归、记忆化。

### 请实现函数 pascal()。

函数接口定义：
def pascal(n, k):
参数满足 0≤k≤n≤20。返回该格的数。

## Answer

```python 
def pascal(n,k,memory={(0,0):1}):
    if k==0 or n==k:
        memory[(n,k)]=1
    if (n,k) not in memory:
        memory[(n,k)]=pascal(n-1,k-1)+pascal(n-1,k)
    return memory[(n,k)]
```
### notes：
- basecase 条件：`k==0` 和`k==n` 时（因为要满足`pascal(n-1,k)`，也就是`n-1>=k`，所以`k==n`需要单独看）（并且其实就是杨辉三角的两边就是basecase）
- 递归时调用pascal函数不要用memory，memory只记录和返回值

---

# 6-4 6D01-密码全排列

## 题目描述
无重复字符的密码串，输出字典序全排列，每行一个。用递归生成。

### 请实现函数 list_permutations()，返回字典序排列列表。

函数接口定义：
def list_permutations(s):
参数 s 为无重复小写字母字符串（1≤∣s∣≤8）。返回全排列字符串列表，按字典序排列。
### example
- 输入样例：
cab
- 输出样例：
abc
acb
bac
bca
cab
cba

## Answer

```python
def list_permutations(s):
    if s == '':
        return ['']

    s = sorted(s)
    ans = []

    for i in range(len(s)):
        rest = s[:i] + s[i+1:]
        for j in list_permutations(''.join(rest)):
            ans.append(s[i] + j)

    return tuple(ans)
```

### notes 

1. **base case**：当 `s` 为空时无法继续递归调用，此时返回`['']`。
2. **字典序排序**：`s` 按字典序排序只需要 `sorted(s)`。`sorted` 函数可作用于所有 `iterable` 可迭代对象，形式为 `sorted(iterable, key=, reverse=False)`，返回**列表**。
3. **递归参数类型**：取出一个字符 `s[i]` 后，剩余字符形成的列表 `rest` 需要通过 `''.join(rest)` 变成字符串类型，否则无法作为参数被调用。
4. **递归返回值处理**：`list_permutations` 返回的是列表，拼接在取出的 `s[i]` 后时需要遍历，直接相加会报错。

---

# 6-5 6D02-货箱层深

## 题目描述
嵌套 list 表示货箱（元素为整数或子 list）。求最大嵌套深度：非 list 深度为 0；空 list 深度为 1；[1, [2, [3]]] 深度为 3。必须递归。

### 请实现函数 max_depth()。

函数接口定义：
def max_depth(xs):
参数 xs 为嵌套 list（仅 int 与 list）。返回整数深度。

### example
- 输入样例：
[1, [2, 3], [[4], 5]]
- 输出样例：
3

## Answer

```python
def max_depth(xs):
    if type(xs)==int:
        return 0

    if len(xs)==0:
        return 1

    return max(max_depth(i) for i in xs) + 1
```


### note

1. base case ：xs若是`int`，返回0；如果 `xs` 是**空列表**，需要返回 1，否则进行遍历时会报错。
2. 判断是否为list：可以用 `type()` 是否为`int` ；也可以用 `isinstance(xs,int)`
   注：`isinstance()`也可判断多个条件
   `isinstance(5, (int, float))  # True`满足其一即可
3. 取最大值直接用 `max` 函数，并且可以用 for 的糖表达来写：
   
```python
max(max_depth(i) for i in xs)
```
---

# 6B02-嵌套货箱

## 题目描述
废土货箱编号嵌套在 list 里。递归 flatten 成一层整数 list，

```python
import ast

def flatten(xs):
    result = []
    for item in xs:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

data = ast.literal_eval(input())
print(*flatten(data))
```
提示：① 对子 list 递归；② 追加单个整数。

### example
- 输入样例
[1, [2, 3], [[4], 5]]
- 输出样例
1 2 3 4 5

## note

### `extend`

`extend` 是列表方法，作用是把另一个可迭代对象里的元素**逐个拆开**追加到列表末尾，区别于 `append`：

```python
a = [1, 2]
a.append([3, 4])    # [1, 2, [3, 4]]  整个塞进去，嵌套保留
b = [1, 2]
b.extend([3, 4])    # [1, 2, 3, 4]    拆开铺平
```


- `item` 是子列表时，先递归拍平得到一个列表，再 `result.extend(...)` 把它的元素并入结果
- `item` 是单个整数时，用 `result.append(item)` 直接追加


### `ast.literal_eval`

`ast` 模块（Abstract Syntax Trees，抽象语法树）里的 `literal_eval` 可以把**字符串安全地解析成 Python 字面量**：

```python
import ast

data = ast.literal_eval("[1, [2, 3], 4]")
# 得到真正的列表 [1, [2, 3], 4]
```

因为 `input()` 读进来的是字符串，不能直接遍历出子列表，所以先用它把输入（字符串）还原成嵌套列表结构。它只接受字面量（数字、字符串、列表、元组、字典等），不会像 `eval` 那样执行任意代码，因此更安全。

最后 `print(*flatten(data))` 里的 `*` 是解包，把列表元素作为多个参数传给 `print`，输出就是空格分隔而不是 `[1, 2, 3]` 这种列表形式。

---

# 6B03-圈杀幸存者

## 题目描述
n 人围圈编号 1..n，每次数 2 出圈，求最后幸存者编号。递归（k=2 经典公式）填空：
```python
def josephus(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return (2 * josephus(n // 2) - 1)

    return (2 * josephus(n // 2) + 1)

n = int(input())
print(josephus(n))
```
## note

### 题目分析

本题是经典的约瑟夫问题（Josephus Problem），具体为 $k = 2$ 的情况：$n$ 个人围成一圈，编号 $1 \sim n$，从 1 开始报数，每次报数到 2 的人出圈（即数 1 的人留下，数 2 的人出圈），求最后幸存者的编号。

我们需要根据 $n$ 的奇偶性，利用递归公式来求解。

### 递推公式推导

我们先模拟一下报数过程，找出规律。

#### 1. 当 $n$ 为偶数时（$n = 2m$）

- **第一轮报数**：1 留下，2 出圈，3 留下，4 出圈…… $2m-1$ 留下，$2m$ 出圈。
- **剩余情况**：第一轮结束后，出圈的是所有偶数编号（2, 4, ..., $2m$），共 $m$ 个人。剩下的人编号为：1, 3, 5, ..., $2m-1$，共 $m$ 个人。
- **下一轮起始**：下一轮从 1 的下一个（即 3 的前一个出圈的是 $2m$，所以接下来从 1 继续报数）开始，1 报 1，3 报 2（出圈）。
- **映射关系**：此时，剩下的 $m$ 个人（1, 3, 5, ..., $2m-1$）构成了一个新的约瑟夫问题，人数为 $m = n/2$。在这个新圈中，编号为 $1, 3, 5, \dots$ 的人，可以看作是新编号 $1, 2, 3, \dots, m$。对应关系为：原编号 $2i - 1$ 对应新编号 $i$。
- **公式推导**：如果 $m$ 个人的幸存者在新编号中是 $j = \text{Josephus}(m)$，那么它在原编号中就是 $2j - 1$。

所以，当 $n$ 为偶数时：
$$ \text{Josephus}(n) = 2 \times \text{Josephus}(n/2) - 1 $$

#### 2. 当 $n$ 为奇数时（$n = 2m + 1$）

- **第一轮报数**：1 留下，2 出圈，3 留下，4 出圈…… $2m-1$ 留下，$2m$ 出圈，$2m+1$ 留下（报 1），接下来回到 1，1 报 2（出圈）。
- **剩余情况**：第一轮出圈的人：2, 4, ..., $2m$，以及最后的 1。剩下的人编号为：3, 5, 7, ..., $2m+1$，共 $m$ 个人。
- **下一轮起始**：此时，下一轮从 3 开始报数（3 报 1，5 报 2 出圈）。
- **映射关系**：剩下的 $m$ 个人（3, 5, ..., $2m+1$）对应新编号 $1, 2, \dots, m$。对应关系为：原编号 $2i + 1$ 对应新编号 $i$（即 $i = 1$ 对应 3，$i = 2$ 对应 5，...，$i = m$ 对应 $2m+1$）。
- **公式推导**：如果 $m$ 个人的幸存者在新编号中是 $j = \text{Josephus}(m)$，那么它在原编号中就是 $2j + 1$。

所以，当 $n$ 为奇数时：
$$ \text{Josephus}(n) = 2 \times \text{Josephus}(n // 2) + 1 $$

### 代码填空

根据上述分析：

- 当 `n % 2 == 0`（偶数）时，使用公式 ①：`2 * josephus(n // 2) - 1`。
- 当 `n % 2 != 0`（奇数）时，使用公式 ②：`2 * josephus(n // 2) + 1`。
