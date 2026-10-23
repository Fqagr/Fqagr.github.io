---
title: 算法笔记：排序
date: 2026-10-23
category: notes
subject: dsa
summary: 桶排序、选择、冒泡、插入、快速排序与三路快排的原理、代码与复杂度对比。
---

# Algorithm · Sort 排序

> 注：主要看函数部分，头尾（IO）一致，不想删改了。

## 0. 预备概念

| 概念 | 含义 |
|---|---|
| 基于比较 | 通过元素间比较决定顺序，下界 $O(n\log n)$ |
| 不基于比较 | 利用值本身的分布（如桶/计数排序），可突破到 $O(n)$ |
| 稳定性 | 相同值的元素排序后**相对位置**是否保持不变 |
| 原地排序 | 是否只使用 $O(1)$ 额外空间 |
| 时间复杂度 | 平均 / 最坏，见各节 |

---

## 1. 桶排序：不基于比较，非原地，稳定*

**思路**：找到最小值 `min_value` 作为基准线，把每个元素减去基准线后放入对应的桶（计数），再按桶序重新装回。

- 时间复杂度：$O(n + V)$，其中 $V$ 是值域范围
- 缺点：值域 $V$ 不能过大（空间 $O(V)$）
- *稳定性说明：对纯整数无所谓；若桶里存的是记录，朴素的"按序重装"会打乱相同值，稳定版需要前缀和 + 逆序回填

```cpp
#include <iostream>
using namespace std;

const int MAXN = 1e5 + 8;
const int MAXV = 1e5 + 8;   // cnt 大小要覆盖值域范围！
int n;
int a[MAXN];
int cnt[MAXV];              // cnt[v] = (v + min_value) 出现的次数

void bucket_sort() {
    // 1. 找最小值作为基准线
    int min_value = a[1];   // a 从 1 开始使用
    for (int i = 2; i <= n; i++)
        if (a[i] < min_value) min_value = a[i];

    // 2. 计数：减去基准线后放入对应的桶
    for (int i = 1; i <= n; i++)
        cnt[a[i] - min_value]++;

    // 3. 重新装回：按值的顺序遍历"桶"，而不是遍历 1..n！
    int idx = 1;
    for (int v = 0; v < MAXV; v++) {
        for (int j = 1; j <= cnt[v]; j++)
            a[idx++] = v + min_value;   // 之前减掉的现在加回来
    }
}

int main() {
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];
    bucket_sort();
    for (int i = 1; i <= n; i++) cout << a[i] << " ";
    return 0;
}
```

```python
def bucket_sort(a):
    if not a:
        return a
    mn = min(a)
    cnt = [0] * (max(a) - mn + 1)
    for x in a:
        cnt[x - mn] += 1
    res = []
    for v, c in enumerate(cnt):
        res.extend([v + mn] * c)
    return res
```

---

## 2. 选择排序：未排序区间选最大值放到最后，$O(n^2)$，不稳定

**不常用，有印象即可。** 为什么记索引而不是记值：如果只存最大值，交换时原位置的值会丢失。

```cpp
#include <iostream>
using namespace std;

const int MAXN = 1e5 + 8;
int n;
int a[MAXN];

void select_sort() {
    for (int i = n; i >= 2; i--) {      // i 是未排序区的右端
        int max_index = 1;
        for (int j = 1; j <= i; j++)
            if (a[j] > a[max_index]) max_index = j;
        swap(a[max_index], a[i]);       // 交换会破坏稳定性（远距离交换）
    }
}

int main() {
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];
    select_sort();
    for (int i = 1; i <= n; i++) cout << a[i] << " ";
    return 0;
}
```

```python
def select_sort(a):
    for i in range(len(a) - 1, 0, -1):
        mi = max(range(i + 1), key=lambda j: a[j])
        a[mi], a[i] = a[i], a[mi]
```

---

## 3. 冒泡排序：相邻两两比较，大者后移，$O(n^2)$，稳定

**优化点**：记录每轮交换次数。某轮零交换说明已整体有序，直接停止——基本有序时进化到 $O(n)$。不记录的话表现与选择排序一样死板。

```cpp
#include <iostream>
using namespace std;

const int MAXN = 1e5 + 8;
int n;
int a[MAXN];

void bubble_sort() {
    for (int i = n; i >= 2; i--) {
        int swap_times = 0;             // 每轮单独计数
        for (int j = 1; j <= i - 1; j++) {
            if (a[j] > a[j + 1]) {      // 严格大于：相等不换，保证稳定性
                swap(a[j], a[j + 1]);
                swap_times++;
            }
        }
        if (swap_times == 0) break;     // 一轮零交换 => 已经有序
    }
}

int main() {
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];
    bubble_sort();
    for (int i = 1; i <= n; i++) cout << a[i] << " ";
    return 0;
}
```

```python
def bubble_sort(a):
    for i in range(len(a) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
```

---

## 4. 插入排序：维护有序前缀，新元素向前插到正确位置，$O(n^2)$，稳定

**基本有序时进化为 $O(n)$**：每个元素的移动距离 ≈ 逆序对数，几乎有序时几乎不移动。数据量小或近乎有序时它反而是最快的。

```cpp
#include <iostream>
using namespace std;

const int MAXN = 1e5 + 8;
int n;
int a[MAXN];

void insert_sort() {
    for (int i = 2; i <= n; i++) {      // 新元素 a[i]
        int j = i;
        while (j > 1 && a[j] < a[j - 1]) {  // 向前冒泡到正确位置
            swap(a[j], a[j - 1]);
            j--;
        }
    }
}

int main() {
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];
    insert_sort();
    for (int i = 1; i <= n; i++) cout << a[i] << " ";
    return 0;
}
```

```python
def insert_sort(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
```

---

## 5. 快速排序：原地，平均 $O(n\log n)$，最坏 $O(n^2)$，不稳定

### 5.1 原理

选定基准值 `t`（pivot），通过一趟分区把数组切成两部分，使得：

$$\underbrace{a[l..i-1]}_{\le t} \;|\; \underbrace{a[i]}_{=t} \;|\; \underbrace{a[i+1..r]}_{\ge t}$$

然后对左右两部分**递归**做同样的事。与归并不同，快排的处理在递归**之前**完成（先分区后递归），且分区是原地的。

**分区过程（交换法）**——用双指针从两端向中间清扫：

1. `i` 从左往右找第一个 $\ge t$ 的元素（"放右边太小的"）
2. `j` 从右往左找第一个 $\le t$ 的元素（"放左边太大的"）
3. 两者都停且未相遇 → 交换，使小的去左边、大的去右边
4. 相遇后，`t` 恰好落在 `a[i]`，分区完成

**不变量**：任意时刻，`i` 左侧（已扫过区）都 $\le t$，`j` 右侧（已扫过区）都 $\ge t$。`i < j` 守卫保证扫描和交换只发生在未处理区内部。

### 5.2 代码

```cpp
#include <iostream>
using namespace std;

const int MAXN = 1e5 + 8;
int n;
int a[MAXN];

void quick_sort(int l, int r) {
    if (l >= r) return;                 // 终止：空区间 / 单元素
    int mid = (l + r) / 2;
    swap(a[l], a[mid]);                 // 取中点当基准：防止基本有序时退化成 O(n^2)
    int t = a[l];                       // t 未离开数组，随交换在坑位间漂移
    int i = l, j = r;
    while (i < j) {
        while (i < j && a[j] >= t) j--; // >= ：等于基准也算"同侧"，跳过
        if (i < j) swap(a[i++], a[j]);
        while (i < j && a[i] <= t) i++;
        if (i < j) swap(a[j--], a[i]);
    }
    a[i] = t;                           // 此时 a[i] 本就是 t，此行为防御性写法
    quick_sort(l, i - 1);
    quick_sort(i + 1, r);
}

int main() {
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];
    quick_sort(1, n);
    for (int i = 1; i <= n; i++) cout << a[i] << " ";
    return 0;
}
```

### 5.3 细节与易错点

- **`i < j` 守卫不能删**：删掉后指针会越过相遇点，交换破坏已分区区域（挖坑法里则会导致元素被吞）
- **扫描的等号问题**：`a[j] >= t` / `a[i] <= t` 跳过等于基准的元素——**全相等的数组每趟都近似对半分**，整体仍是 $O(n\log n)$；反之用严格不等号会让相等元素反复交换，全相等时退化 $O(n^2)$
- **基准选取**：固定取 `a[l]` 时，对已有序数组每趟只切掉一个元素 → $O(n^2)$。取中点或随机化（`swap(a[l], a[rand()%(r-l+1)+l])`）可避免
- **终止条件**：`if (l >= r) return` 与递归前的区间守卫是二选一的关系，不能同时都不写

### 5.4 复杂度

| 场景 | 复杂度 | 原因 |
|---|---|---|
| 平均 | $O(n\log n)$ | 每趟近似对半分，共 $\log n$ 层，每层 $O(n)$ |
| 最坏 | $O(n^2)$ | 基准总选到极值（如有序数组取端点） |
| 空间 | $O(\log n)$ | 递归栈；原地分区无额外数组 |

```python
def quick_sort(a):
    if len(a) <= 1:
        return a
    t = a[len(a) // 2]
    left  = [x for x in a if x < t]
    mid   = [x for x in a if x == t]
    right = [x for x in a if x > t]
    return quick_sort(left) + mid + quick_sort(right)
```

> 注：Python 版为便于理解写成非原地的三段式，这其实就是三路分区的思想，见下一节。

---

## 6. 三路快排：每次分区额外确定"等于 t"的整段，重复元素多时显著更优

### 6.1 原理（荷兰国旗问题）

两路快排只把数组分成 $\le t$ 和 $\ge t$ 两段，等于 `t` 的元素散落在两边、还要被反复比较。三路分区用**三个指针**把数组一次分成**三段**：

$$\underbrace{a[l..i-1]}_{<t} \;|\; \underbrace{a[i..j]}_{=t} \;|\; \underbrace{a[j+1..r]}_{>t}$$

扫描指针 `k` 在未知区 `[k, j]` 里逐个检查，像探照灯一样把元素甩向两侧：

| 判断 | 动作 | 为什么 |
|---|---|---|
| `a[k] > t` | `swap(a[k],a[j]); j--`（**k 不动**） | 换回来的是未知区的元素，还没检查 |
| `a[k] == t` | `k++` | 本来就属于中段，原地扩展 |
| `a[k] < t` | `swap(a[k],a[i]); i++; k++` | 换回来的是"== t"区的元素，身份已知，可跳过 |

**不变量**：任意时刻 `[l, i-1]` 全 $< t$，`[i, k-1]` 全 $= t$，`[j+1, r]` 全 $> t$，`[k, j]` 未知。循环到 `k > j` 时未知区消失，分区完成。

### 6.2 代码

```cpp
#include <iostream>
using namespace std;

const int MAXN = 1e5 + 8;
int n;
int a[MAXN];

void quick_third_sort(int l, int r) {
    if (l >= r) return;
    int i = l, j = r, k = l;            // j 从 r 开始！（j 是右边界）
    int mid = (l + r) / 2;
    swap(a[l], a[mid]);
    int t = a[l];
    while (k <= j) {
        if (a[k] > t) {                 // 更大，甩给右边
            swap(a[k], a[j]);
            j--;
            // k 不动：a[k] 现在是从右边换来的未知元素
        } else if (a[k] == t) {         // 相等，原地留下
            k++;
        } else {                        // 更小，甩给左边
            swap(a[k], a[i]);
            i++;
            k++;                        // 换来的 a[i] 一定是 == t 区的，已看过
        }
    }
    // 循环结束后 [i, j] 内全部 == t，无需再逐个赋值
    quick_third_sort(l, i - 1);
    quick_third_sort(j + 1, r);
}

int main() {
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];
    quick_third_sort(1, n);
    for (int i = 1; i <= n; i++) cout << a[i] << " ";
    return 0;
}
```

### 6.3 与两路快排的对比

| | 两路 | 三路 |
|---|---|---|
| 分区结果 | $\le t$ / $\ge t$ 两段 | $<t$ / $=t$ / $>t$ 三段 |
| 相等元素 | 参与交换、散落两侧 | 一次归拢进中段，不再参与递归 |
| 全相等数组 | 取决于实现，可能退化 | **一趟结束**，$O(n)$ |
| 典型应用 | 通用排序 | 重复元素多；快速选择第 k 小 |

三路分区还是**快速选择（quickselect）**求第 $m$ 小的基础：分区后若 $m$ 落在 $[i, j]$（等于段）内，答案直接是 `t`；否则只需递归一侧。

```python
def quick_third_sort(a):
    if len(a) <= 1:
        return a
    t = a[len(a) // 2]
    left  = [x for x in a if x < t]
    mid   = [x for x in a if x == t]
    right = [x for x in a if x > t]
    return quick_third_sort(left) + mid + quick_third_sort(right)
```

---

## 7. 总结对比

| 算法 | 平均 | 最坏 | 空间 | 稳定 | 特点 |
|---|---|---|---|---|---|
| 桶排序 | $O(n+V)$ | $O(n+V)$ | $O(V)$ | 视实现 | 值域小才划算 |
| 选择排序 | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ✗ | 交换次数最少 |
| 冒泡排序 | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ✓ | 基本有序时 $O(n)$ |
| 插入排序 | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ✓ | 小数据 / 近乎有序之王 |
| 快速排序 | $O(n\log n)$ | $O(n^2)$ | $O(\log n)$ | ✗ | 通用最快，注意基准选取 |
| 三路快排 | $O(n\log n)$ | $O(n^2)$ | $O(\log n)$ | ✗ | 重复元素多时最优 |
