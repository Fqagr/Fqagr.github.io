---
title: FIP 期中模拟题
date: 2026-11-03
category: notes
subject: python
summary: 期中模拟题
---

# FIP W1-W7 期中模拟题 A卷

满分：100 分  
时间：45 分钟  
形式：纸质闭卷  
复习范围：W1-W7  

## 一、选择题（1-20，每题 2 分，共 40 分）

1. `input()` 的返回值类型是？

   A. `int`  
   B. `float`  
   C. `str`  
   D. `bool`

2. `print(9 // 2, 9 % 2)` 的输出是？

   A. `4 1`  
   B. `4.5 1`  
   C. `4 2`  
   D. `5 1`

3. `range(2, 6)` 产生的整数序列是？

   A. `2, 3, 4, 5, 6`  
   B. `2, 3, 4, 5`  
   C. `2, 3, 4`  
   D. `3, 4, 5, 6`

4. 执行 `x = 3` 后再执行 `x *= 4`，此时 `x` 的值是？

   A. `7`  
   B. `12`  
   C. `34`  
   D. `3`

5. 当 `x = 5` 时，表达式 `x % 2 == 0 and x > 0` 的结果是？

   A. `True`  
   B. `False`  
   C. 报错  
   D. 无法确定

6. `break` 的作用是？

   A. 结束整个程序  
   B. 跳出当前循环  
   C. 结束当前函数  
   D. 跳过本次循环，继续下一轮

7. `for` 循环的 `else` 子句何时执行？

   A. 循环被 `break` 打断时  
   B. 循环正常结束且没有被 `break` 打断时  
   C. 每次迭代后都会执行  
   D. 永远不会执行

8. `len("hello")` 的结果是？

   A. `4`  
   B. `5`  
   C. `6`  
   D. 报错

9. 若 `xs = [1, 2, 3, 4]`，那么 `xs[1:3]` 的结果是？

   A. `[1, 2, 3]`  
   B. `[2, 3]`  
   C. `[2, 3, 4]`  
   D. `[1, 2]`

10. 下列关于别名和拷贝的说法正确的是？

   A. `b = a` 和 `b = a[:]` 完全等价  
   B. `b = a` 让 `a` 和 `b` 指向同一个列表对象  
   C. `b = a[:]` 让 `a` 和 `b` 指向同一个对象  
   D. 列表没有别名问题

11. 若 `d = {}`，则 `d.get("x", 0)` 的结果是？

   A. `KeyError`  
   B. `None`  
   C. `0`  
   D. `''`

12. `len({1, 2, 2, 3})` 的结果是？

   A. `2`  
   B. `3`  
   C. `4`  
   D. 报错

13. `sum([1, 2, 3])` 的结果是？

   A. `3`  
   B. `5`  
   C. `6`  
   D. 报错

14. 下面代码的输出是什么？

   ```python
   for i, x in enumerate([10, 20]):
       print(i, x)
   ```

   A. `0 10` 和 `1 20` 两行  
   B. `1 10` 和 `2 20` 两行  
   C. `10 0` 和 `20 1` 两行  
   D. 报错

15. 递归函数必须有 Base Case 的主要原因是？

   A. 为了让返回值更精确  
   B. 防止无限递归  
   C. 提高代码可读性  
   D. 便于使用记忆化

16. 二分查找的时间复杂度是？

   A. `O(1)`  
   B. `O(log n)`  
   C. `O(n)`  
   D. `O(n log n)`

17. 归并排序的平均时间复杂度是？

   A. `O(1)`  
   B. `O(log n)`  
   C. `O(n)`  
   D. `O(n log n)`

18. 关于 `a.sort()` 和 `sorted(a)` 的说法正确的是？

   A. 两者都会修改 `a`  
   B. `a.sort()` 会修改 `a`，`sorted(a)` 返回新列表  
   C. 两者都返回新列表  
   D. 两者都不修改 `a`

19. `print(f"{2.71828:.2f}")` 的输出是？

   A. `2.72`  
   B. `2.7`  
   C. `2.71828`  
   D. `2.718`

20. `type([])` 的结果是？

   A. `<class 'tuple'>`  
   B. `<class 'dict'>`  
   C. `<class 'list'>`  
   D. `<class 'set'>`

## 二、程序填空（每空 5 分，共 40 分）

每题有两个空，请把空填完整。

### 21. 判断素数

```python
def is_prime(x):
    if x < 2:
        return False
    for k in range(2, ______):
        if x % k == 0:
            return False
    return ______
```

### 22. 最大公约数

```python
a, b = map(int, input().split())
while ______:
    a, b = ______
print(a)
```

### 23. 二分查找

```python
def binary_search(xs, target):
    left, right = 0, len(xs) - 1
    while ______:
        mid = (left + right) // 2
        if xs[mid] == target:
            return mid
        if xs[mid] < target:
            left = ______
        else:
            right = mid - 1
    return -1
```

### 24. 词频统计

```python
count = {}
for word in text.______:
    count[word] = count.get(word, ______) + 1
```

## 三、程序输出（25-28，每题 5 分，共 20 分）

### 25.

```python
x = 5
while x > 0:
    print(x, end=" ")
    x -= 2
```

### 26.

```python
xs = [1, 2, 3]
xs.extend([4, 5])
xs.append(6)
xs.remove(2)
print(xs[1:4])
```

### 27.

```python
def f(n):
    if n <= 1:
        return n
    return f(n - 1) + f(n - 2)

print(f(5))
```

### 28.

```python
d = {"a": 1, "b": 2}
d["c"] = d.get("a", 0) + 1
print(len(d), d["c"])
```

# FIP W1-W7 期中模拟题 B卷

满分：100 分  
时间：45 分钟  
形式：纸质闭卷  
复习范围：W1-W7  

## 一、选择题（1-20，每题 2 分，共 40 分）

1. `print(list(range(10, 0, -3)))` 的输出是？

   A. `[10, 7, 4, 1]`  
   B. `[10, 7, 4]`  
   C. `[9, 6, 3]`  
   D. `[10, 9, 8]`

2. `"A" in "abc"` 的结果是？

   A. `True`  
   B. `False`  
   C. 报错  
   D. 无法确定

3. `len("abc")` 的结果是？

   A. `2`  
   B. `3`  
   C. `4`  
   D. 报错

4. `str(1) + str(2)` 的结果是？

   A. `3`  
   B. `"12"`  
   C. `"3"`  
   D. 报错

5. `bool([])` 的结果是？

   A. `True`  
   B. `False`  
   C. `None`  
   D. 报错

6. 若 `xs = [1, 2, 3]`，则 `xs.pop()` 返回？

   A. `1`  
   B. `2`  
   C. `3`  
   D. `None`

7. `(1,)` 的类型是？

   A. `int`  
   B. `tuple`  
   C. `list`  
   D. `dict`

8. `len({1, 2, 2, 3})` 的结果是？

   A. `2`  
   B. `3`  
   C. `4`  
   D. 报错

9. 下列哪个可以作为字典的键？

   A. `[1, 2]`  
   B. `(1, 2)`  
   C. `{1: 2}`  
   D. `set([1, 2])`

10. 下面代码的输出是？

   ```python
   f = lambda x: x * x
   print(f(3))
   ```

   A. `6`  
   B. `9`  
   C. `3`  
   D. 报错

11. `sum([x * x for x in range(3)])` 的结果是？

   A. `0`  
   B. `3`  
   C. `5`  
   D. `9`

12. `sorted([3, 1, 2], key=lambda x: -x)` 的结果是？

   A. `[1, 2, 3]`  
   B. `[3, 2, 1]`  
   C. `[1, 3, 2]`  
   D. `[2, 3, 1]`

13. 递归函数必须写 Base Case，主要目的是？

   A. 防止无限递归  
   B. 增加可读性  
   C. 避免使用循环  
   D. 便于打印结果

14. 快速排序的平均时间复杂度是？

   A. `O(1)`  
   B. `O(log n)`  
   C. `O(n)`  
   D. `O(n log n)`

15. `max([1, -2, 3], key=abs)` 的结果是？

   A. `1`  
   B. `-2`  
   C. `3`  
   D. 报错

16. 二分查找的前提条件是？

   A. 列表必须为空  
   B. 列表必须有序  
   C. 列表必须去重  
   D. 列表必须全为整数

17. 若 `d = {"a": 1}`，则 `d.get("b", 2)` 的结果是？

   A. `1`  
   B. `2`  
   C. `None`  
   D. 报错

18. 下列关于 `append` 和 `extend` 的说法正确的是？

   A. `append([3, 4])` 会把 `3` 和 `4` 拆开加入  
   B. `extend([3, 4])` 会把整个列表作为一个元素加入  
   C. `append([3, 4])` 会把整个列表作为一个元素加入  
   D. 两者完全等价

19. `print(f"{3.14159:.2f}")` 的输出是？

   A. `3.14`  
   B. `3.1`  
   C. `3.14159`  
   D. `3.142`

20. `set()` 的作用是？

   A. 创建空列表  
   B. 创建空字典  
   C. 创建空集合  
   D. 创建空元组

## 二、程序填空（每空 5 分，共 40 分）

每题有两个空，请把空填完整。

### 21. 阶乘

```python
def factorial(n):
    if n <= 1:
        return ______
    return ______ * factorial(n - 1)
```

### 22. 快速排序

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = ______
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + ______
```

### 23. 合并两个有序列表

```python
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and ______:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return ______
```

### 24. 词频统计

```python
count = {}
for word in text.______:
    count[word] = count.get(word, 0) + ______
```

## 三、程序输出（25-28，每题 5 分，共 20 分）

### 25.

```python
print(list(range(10, 0, -3)))
```

### 26.

```python
s = "a,b,c"
print(s.split(","), "-".join(s.split(",")))
```

### 27.

```python
d = {}
d[1] = 1
d[2] = d.get(1, 0) + 1
print(d)
```

### 28.

```python
def f(n):
    if n == 0:
        return 1
    return n + f(n - 1)

print(f(4))
```

# FIP W1-W7 期中模拟题 C卷

满分：100 分  
时间：45 分钟  
形式：纸质闭卷  
复习范围：W1-W7  

## 一、选择题（1-20，每题 2 分，共 40 分）

1. `print(list(zip([1, 2, 3], "abc")))` 的输出是？

   A. `[(1, 'a'), (2, 'b'), (3, 'c')]`  
   B. `[(1, 'a'), (2, 'b')]`  
   C. `[['1', 'a'], ['2', 'b'], ['3', 'c']]`  
   D. 报错

2. `len({1, 2, 3}.intersection({2, 3, 4}))` 的结果是？

   A. `1`  
   B. `2`  
   C. `3`  
   D. `4`

3. `print(list(map(str, range(3))))` 的输出是？

   A. `['0', '1', '2']`  
   B. `[0, 1, 2]`  
   C. `['1', '2', '3']`  
   D. 报错

4. `print(list(reversed([1, 2, 3])))` 的输出是？

   A. `[1, 2, 3]`  
   B. `[3, 2, 1]`  
   C. `3 2 1`  
   D. 报错

5. `max([1, -2, 3], key=abs)` 的结果是？

   A. `1`  
   B. `-2`  
   C. `3`  
   D. 报错

6. `"hello".replace("l", "L")` 的结果是？

   A. `"heLLo"`  
   B. `"heLlo"`  
   C. `"hello"`  
   D. 报错

7. `"abc".upper()` 的结果是？

   A. `"ABC"`  
   B. `"Abc"`  
   C. `"abc"`  
   D. 报错

8. `"1,2,3".split(",")` 的结果是？

   A. `['1', '2', '3']`  
   B. `[1, 2, 3]`  
   C. `('1', '2', '3')`  
   D. `"1 2 3"`

9. 下面代码的输出是？

   ```python
   def f(n):
       if n <= 1:
           return 1
       return n * f(n - 1)

   print(f(4))
   ```

   A. `10`  
   B. `24`  
   C. `12`  
   D. `6`

10. 下面代码的输出是？

   ```python
   def g(n):
       if n == 0:
           return 0
       return n + g(n - 1)

   print(g(5))
   ```

   A. `5`  
   B. `10`  
   C. `15`  
   D. `20`

11. 归并排序的平均时间复杂度是？

   A. `O(1)`  
   B. `O(log n)`  
   C. `O(n)`  
   D. `O(n log n)`

12. 快速排序的平均时间复杂度是？

   A. `O(1)`  
   B. `O(log n)`  
   C. `O(n)`  
   D. `O(n log n)`

13. 简洁版快速排序选取首元素作基准时，最坏情况可能退化为？

   A. `O(1)`  
   B. `O(log n)`  
   C. `O(n)`  
   D. `O(n^2)`

14. 二分查找要求的数据状态是？

   A. 无序即可  
   B. 必须有序  
   C. 必须去重  
   D. 必须全为正数

15. `functools.lru_cache` 的主要作用是？

   A. 打印函数调用过程  
   B. 缓存函数结果，避免重复计算  
   C. 提高函数可读性  
   D. 自动修改善误

16. `print(list(range(2, 10, 3)))` 的输出是？

   A. `[2, 5, 8]`  
   B. `[2, 5, 8, 10]`  
   C. `[2, 4, 6, 8]`  
   D. `[3, 6, 9]`

17. `list.pop(0)` 的时间复杂度通常是？

   A. `O(1)`  
   B. `O(log n)`  
   C. `O(n)`  
   D. `O(n log n)`

18. 关于 `a.sort()` 和 `sorted(a)` 的说法正确的是？

   A. 两者都会修改 `a`  
   B. `a.sort()` 会修改 `a`，`sorted(a)` 返回新列表  
   C. 两者都返回新列表  
   D. 两者都不修改 `a`

19. 若 `d = {"a": 1}`，则 `d.get("b", 2)` 的结果是？

   A. `1`  
   B. `2`  
   C. `None`  
   D. 报错

20. `len({1, 2, 2})` 的结果是？

   A. `1`  
   B. `2`  
   C. `3`  
   D. 报错

## 二、程序填空（每空 5 分，共 40 分）

每题有两个空，请把空填完整。

### 21. 记忆化杨辉三角

```python
def pascal_memo(n, k, memo=None):
    if memo is None:
        memo = {}
    if (n, k) in memo:
        return memo[(n, k)]
    if k == ______ or k == n:
        return 1
    memo[(n, k)] = pascal_memo(n - 1, k - 1, memo) + ______
    return memo[(n, k)]
```

### 22. 合并两个有序列表

```python
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and ______:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return ______
```

### 23. 快速排序

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = ______
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + ______
```

### 24. 两数之和

```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if ______ in seen:
            return [seen[x], i]
        seen[target - x] = ______
    return []
```

## 三、程序输出（25-28，每题 5 分，共 20 分）

### 25.

```python
print(list(zip([1, 2, 3], "abc")))
```

### 26.

```python
d = {1: 2, 3: 4}
print(sorted(d.items(), key=lambda x: -x[1]))
```

### 27.

```python
print(list(map(str, range(3))))
```

### 28.

```python
def f(n):
    if n == 0:
        return 0
    return n + f(n - 1)

print(f(5))
```

# FIP W1-W7 期中模拟题答案解析

## A卷答案

### 选择题

1. C。`input()` 返回字符串。
2. A。`9 // 2` 是 4，`9 % 2` 是 1。
3. B。`range(2, 6)` 不包含 6。
4. B。`x *= 4` 等价于 `x = x * 4`，所以是 12。
5. B。`5 % 2 == 0` 为 False。
6. B。`break` 会跳出当前最近一层循环。
7. B。循环正常结束且没有被 `break` 打断时才执行 `else`。
8. B。字符串 `"hello"` 有 5 个字符。
9. B。切片左闭右开，`xs[1:3]` 取下标 1 和 2。
10. B。`b = a` 让两个名字指向同一个列表对象。
11. C。`get` 的第二个参数是缺省值。
12. B。集合自动去重。
13. C。1 + 2 + 3 = 6。
14. A。`enumerate` 从 0 开始给下标。
15. B。没有 Base Case 会无限递归。
16. B。二分查找每次缩小一半范围。
17. D。归并排序是 `O(n log n)`。
18. B。`sort()` 原地修改，`sorted()` 返回新列表。
19. A。`.2f` 保留两位小数。
20. C。空列表的类型是 `list`。

### 程序填空

21. `int(x ** 0.5) + 1`，`True`。  
    说明：只需枚举到平方根附近，全部检查完仍没有因子就是素数。

22. `b`，`b, a % b`。  
    说明：这是辗转相除法，`b` 为 0 时结束。

23. `left <= right`，`mid + 1`。  
    说明：二分查找要保留右侧时排除中间位置。

24. `split()`，`0`。  
    说明：先把文本按空白切分，再用 `get` 处理首次出现的词。

### 程序输出

25. `5 3 1`

26. `[3, 4, 5]`

27. `5`

28. `3 2`

## B卷答案

### 选择题

1. A。`range(10, 0, -3)` 依次是 10、7、4、1。
2. B。`"A"` 和 `"a"` 是不同字符。
3. B。`"abc"` 有 3 个字符。
4. B。两个字符串拼接得到 `"12"`。
5. B。空列表为假值。
6. C。`pop()` 默认弹出末尾元素。
7. B。单元素元组必须有逗号。
8. B。集合自动去重。
9. B。元组可作为字典键，列表、字典、集合不行。
10. B。`3 * 3 = 9`。
11. C。`0 + 1 + 4 = 5`。
12. B。`-x` 使排序按从大到小。
13. A。Base Case 用来防止无限递归。
14. D。快速排序平均复杂度是 `O(n log n)`。
15. C。`abs(3)` 最大。
16. B。二分查找必须有序。
17. B。`get` 的第二个参数是缺省值。
18. C。`append([3, 4])` 把整个列表作为一个元素加入。
19. A。`.2f` 保留两位小数。
20. C。`set()` 创建空集合，空字典是 `{}`。

### 程序填空

21. `1`，`n`。  
    说明：阶乘的 Base Case 返回 1，递归步是 `n * factorial(n - 1)`。

22. `arr[0]`，`quick_sort(right)`。  
    说明：简洁版快排取首元素作基准，再递归右侧。

23. `j < len(right)`，`result`。  
    说明：合并时要同时检查左右两边，最后返回合并结果。

24. `split()`，`1`。  
    说明：词频统计要按空白切分，每次出现计数加 1。

### 程序输出

25. `[10, 7, 4, 1]`

26. `['a', 'b', 'c'] a-b-c`

27. `{1: 1, 2: 2}`

28. `11`

## C卷答案

### 选择题

1. A。`zip` 按位置配对。
2. B。两个集合的交集是 `{2, 3}`，长度为 2。
3. A。`map(str, ...)` 把每个整数转成字符串。
4. B。`reversed` 会反向遍历序列。
5. C。`abs(3)` 最大。
6. A。`replace` 会替换所有出现的 `"l"`。
7. A。`upper()` 转全大写。
8. A。`split(",")` 得到字符串列表。
9. B。`4! = 24`。
10. C。5 + 4 + 3 + 2 + 1 = 15。
11. D。归并排序是 `O(n log n)`。
12. D。快速排序平均是 `O(n log n)`。
13. D。最坏情况下可能退化为 `O(n^2)`。
14. B。二分查找必须有序。
15. B。`lru_cache` 用来缓存函数结果。
16. A。`range(2, 10, 3)` 依次是 2、5、8。
17. C。删除头部元素会让后面整体前移。
18. B。`sort()` 原地修改，`sorted()` 返回新列表。
19. B。`get` 的第二个参数是缺省值。
20. B。集合自动去重。

### 程序填空

21. `0`，`pascal_memo(n - 1, k, memo)`。  
    说明：杨辉三角两侧为 1，中间由上一行两个肩膀相加。

22. `j < len(right)`，`result`。  
    说明：合并时要同时检查左右两边，最后返回合并结果。

23. `arr[0]`，`quick_sort(right)`。  
    说明：简洁版快排取首元素作基准，再递归右侧。

24. `target - x`，`i`。  
    说明：记录补数出现的位置，遇到另一个数即可返回两个下标。

### 程序输出

25. `[(1, 'a'), (2, 'b'), (3, 'c')]`

26. `[(3, 4), (1, 2)]`

27. `['0', '1', '2']`

28. `15`


# FIP W8 重点模拟题 D卷

满分：100 分  
时间：45 分钟  
形式：纸质闭卷  
重点范围：W8 数据结构 + dict.get / setdefault / deque / 栈 / 队列  

## 一、选择题（1-20，每题 2 分，共 40 分）

1. 哪种结构是 LIFO？

   A. 队列  
   B. 栈  
   C. 列表  
   D. 字典

2. 哪种结构是 FIFO？

   A. 栈  
   B. 队列  
   C. 元组  
   D. 集合

3. 在 Python 中，最常用的双端队列结构是？

   A. `list`  
   B. `tuple`  
   C. `dict`  
   D. `collections.deque`

4. `list.pop(0)` 的时间复杂度通常是？

   A. `O(1)`  
   B. `O(log n)`  
   C. `O(n)`  
   D. `O(n log n)`

5. `deque.popleft()` 的时间复杂度通常是？

   A. `O(1)`  
   B. `O(log n)`  
   C. `O(n)`  
   D. `O(n^2)`

6. 下列哪个可以作为字典的键？

   A. `[1, 2]`  
   B. `(1, 2)`  
   C. `{1: 2}`  
   D. `set([1, 2])`

7. `d.get(k, default)` 在键 `k` 不存在时会？

   A. 抛出 `KeyError`  
   B. 返回 `None`  
   C. 返回 `default`  
   D. 自动插入 `default`

8. `d.setdefault(k, default)` 在键 `k` 不存在时会？

   A. 抛出 `KeyError`  
   B. 返回 `None`  
   C. 插入 `default` 并返回它  
   D. 不做任何事

9. 若 `d = {}`，则 `d.setdefault("x", 0)` 的返回值是？

   A. `None`  
   B. `0`  
   C. `"x"`  
   D. 报错

10. 若 `d = {"a": 1}`，则 `d.setdefault("a", 5)` 的返回值是？

   A. `1`  
   B. `5`  
   C. `None`  
   D. 报错

11. `d.items()` 返回的是？

   A. 只包含键的视图  
   B. 只包含值的视图  
   C. 键值对视图  
   D. 列表副本

12. 下列哪个不能作为字典键？

   A. `"abc"`  
   B. `1`  
   C. `(1, 2)`  
   D. `[1, 2]`

13. 哈希冲突指的是？

   A. 两个键映射到同一个槽位  
   B. 键不存在  
   C. 值类型错误  
   D. 表太大

14. 在 `deque` 中，右端入队常用哪个方法？

   A. `append(x)`  
   B. `appendleft(x)`  
   C. `pop()`  
   D. `popleft()`

15. 在 `deque` 中，左端出队常用哪个方法？

   A. `append(x)`  
   B. `appendleft(x)`  
   C. `pop()`  
   D. `popleft()`

16. `is_valid("{[()]}")` 的结果是？

   A. `True`  
   B. `False`  
   C. 报错  
   D. 无法确定

17. `is_valid("{[(])}")` 的结果是？

   A. `True`  
   B. `False`  
   C. 报错  
   D. 无法确定

18. 在队列中，最先进入的元素？

   A. 最先出去  
   B. 最后出去  
   C. 不确定  
   D. 永远不出去

19. 在栈中，最后进入的元素？

   A. 最先出去  
   B. 最后出去  
   C. 不确定  
   D. 永远不出去

20. `list.pop()` 默认弹出？

   A. 左端元素  
   B. 右端元素  
   C. 最小元素  
   D. 随机元素

## 二、程序填空（每空 5 分，共 40 分）

每题有两个空，请把空填完整。

### 21. 用 list 当栈

```python
stack = []
stack.______(1)
stack.______(2)
top = stack.pop()
```

### 22. 用 dict.get 统计词频

```python
count = {}
for word in words:
    count[word] = count.______(word, 0) + ______
```

### 23. 用 deque 做队列

```python
from collections import deque
q = deque()
q.______(1)
q.______(2)
first = q.popleft()
```

### 24. 括号匹配

```python
def is_valid(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack.______ != pairs[ch]:
                return False
            stack.______()
    return not stack
```

## 三、程序输出（25-28，每题 5 分，共 20 分）

### 25.

```python
d = {}
d["a"] = d.get("a", 0) + 1
print(d)
```

### 26.

```python
d = {"a": 1}
d.setdefault("a", 5)
print(d)
```

### 27.

```python
d = {}
d.setdefault("x", 0)
print(d)
```

### 28.

```python
from collections import deque
q = deque([1, 2, 3])
q.popleft()
q.append(4)
print(q)
```

# FIP W8 重点模拟题 E卷

满分：100 分  
时间：45 分钟  
形式：纸质闭卷  
重点范围：W8 数据结构 + dict.get / setdefault / deque / 栈 / 队列  

## 一、选择题（1-20，每题 2 分，共 40 分）

1. 在栈中，最后进入的元素会？

   A. 最先出去  
   B. 最后出去  
   C. 不确定  
   D. 永远不出去

2. 在队列中，最先进入的元素会？

   A. 最先出去  
   B. 最后出去  
   C. 不确定  
   D. 永远不出去

3. `deque.popleft()` 的作用是？

   A. 从左端删除并返回元素  
   B. 从右端删除并返回元素  
   C. 只看左端元素  
   D. 清空队列

4. `list.pop(0)` 的时间复杂度通常是？

   A. `O(1)`  
   B. `O(log n)`  
   C. `O(n)`  
   D. `O(n^2)`

5. `d.get(k, default)` 在键 `k` 存在时会？

   A. 返回对应值  
   B. 返回 `default`  
   C. 插入 `default`  
   D. 抛出异常

6. `d.get(k, default)` 在键 `k` 不存在时会？

   A. 抛出 `KeyError`  
   B. 返回 `default`  
   C. 插入 `default`  
   D. 返回 `None`

7. `d.setdefault(k, default)` 在键 `k` 不存在时会？

   A. 返回 `default` 并插入  
   B. 返回 `None`  
   C. 抛出异常  
   D. 不做任何事

8. `d.setdefault(k, default)` 在键 `k` 已存在时会？

   A. 返回当前值  
   B. 覆盖旧值  
   C. 返回 `default`  
   D. 删除旧值

9. 下列哪个不能作为字典键？

   A. `"abc"`  
   B. `(1, 2)`  
   C. `1`  
   D. `[1, 2]`

10. `d.update({"b": 2})` 会？

   A. 只读取不修改  
   B. 插入或覆盖键 `"b"`  
   C. 删除键 `"b"`  
   D. 报错

11. `d.items()` 返回的是？

   A. 键值对视图  
   B. 键视图  
   C. 值视图  
   D. 列表副本

12. `d.values()` 返回的是？

   A. 键视图  
   B. 值视图  
   C. 键值对视图  
   D. 字典副本

13. `d.keys()` 返回的是？

   A. 键视图  
   B. 值视图  
   C. 键值对视图  
   D. 列表副本

14. 下列哪个方法会清空字典？

   A. `clear()`  
   B. `pop()`  
   C. `update()`  
   D. `setdefault()`

15. 下列哪个方法会从字典删除并返回某个键的值？

   A. `get()`  
   B. `setdefault()`  
   C. `pop()`  
   D. `items()`

16. 在 `deque` 中，左端入队常用？

   A. `append(x)`  
   B. `appendleft(x)`  
   C. `pop()`  
   D. `popleft()`

17. 在 `deque` 中，右端入队常用？

   A. `append(x)`  
   B. `appendleft(x)`  
   C. `pop()`  
   D. `popleft()`

18. 下列哪个最适合做撤销操作？

   A. 栈  
   B. 队列  
   C. 集合  
   D. 字典

19. 下列哪个最适合做打印任务队列？

   A. 栈  
   B. 队列  
   C. 集合  
   D. 元组

20. `is_valid("{[(])}")` 的结果是？

   A. `True`  
   B. `False`  
   C. 报错  
   D. 无法确定

## 二、程序填空（每空 5 分，共 40 分）

每题有两个空，请把空填完整。

### 21. 用 deque 做队列

```python
from collections import deque
q = deque()
q.______(1)
q.______(2)
first = q.popleft()
```

### 22. 用 setdefault 统计词频

```python
count = {}
for word in words:
    count.______(word, 0)
    count[word] += ______
```

### 23. 用 dict.update 合并

```python
a = {"x": 1}
a.______({"y": 2})
print(a)
```

### 24. 括号匹配

```python
def is_valid(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack[-1] != ______:
                return False
            stack.pop()
    return not ______
```

## 三、程序输出（25-28，每题 5 分，共 20 分）

### 25.

```python
d = {"a": 1}
d.update({"b": 2})
print(d)
```

### 26.

```python
d = {"a": 1}
print(d.get("b", 2), d.setdefault("b", 3))
```

### 27.

```python
from collections import deque
q = deque()
q.append(1)
q.appendleft(0)
print(q)
```

### 28.

```python
from collections import deque
q = deque([1, 2, 3])
q.rotate(1)
print(q)
```

# FIP W8 重点模拟题答案解析

## D卷答案

### 选择题

1. B。栈是 LIFO。
2. B。队列是 FIFO。
3. D。`collections.deque` 常用于双端队列。
4. C。`list.pop(0)` 会让后面元素整体前移，通常是 `O(n)`。
5. A。`deque.popleft()` 是 `O(1)`。
6. B。元组可以作为字典键，列表、字典、集合不行。
7. C。`get(k, default)` 在键不存在时返回 `default`，不会插入。
8. C。`setdefault(k, default)` 在键不存在时插入并返回 `default`。
9. B。`d` 原来为空，`setdefault` 会插入 `"x": 0` 并返回 `0`。
10. A。键已存在时 `setdefault` 返回当前值。
11. C。`items()` 是键值对视图。
12. D。列表不能作为字典键。
13. A。哈希冲突是不同键映射到同一槽位。
14. A。右端入队常用 `append`。
15. D。左端出队常用 `popleft`。
16. A。括号完全匹配。
17. B。括号交叉不匹配。
18. A。队列是先进先出。
19. A。栈是后进先出。
20. B。`list.pop()` 默认弹出末尾元素。

### 程序填空

21. `append`，`append`。  
    说明：`list` 可以用尾部 `append` 当作栈顶压入。

22. `get`，`1`。  
    说明：`count.get(word, 0) + 1` 是词频统计的标准写法。

23. `append`，`append`。  
    说明：队列从右端入队，再用 `popleft()` 从左端出队。

24. `[-1]`，`pop`。  
    说明：右括号来时要检查栈顶是否匹配，匹配后弹出。

### 程序输出

25. `{'a': 1}`

26. `{'a': 1}`

27. `{'x': 0}`

28. `deque([2, 3, 4])`

## E卷答案

### 选择题

1. A。栈是 LIFO。
2. A。队列是 FIFO。
3. A。`popleft()` 从左端删除并返回元素。
4. C。`list.pop(0)` 通常为 `O(n)`。
5. A。键存在时返回对应值。
6. B。键不存在时返回 `default`。
7. A。键不存在时插入并返回 `default`。
8. A。键存在时返回当前值。
9. D。列表不能作键。
10. B。`update` 会插入或覆盖键值。
11. A。`items()` 是键值对视图。
12. B。`values()` 是值视图。
13. A。`keys()` 是键视图。
14. A。`clear()` 清空字典。
15. C。`pop()` 删除并返回指定键的值。
16. B。左端入队用 `appendleft`。
17. A。右端入队用 `append`。
18. A。撤销操作通常用栈。
19. B。打印任务按先后处理，用队列。
20. B。括号交叉不匹配。

### 程序填空

21. `append`，`append`。  
    说明：队列从右端入队，之后用 `popleft()` 出队。

22. `setdefault`，`1`。  
    说明：先保证键存在并默认为 0，再累加 1。

23. `update`。  
    说明：`update` 可以批量插入或覆盖键值。

24. `pairs[ch]`，`stack`。  
    说明：栈顶必须与当前右括号匹配，最后栈应为空。

### 程序输出

25. `{'a': 1, 'b': 2}`

26. `2 3`

27. `deque([0, 1])`

28. `deque([3, 1, 2])`
