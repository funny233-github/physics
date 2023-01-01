# 前置依赖
---

本项目需要 Python3 作为运行环境！

```bash
python3 -m pip install numpy matplotlib
```

# 使用方法
---

## 三体问题数值模拟

```bash
python3 physics.py
```

将在当前工作目录下生成 `nomal.png` 文件。

## 完全弹性碰撞计数

左侧为一固定墙体，右侧的光滑表面上依次有一静止质点 A 和运动质点 B ，质点 B 初速度 1m/s 向左。两个质点之间或者质点 A 与墙体之间可能发生碰撞，一切碰撞为完全弹性碰撞。

依次给定质点 A 和 B 的质量（单位：kg），输出每次碰撞后各质点的速度（以向左为速度正方向），并累计碰撞次数。

```bash
python3 collisions.py <质点A质量> <质点B质量>
```

#更新
---
添加了`dynatic_energy`函数计算动能,添加`modulus`函数计算向量模
