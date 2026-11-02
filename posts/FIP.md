---
title: FIP W1-W8 复习讲义
date: 2026-11-02
category: notes
subject: python
summary: 期中笔记整理
---


## 使用说明

这份讲义按周组织，每周包含：核心思想、知识点讲解、常见例题、完整代码骨架、常用函数和方法、易错点。复习时建议先看每章开头的问题，再对照代码手推一两个小例子。

## W1 计算

核心问题：如何把一个实际问题拆成输入、处理、输出？

### 1. IPO

IPO 是 Input、Process、Output 的缩写。写题时先问三个问题：要读什么数据？要做什么计算？要输出什么格式？以温度转换为例：输入摄氏温度，处理公式 `F = C * 9 / 5 + 32`，输出华氏温度。以圆面积为例：输入半径，处理 `area = pi * r ** 2`，输出面积。

### 2. 输入与输出

`print` 用来输出，`input` 用来读入一行。`input` 的返回值永远是字符串，即使你输入的是数字，所以算术前必须转换。

```python
print("Hello World!")
print(1, 2, 3, sep="-")
print(1, end=" ")
print(2)

a = input()
print(type(a))  # <class 'str'>
n = int(input())
r = float(input())
```

一行读多个数用 `split` 和 `map`。

```python
hour, minute = map(int, input().split())
```

`split` 默认按空白切，`map(int, ...)` 会把每个片段转成整数，最后解包给左边变量。如果输入只有两段，左边的变量也必须正好两个。

### 3. 变量与赋值

变量是给值起的名字。赋值语句先把右边表达式算出来，再绑定到左边名字。同一名字可以先后指向不同类型的值，这叫动态类型。

```python
x = 6
x = "hello"
total = 0
total += x  # 等价 total = total + x
```

变量名必须以字母或下划线开头，后面可以用字母、数字、下划线。变量名区分大小写，不能用 Python 关键字，也不要覆盖内置函数名，例如 `max`、`sum`、`print`。

### 4. 运算符与表达式

常见算术运算符：`+`、`-`、`*`、`/`、`//`、`%`、`**`。

```python
print(10 / 3)   # 3.3333333333333335
print(10 // 3)  # 3
print(10 % 3)   # 1
print(2 ** 10)  # 1024
```

`/` 是浮点除法，`//` 是整数除法，`%` 是余数。温度转换这种需要小数结果的题必须用 `/`，不要误用 `//`。

关系运算符返回布尔值：`==`、`!=`、`>`、`<`、`>=`、`<=`。条件里判断相等要用 `==`，赋值用 `=`。

### 5. 单一 if

W1 只讲单分支 `if`。缩进决定哪些语句属于这个分支。

```python
n = int(input())
if n % 7 == 0:
    print("是 7 的倍数")
```

### 6. while True 与 break

`while True` 会一直循环，直到遇到 `break`。哨兵值通常不应计入结果，所以 `break` 要写在处理数据之前。

```python
total = 0
count = 0
while True:
    x = int(input())
    if x == -1:
        break
    total += x
    count += 1
if count > 0:
    print(total / count)
```

常用循环模式：累加、计数、找最值、分档统计。

```python
max_val = None
while True:
    x = int(input())
    if x == 0:
        break
    if max_val is None or x > max_val:
        max_val = x
print(max_val)
```

```python
positive = negative = 0
while True:
    x = int(input())
    if x == 0:
        break
    if x > 0:
        positive += 1
    if x < 0:
        negative += 1
print(positive, negative)
```

### 7. 格式化输出

`f-string` 用花括号嵌入变量或表达式。

```python
area = 2.56
print(f"面积是：{area:.2f}")
```

`.2f` 表示浮点数保留两位小数，`.1f` 表示一位小数。OJ 通常要求输出和题面完全一致，所以不要多加提示文字。

### 8. 文件与终端

Python 源文件要用 `.py` 扩展名。在终端进入源文件所在目录后运行。

```text
cd w1_lab
python hello.py
```

如果报 `FileNotFoundError`，先检查当前目录和文件位置是否一致。

### 9. W1 常见例题

矩形面积：

```python
length = int(input())
width = int(input())
print(length * width)
```

温度转换：

```python
celsius = float(input())
fahrenheit = celsius * 9 / 5 + 32
print(f"{fahrenheit:.1f}")
```

判断 7 的倍数：

```python
n = int(input())
if n % 7 == 0:
    print("yes")
```

取个位数：

```python
n = int(input())
print(n % 10)
```

## W2 枚举与减治

核心问题：候选解太多时，是逐个枚举，还是每一步缩小问题规模？

### 1. if-else 和布尔运算

`else` 表示条件不成立时的另一条路径。多个条件可以用 `and`、`or`、`not` 组合。

```python
x = int(input())
if x >= 0:
    print("non-negative")
else:
    print("negative")
```

`and` 要求两个条件都真，`or` 只要有一个真，`not` 取反。Python 的布尔运算会短路：如果左边已经能决定结果，右边不会继续求值。

### 2. for 与 range

`range` 表示整数等差序列，默认右端点不包含。

```python
print(list(range(5)))          # [0, 1, 2, 3, 4]
print(list(range(2, 5)))       # [2, 3, 4]
print(list(range(1, 10, 3)))   # [1, 4, 7]
print(list(range(5, 0, -1)))   # [5, 4, 3, 2, 1]
```

`for` 会依次取出每个元素。

```python
for k in range(2, 10):
    print(k)
```

### 3. 循环 else 和布尔标识

循环的 `else` 不是 `if` 的 `else`。只有循环没有被 `break` 打断时才会执行。

```python
x = int(input())
is_prime = True
for k in range(2, int(x ** 0.5) + 1):
    if x % k == 0:
        is_prime = False
        break
print(is_prime)
```

用循环 `else` 可以少写一个标识变量：

```python
for k in range(2, int(x ** 0.5) + 1):
    if x % k == 0:
        print("composite")
        break
else:
    print("prime")
```

### 4. 素数枚举

素数是大于 1 且只能被 1 和自身整除的整数。判断素数时不用枚举到 `x - 1`，只需枚举到 `sqrt(x)`。原因是如果 `x = a * b`，那么 `a` 和 `b` 中至少有一个不大于 `sqrt(x)`。

```python
def is_prime(x):
    if x < 2:
        return False
    for k in range(2, int(x ** 0.5) + 1):
        if x % k == 0:
            return False
    return True
```

输出区间内的素数：

```python
a, b = map(int, input().split())
for x in range(a, b + 1):
    if is_prime(x):
        print(x)
```

### 5. 最大公约数

枚举法从小到大记录能同时整除 `a` 和 `b` 的最大数：

```python
best = 1
for k in range(1, min(a, b) + 1):
    if a % k == 0 and b % k == 0:
        best = k
print(best)
```

但更高效的是辗转相除法，也就是欧几里得算法。它每一步把 `(a, b)` 缩小成 `(b, a % b)`，直到 `b` 为 0。

```python
a, b = map(int, input().split())
while b:
    a, b = b, a % b
print(a)
```

这里的 `a, b = b, a % b` 是同步赋值。右边先全部算完，再一次性赋给左边变量，因此不会先用新的 `a` 去算 `a % b`。

### 6. 条件 while

`while` 可以直接写循环条件，而不一定要用 `while True` 加 `break`。

```python
n = int(input())
while n > 0:
    print(n)
    n -= 1
```

条件必须在循环体里有机会变假，否则会死循环。

### 7. 多重循环枚举：凑硬币

问题：给定金额 `x`，用 1 分、2 分、5 分硬币凑出所有组合。

```python
x = int(input())
for one in range(x + 1):
    for two in range(x // 2 + 1):
        for five in range(x // 5 + 1):
            if one + 2 * two + 5 * five == x:
                print(one, two, five)
```

注意上界。2 分硬币最多 `x // 2` 个，5 分硬币最多 `x // 5` 个。`range` 右端点不包含，所以要 `+ 1`。

### 8. 分解质因数

外层 `for` 枚举候选因子，内层 `while` 反复除尽当前因子。

```python
x = int(input())
print(f"{x} = 1", end="")
n = x
for k in range(2, n + 1):
    while n % k == 0:
        print(f" × {k}", end="")
        n //= k
print()
```

这里不需要先判断 `k` 是否素数，因为合数因子会在更小的因子阶段被除尽。

### 9. 数字谜枚举

题目形如 `3?7 + ?5? = 892`，其中问号代表不同非零数字。可以枚举三个问号，验证等式。

```python
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if 307 + a * 10 + b * 100 + c * 10 + 5 == 892:
                print(a, b, c)
```

实际题目要把数位对准，这里重点是枚举思想。

### 10. 二分求根

若函数在区间 `[a, b]` 连续，且 `f(a)` 与 `f(b)` 异号，则区间内至少有一个根。二分法每次取中点，根据中点函数值与端点符号关系保留有根的一半。

```python
import math

a, b = 1.0, 2.0
eps = 1e-6
while True:
    fa = a ** 3 - 3 * math.sin(a)
    fb = b ** 3 - 3 * math.sin(b)
    if fa * fb > 0:
        print("no root")
        break
    m = (a + b) / 2
    fm = m ** 3 - 3 * math.sin(m)
    if abs(fm) < eps:
        print(m)
        break
    if fm * fa > 0:
        a = m
    else:
        b = m
```

浮点数不要用 `f(m) == 0` 判断，要用 `abs(f(m)) < eps`。

### 11. 牛顿法和弦截法

牛顿法用切线代替曲线，公式是 `x = x - f(x) / f'(x)`。求平方根等价于解 `x ** 2 - a = 0`。

```python
a = 3
eps = 1e-3
x = a / 2
while True:
    if abs(x ** 2 - a) < eps:
        break
    x = (x + a / x) / 2
print(x)
```

弦截法不需要导数，用最近两点连线近似切线。

```python
eps = 1e-3
xp, xc = 1.0, 2.0
while True:
    fp = xp ** 2 - 2
    fc = xc ** 2 - 2
    if abs(fc) < eps:
        print(xc)
        break
    xp, xc = xc, xc - fc * (xc - xp) / (fc - fp)
```

注意分母 `fc - fp` 可能接近 0，工程上应判断或换初值。

## W3 迭代与模拟

核心问题：精确解不可得或不必要时，如何得到足够好的结果？

### 1. if-elif-else

多个互斥分支用 `elif`。从上到下匹配，第一个成立的分支执行后，后面的不再检查。

```python
score = float(input())
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(grade)
```

条件顺序很重要。上例必须从大到小判断，否则 `score >= 60` 放在前面会把高分也判成 D。

### 2. 条件表达式

条件表达式的形式是 `值1 if 条件 else 值2`。它是一个表达式，不是控制语句。

```python
digit = int(a[-i]) if i <= len(a) else 0
```

只有选中的一侧会被求值，这在大数加法补 0 时很有用。

### 3. def 函数

`def` 把一段计算封装成可重复使用的函数。

```python
def add(a, b):
    return a + b

print(add(3, 4))
```

位置参数按顺序对应，关键字参数按名字对应。有默认值的参数要写在后面。

```python
def greet(name, title="同学"):
    return title + name

greet("李")
greet("李", title="老师")
```

`return` 会立刻结束函数并返回结果。没有 `return` 的函数返回 `None`。函数内部给名字赋值默认是局部变量。

### 4. 类型注解和 docstring

类型注解给人看，不强制运行时检查。

```python
def secant(f, x0: float, x1: float, eps: float) -> float:
    """用弦截法求 f(x)=0 的近似根。f 必须可调用。"""
    ...
```

### 5. 高阶函数和 lambda

参数或返回值中出现函数，就是高阶函数。`secant(f, ...)` 接收函数 `f`，所以是高阶函数。

```python
def apply_twice(f, x):
    return f(f(x))

print(apply_twice(lambda x: x * x, 3))  # 81
```

`lambda` 是匿名单表达式函数，适合短公式或 `key=`。

```python
root = secant(lambda x: x ** 2 - 2, 1.0, 2.0, 1e-3)
```

`lambda` 里不能写语句块。

### 6. eval

`eval` 可以把字符串当表达式求值，但不要用于用户输入或作业草稿。

```python
x = 1.5
print(eval("x ** 2 - 2"))
```

更安全的做法是把公式写成函数或 lambda。

### 7. random 模块

常用函数：

| 函数 | 含义 |
|---|---|
| `random.seed(a)` | 固定随机种子，便于复现 |
| `random.random()` | 返回 `[0, 1)` 的浮点数 |
| `random.uniform(a, b)` | 返回区间内的随机浮点数 |
| `random.randint(a, b)` | 返回 `[a, b]` 内随机整数，端点都含 |
| `random.randrange(start, stop, step)` | 类似 `range` 规则，右端点不含 |
| `random.choice(seq)` | 从非空序列随机选一个 |
| `random.shuffle(x)` | 原地打乱可变序列 |
| `random.sample(pop, k)` | 无放回抽取 k 个 |

蒙特卡洛估算圆周率：

```python
import random

random.seed(42)
n = 1000000
inside = 0
for _ in range(n):
    x = random.random()
    y = random.random()
    if x * x + y * y <= 1:
        inside += 1
print(4 * inside / n)
```

### 8. 字符串作为序列

字符串是不可变序列。可以索引、切片、遍历，但不能改单个字符。

```python
s = "hello"
print(s[0])
print(s[-1])
print(s[1:4])
for ch in s:
    print(ch)
```

常用方法和函数：

| 名称 | 含义 |
|---|---|
| `len(s)` | 字符个数 |
| `s.find(sub)` | 找不到返回 -1 |
| `s.index(sub)` | 找不到抛 ValueError |
| `s.count(sub)` | 子串出现次数 |
| `s.startswith(prefix)` | 是否以指定前缀开头 |
| `s.endswith(suffix)` | 是否以指定后缀结尾 |
| `s.upper()` | 全大写 |
| `s.lower()` | 全小写 |
| `s.capitalize()` | 首字母大写 |
| `s.title()` | 单词首字母大写 |
| `s.swapcase()` | 大小写互换 |
| `s.replace(old, new)` | 替换子串 |
| `s.split(sep=None)` | 按分隔符切分，默认空白 |
| `sep.join(iterable)` | 用分隔符拼接字符串元素 |
| `s.strip()` | 去两端空白 |
| `s.lstrip()` | 去左端空白 |
| `s.rstrip()` | 去右端空白 |
| `ord(ch)` | 字符转码点 |
| `chr(i)` | 码点转字符 |

```python
text = "1,2,3"
nums = text.split(",")
joined = "-".join(nums)
print(nums, joined)
print(ord("A"), chr(65))
```

字符串拼接是造新串。需要频繁修改时，通常先用列表，最后用 `join`。

### 9. 迭代与数值终止条件

数值迭代不追求完全等于精确根，而是用容差 `eps` 判断足够接近。常见终止条件有两种：`abs(f(x)) < eps` 或 `abs(x_new - x_old) < eps`。

```python
eps = 1e-6
max_iter = 100
for _ in range(max_iter):
    new_x = ...
    if abs(new_x - x) < eps:
        x = new_x
        break
    x = new_x
```

### 10. 大数加法

当数字太大超出普通类型范围时，可以用字符串逐位模拟竖式加法。Python 的 `int` 其实支持大整数，但这里训练的是逐位处理思想。

```python
def big_add(a, b):
    result = ""
    carry = 0
    i = 1
    while i <= max(len(a), len(b)) or carry:
        da = int(a[-i]) if i <= len(a) else 0
        db = int(b[-i]) if i <= len(b) else 0
        total = da + db + carry
        result = str(total % 10) + result
        carry = total // 10
        i += 1
    return result
```

简单模拟乘法可以先重复加法。

```python
a = "123"
b = 45
for _ in range(b - 1):
    a = big_add(a, a)
print(a)
```

## W4 序列与查找

核心问题：有序和查找有什么关系？不同结构分别适合哪些操作？

### 1. list 列表

列表是可变序列，元素有序、可重复，按下标访问。

```python
xs = []
xs.append(1)
xs.append(2)
xs[0] = 99
print(xs)
```

索引从 0 开始，负索引表示从末尾倒数。

```python
xs = [10, 20, 30, 40]
print(xs[0], xs[-1])
print(xs[1:3])
print(xs[:2])
print(xs[2:])
print(xs[::-1])
```

切片是左闭右开，得到新列表。

常用列表方法：

| 方法 | 含义 |
|---|---|
| `append(x)` | 末尾追加一个元素 |
| `extend(iterable)` | 逐个追加多个元素 |
| `insert(i, x)` | 在下标 i 处插入 |
| `remove(x)` | 删除第一个等于 x 的元素 |
| `pop()` | 弹出末尾元素 |
| `pop(i)` | 弹出并返回指定位置元素 |
| `clear()` | 清空列表 |
| `index(x)` | 查找元素首次下标 |
| `count(x)` | 统计元素个数 |
| `sort()` | 原地排序 |
| `reverse()` | 原地反转 |

注意 `append` 和 `extend` 的区别：`append([3,4])` 会把整个列表作为一个元素，`extend([3,4])` 会拆开加入。

```python
a = [1, 2]
a.append([3, 4])
print(a)  # [1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])
print(b)  # [1, 2, 3, 4]
```

别名和拷贝很重要。`b = a` 让两个名字指向同一个列表对象，`b = a[:]` 或 `b = a.copy()` 创建新列表。

### 2. tuple 元组

元组是不可变序列，适合表示一组绑定在一起的数据。

```python
t = (1, 2, 3)
one = (1,)
packed = 1, 2, 3
```

单元素元组必须有逗号。元组可以索引、切片、遍历，但没有 `append` 等修改方法。

```python
x, y = (10, 20)
```

### 3. 常用序列函数

| 函数 | 含义 |
|---|---|
| `len(xs)` | 元素个数 |
| `min(xs)` | 最小值 |
| `max(xs)` | 最大值 |
| `sum(xs)` | 求和 |
| `sorted(xs)` | 返回新排序列表 |
| `reversed(xs)` | 反向迭代器 |
| `enumerate(xs)` | 同时给出下标和元素 |
| `zip(a, b)` | 按位置配对多个序列 |
| `any(xs)` | 有一个真则为真 |
| `all(xs)` | 全部为真才为真 |

`min`、`max`、`sorted` 都可以接 `key=`。`key` 是一个单参数函数，用来决定比较依据。

```python
words = ["apple", "banana", "pear"]
print(max(words, key=len))
print(sorted(words, key=lambda s: -len(s)))
```

### 4. 参数打包与解包

定义函数时，`*args` 收集多余位置参数为元组，`**kwargs` 收集多余关键字参数为字典。

```python
def f(a, *args, **kwargs):
    print(a, args, kwargs)

f(1, 2, 3, eps=1e-3)
```

调用时 `*xs` 把列表拆开，`**d` 把字典按关键字拆开。

```python
xs = [1, 5, 3]
print(max(*xs))  # 等价 max(1, 5, 3)
```

### 5. 大 O 记号

大 O 描述增长趋势。

| 复杂度 | 含义 | 例子 |
|---|---|---|
| `O(1)` | 常数时间 | 列表按索引访问 |
| `O(log n)` | 对数时间 | 二分查找 |
| `O(n)` | 线性时间 | 线性查找、找最值 |
| `O(n log n)` | 线性对数 | 归并排序 |

### 6. 找最值

```python
def find_max(xs):
    if not xs:
        return None
    best = xs[0]
    for x in xs[1:]:
        if x > best:
            best = x
    return best
```

找最大值下标：

```python
def find_max_index(xs):
    if not xs:
        return -1
    best_idx = 0
    for i in range(1, len(xs)):
        if xs[i] > xs[best_idx]:
            best_idx = i
    return best_idx
```

### 7. 线性查找

线性查找不要求数据有序，时间复杂度 `O(n)`。

```python
def linear_search(xs, target):
    for i, x in enumerate(xs):
        if x == target:
            return i
    return -1
```

查找所有出现位置：

```python
def linear_search_all(xs, target):
    result = []
    for i, x in enumerate(xs):
        if x == target:
            result.append(i)
    return tuple(result)
```

### 8. 二分查找

二分查找要求数据有序，时间复杂度 `O(log n)`。每次把查找范围缩小一半。

```python
def binary_search(xs, target):
    left, right = 0, len(xs) - 1
    while left <= right:
        mid = (left + right) // 2
        if xs[mid] == target:
            return mid
        if xs[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

如果先排序，返回的下标对应的是排序后的列表，不再是原列表下标。

### 9. Markdown 与 MathJax 报告

报告里表格要用竖线写，代码要用三反引号围起来，公式用 `$...$` 或 `$$...$$`。

```markdown
| 策略 | 比较次数 |
|:---|---:|
| 线性 | 6 |
| 二分 | 2 |
```

复杂度可以写成 `$O(n)$` 或 `$O(\log n)$`。

## W5 哈希

核心问题：如何通过键直接定位数据？

### 1. 哈希思想

哈希表把键转换成索引，从而实现平均 `O(1)` 查找。简单哈希函数常取模，例如数字 ID 对表长取模。

```python
def hash_func(key, table_size):
    num = int(key.split("-")[1])
    return num % table_size
```

表长常选质数，可以减少冲突聚集。

### 2. 冲突处理

不同键可能映射到同一个槽位，这就是哈希冲突。

开链法：每个槽位是一个列表，冲突时追加到列表末尾。

```python
table_size = 13
hash_table = [[] for _ in range(table_size)]

def insert(key, value):
    idx = hash_func(key, table_size)
    hash_table[idx].append((key, value))

def lookup(key):
    idx = hash_func(key, table_size)
    for k, v in hash_table[idx]:
        if k == key:
            return v
    return None
```

线性探测：冲突时向后找空位。

```python
def insert_probe(hash_table, key, value, table_size):
    idx = hash_func(key, table_size)
    while hash_table[idx] is not None:
        idx = (idx + 1) % table_size
    hash_table[idx] = (key, value)
```

### 3. dict 字典

字典是键到值的映射，底层是哈希表。键必须不可变，例如整数、浮点数、字符串、布尔值或由不可变元素组成的元组。列表、字典、集合不能作键。

```python
sensor = {"S-042": 28.1}
sensor["S-117"] = 24.2
print(sensor.get("S-999", "未找到"))
print("S-042" in sensor)
del sensor["S-042"]
```

常用字典方法：

| 方法 | 含义 |
|---|---|
| `d[k]` | 取值或赋值；取值时键不存在会 KeyError |
| `d.get(k, default)` | 安全取值，不存在返回默认值 |
| `d.setdefault(k, default)` | 不存在时插入默认值 |
| `d.update(other)` | 批量更新，同键覆盖 |
| `d.pop(k)` | 删除并返回对应值 |
| `d.popitem()` | 删除一对，CPython 中通常是最后插入的一对 |
| `d.clear()` | 清空 |
| `d.copy()` | 浅拷贝 |
| `d.keys()` | 键视图 |
| `d.values()` | 值视图 |
| `d.items()` | 键值对视图 |

遍历字典时，默认遍历键。

```python
for k in d:
    print(k, d[k])

for k, v in d.items():
    print(k, v)
```

### 4. set 集合

集合只关心成员是否存在。元素唯一、无序、必须可哈希。空集合是 `set()`，不是 `{}`。

```python
s = set()
s.add(1)
s.add(2)
s.discard(1)
print(2 in s)
```

集合运算：

| 运算 | 符号 | 方法 |
|---|---|---|
| 并集 | `\|` | `union` |
| 交集 | `&` | `intersection` |
| 差集 | `-` | `difference` |
| 对称差 | `^` | `symmetric_difference` |
| 子集 | `<=` | `issubset` |
| 超集 | `>=` | `issuperset` |
| 无交集 | 无 | `isdisjoint` |

查重一行代码：

```python
has_duplicate = len(xs) != len(set(xs))
```

### 5. 词频统计

```python
count = {}
for word in text.split():
    count[word] = count.get(word, 0) + 1
print(count)
```

不要写 `count[word] += 1`，第一次遇到该词会 KeyError。

从文件读词频：

```python
count = {}
f = open("fox.txt")
for line in f:
    for word in line.split():
        count[word] = count.get(word, 0) + 1
f.close()
```

文件对象可以按行遍历。本周手动 `close`，后续会讲 `with`。

### 6. 寻找单身汉

绝大多数元素成对出现，只有一个元素落单。

```python
def find_single(xs):
    count = {}
    for x in xs:
        count[x] = count.get(x, 0) + 1
    for x, c in count.items():
        if c == 1:
            return x
    return None
```

两个单身汉：

```python
def find_two_singles(xs):
    count = {}
    for x in xs:
        count[x] = count.get(x, 0) + 1
    result = []
    for x, c in count.items():
        if c == 1:
            result.append(x)
    return result
```

### 7. 两数之和

用字典记录已经见过的补数。

```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if x in seen:
            return [seen[x], i]
        seen[target - x] = i
    return []
```

### 8. 作用域和 global

函数内赋值默认创建局部变量。要给全局名赋新值，必须写 `global`。

```python
count = 0

def bump():
    global count
    count += 1
```

更好的写法是参数进、返回值出。

### 9. 异常

缺键会抛 `KeyError`，文件不存在会抛 `FileNotFoundError`。

```python
try:
    f = open("fox.txt")
except FileNotFoundError:
    print("文件不存在")
else:
    for line in f:
        print(line, end="")
    f.close()
```

词频缺键应优先用 `get`，不要靠捕获异常当控制流。不要用裸 `except: pass` 吞掉错误。

## W6 递归

核心问题：如何用更小的同类问题描述当前问题？

### 1. 递归四基础

| 基础 | 含义 | 缺了会怎样 |
|---|---|---|
| Base Case | 最小规模直接返回 | 无限递归，RecursionError |
| Make Progress | 每次调用规模变小 | 无法到达终止条件 |
| Always Believe | 相信子问题已解决 | 写不动，容易陷入展开 |
| Compound Interest | 同一子问题不重复算 | 树状递归指数爆炸 |

递归模板：

```python
def solve(n):
    if base_condition(n):
        return direct_answer
    sub = solve(smaller(n))
    return combine(n, sub)
```

### 2. 汉诺塔

把 `n` 个盘从 `source` 移到 `target`，需要借助 `aux`。步骤是：先把上面 `n - 1` 个盘移到 `aux`，再把最大盘移到 `target`，最后把 `n - 1` 个盘从 `aux` 移到 `target`。

```python
def hanoi(n, source, target, aux):
    if n > 0:
        hanoi(n - 1, source, aux, target)
        print(f"move {n} from {source} to {target}")
        hanoi(n - 1, aux, target, source)
```

### 3. 阶乘

`n! = n * (n - 1)!`，Base Case 是 `0! = 1` 或 `1! = 1`。

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

`factorial(5)` 会先递进到 Base Case，再回归时逐步乘回来。

### 4. 线性递归与尾递归

每次只调用一次自己是线性递归。如果递归调用是最后一步，返回前不再做额外计算，就是尾递归。

```python
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)
```

尾递归可以改写成循环。

```python
def gcd_iter(x, y):
    while y != 0:
        x, y = y, x % y
    return x
```

Python 不保证自动消除尾递归，工程上常手动改成循环。

### 5. 树状递归与记忆化

斐波那契每次调用两个子问题，形成调用树。

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

朴素版会重复计算大量子问题。用字典记忆化可以把时间复杂度降为 `O(n)`。

```python
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        result = n
    else:
        result = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    memo[n] = result
    return result
```

也可以用 `functools.lru_cache`。

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

装饰后参数必须可哈希。多组测试之间可以用 `fib.cache_clear()`。

### 6. 整行杨辉三角

`pascal(n)` 返回第 n 行整个列表。上一行只计算一次，存进变量再拼本行。

```python
def pascal(n):
    if n == 0:
        return [1]
    prev = pascal(n - 1)
    row = [1]
    for i in range(len(prev) - 1):
        row.append(prev[i] + prev[i + 1])
    row.append(1)
    return row
```

迭代版：

```python
def pascal_iter(n):
    row = [1]
    for _ in range(n):
        new_row = [1]
        for j in range(len(row) - 1):
            new_row.append(row[j] + row[j + 1])
        new_row.append(1)
        row = new_row
    return row
```

### 7. 函数默认参数和注解

默认参数在定义时求值一次。不要把可变对象当默认值。

```python
def f(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items
```

注解：

```python
def fib(n: int) -> int:
    ...
```

## W7 分治算法

核心问题：问题切成两半后，只走一边还是两半都做完再合并？

### 1. 减治与分治

减治通常只产生一个子问题，子问题的解就是原问题的解，例如二分查找。分治会产生多个子问题，并且需要合并，例如归并排序。

### 2. 递归版二分查找

递归版二分查找是尾递归。

```python
def binary_search_rec(xs, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if xs[mid] == target:
        return mid
    if xs[mid] < target:
        return binary_search_rec(xs, target, mid + 1, right)
    return binary_search_rec(xs, target, left, mid - 1)

def binary_search(xs, target):
    return binary_search_rec(xs, target, 0, len(xs) - 1)
```

尾递归可以改循环。

```python
def binary_search_iter(xs, target):
    left, right = 0, len(xs) - 1
    while left <= right:
        mid = (left + right) // 2
        if xs[mid] == target:
            return mid
        if xs[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### 3. 归并排序

归并排序分三步：对半分，递归排两半，合并两个有序列表。

```python
def merge_sort(xs):
    if len(xs) <= 1:
        return xs
    mid = len(xs) // 2
    left = merge_sort(xs[:mid])
    right = merge_sort(xs[mid:])
    return merge(left, right)
```

合并两个有序列表：

```python
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

`<=` 保证相等时先取左半，有利于稳定性。漏掉最后的 `extend` 是高频错误。

`arr[:mid]` 是切片拷贝，不是窗口。工程上可以用下标版本减少拷贝。

```python
def merge_sort_inplace(arr, lo, hi):
    if hi - lo <= 1:
        return
    mid = (lo + hi) // 2
    merge_sort_inplace(arr, lo, mid)
    merge_sort_inplace(arr, mid, hi)
```

### 4. 跨中点最大子段和

最大连续子段和可能出现在左半、右半或穿过中点。前两种交给子问题，第三种在本层处理。

```python
def max_crossing(arr, lo, mid, hi):
    best_l = arr[mid - 1]
    s = best_l
    for i in range(mid - 2, lo - 1, -1):
        s += arr[i]
        best_l = max(best_l, s)
    best_r = arr[mid]
    s = best_r
    for j in range(mid + 1, hi):
        s += arr[j]
        best_r = max(best_r, s)
    return best_l + best_r

def max_subarray(arr, lo, hi):
    if hi - lo == 1:
        return arr[lo]
    mid = (lo + hi) // 2
    return max(
        max_subarray(arr, lo, mid),
        max_subarray(arr, mid, hi),
        max_crossing(arr, lo, mid, hi),
    )
```

### 5. 逆序对

逆序对指 `i < j` 且 `arr[i] > arr[j]`。归并排序在合并时左右两半已有序，取右半元素时，左半剩余元素都比它大，可以一次性计数。

```python
def merge_count(left, right):
    result = []
    i = j = inv = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inv += len(left) - i
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inv

def inversions(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, c1 = inversions(arr[:mid])
    right, c2 = inversions(arr[mid:])
    merged, c3 = merge_count(left, right)
    return merged, c1 + c2 + c3
```

`return merged, total` 实际返回元组，调用处可以拆成两个变量。

### 6. 快速排序

快速排序先选基准，把更小的放左、更大的放右，再递归两侧。

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
```

基准必须从参与分区的数组中排除，所以这里用 `arr[1:]`。首元素作基准时，已排序输入会退化，可以随机选基准或用三路分区。

```python
import random

def quick_sort_random(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort_random(less) + equal + quick_sort_random(greater)
```

### 7. 杨辉三角格子版

`pascal(n, k)` 返回第 n 行第 k 个数。两侧都是 1，中间是上一行两个肩膀之和。

```python
def pascal(n, k):
    if k == 0 or k == n:
        return 1
    return pascal(n - 1, k - 1) + pascal(n - 1, k)
```

用 `(n, k)` 作记忆化键。

```python
def pascal_memo(n, k, memo=None):
    if memo is None:
        memo = {}
    if (n, k) in memo:
        return memo[(n, k)]
    if k == 0 or k == n:
        return 1
    memo[(n, k)] = pascal_memo(n - 1, k - 1, memo) + pascal_memo(n - 1, k, memo)
    return memo[(n, k)]
```

## W8 简单线性数据结构

核心问题：数据按什么顺序进出？用什么结构才快？

### 1. 数组与链表

数组是连续存放，按下标访问快；链表结点分散存放，通过引用连接。

| 操作 | 数组 | 链表 |
|---|---|---|
| 按下标访问 | `O(1)` | `O(n)` |
| 头部插入 | `O(n)` | `O(1)` |
| 已知位置插入删除 | `O(n)` | `O(1)` |
| 内存 | 连续 | 分散 |

Python 常用 `list` 表现数组形态，两端都要快时用 `collections.deque`。

### 2. list 当栈

栈是 LIFO，后进先出。`list` 的尾部就是栈顶。

```python
stack = []
stack.append("A")  # push
stack.append("B")
top = stack.pop()  # pop
print(top)
```

### 3. list.pop(0) 的陷阱

`list.pop(0)` 逻辑上像出队，但性能是 `O(n)`，因为后面所有元素都要前移。队列应该用 `deque.popleft()`。

### 4. collections.deque

`deque` 是双端队列，两端插入删除都是 `O(1)`。

| 方法 | 含义 |
|---|---|
| `append(x)` | 右端入队 |
| `appendleft(x)` | 左端入队 |
| `pop()` | 右端弹出 |
| `popleft()` | 左端弹出 |
| `extend(iterable)` | 右端逐个加入 |
| `extendleft(iterable)` | 左端逐个加入，顺序会反转 |
| `clear()` | 清空 |
| `rotate(n)` | 循环旋转，正数右移，负数左移 |
| `maxlen=n` | 构造时指定长度，满了自动丢另一端 |

队列 FIFO 标准写法：

```python
from collections import deque

orders = deque()
orders.append("A")     # enqueue
orders.append("B")
first = orders.popleft()  # dequeue
print(first)
```

简单队列类：

```python
from collections import deque

class SimpleQueue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0
```

### 5. 栈的应用：括号匹配

每个右括号都要和最近的未匹配左括号配对，所以用 LIFO 栈。

```python
def is_valid(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack
```

三个关键点：右括号来时先判空栈，栈顶必须匹配，结束后栈必须为空。

### 6. Git 和 GitHub

Git 管本机版本历史，GitHub 托管远程仓库。

基本流程：

```text
工作区 --git add--> 暂存区 --git commit--> 本地仓库 --git push--> 远程仓库
```

常用命令：

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
git init
git status
git add README.md
git add .
git commit -m "W8 研讨课代码"
git log --oneline
git remote add origin <仓库地址>
git branch -M main
git push -u origin main
```

`.gitignore` 用来排除不该提交的文件。

```text
__pycache__/
*.pyc
.vscode/
.DS_Store
```

常见错误包括未 `add` 就 `commit`、重复添加 `origin`、`push` 认证失败、提交了缓存文件等。

## 复习速查

### 顺序结构

| 结构 | 顺序 | Python 实现 |
|---|---|---|
| 栈 | LIFO | `list` + `append` / `pop` |
| 队列 | FIFO | `deque` + `append` / `popleft` |

### 查找策略

| 策略 | 前提 | 复杂度 |
|---|---|---|
| 线性查找 | 无需有序 | `O(n)` |
| 二分查找 | 必须有序 | `O(log n)` |
| 哈希查找 | 键可哈希 | 平均 `O(1)` |

### 递归与分治

| 算法 | 类型 | Base Case | 合并方式 |
|---|---|---|---|
| 二分查找 | 减治 | `left > right` | 无 |
| 欧几里得 GCD | 减治 | `y == 0` | 无 |
| 归并排序 | 分治 | `len <= 1` | `merge` |
| 逆序对 | 分治 | `len <= 1` | `merge` 时计数 |
| 快速排序 | 分治 | `len <= 1` | 分区后拼接 |

### 常见复杂度

| 复杂度 | 典型例子 |
|---|---|
| `O(1)` | 列表按索引访问、字典按键访问 |
| `O(log n)` | 二分查找 |
| `O(n)` | 线性查找、词频统计 |
| `O(n log n)` | 归并排序 |
| `O(n^2)` | 简单快排最坏情况、`list.pop(0)` 循环清空 |