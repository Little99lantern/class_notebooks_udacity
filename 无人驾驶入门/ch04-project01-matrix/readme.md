
根据udacity reviews优化
1. list(zip(*self.g))是一个把二维的数组 的行 和列交换的操作。参考https://blog.csdn.net/u010039733/article/details/48448313
    没有在代码中实现
2. Add(): 一行搞定： Matrix([[self[i][j] + other[i][j] for j in range(self.w)] for i in range(self.h)])
3. Neg: 一行搞定： Matrix([[-self[i][j] for j in range(self.w)] for i in range(self.h)])

优化后文件:matrix_modified.py
