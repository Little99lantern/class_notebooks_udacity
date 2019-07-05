# 可优化点 (可以参考后面的C++优化课程)

```cpp
// initialize newGrid to zeros
    vector <float> row;
    for (int i=0;i<height;i++){
        row.clear();
        for (int j=0;j<width;j++){
            row.push_back(0.0);
        }
        newGrid.push_back(row);
    }
```

你可以不用这么正经得初始化哈，你可以直接复制一个同样结构的newGrid，然后把里面的东西都改一下

## initialize_beliefs

你可以用以下方式来初始化你的矩阵～  
```cpp
vector< vector <float> > newGrid (rows , vector< float >(cols , beliefs));
```

## sense

你可以用以下方式来简化你的代码～

```cpp
int hit = (color == grid[i][j]);
newGrid[i][j] = beliefs[i][j] * (hit * p_hit + (1 - hit) * p_miss);
```

# move

你也可以使用以下方式来简化你的代码～

```cpp
newGrid[(i+dy)%rows][(j+dx)%cols]=beliefs[i][j];
或者
newGrid[i][j] = beliefs[(i - dx+height) % height][(j - dy+width) % width];
```
