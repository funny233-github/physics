# 完全弹性碰撞统计碰撞次数
# Author：Dragon1573

from numpy import array
from numpy import matmul
from sys import argv
from re import match

# 非负浮点数
FLOAT_FORMAT = r"(^[1-9]\d*\.\d+$|^0\.\d+$|^[1-9]\d*$|^0$)"

class Engine:
    """
    物理引擎
    """

    def __init__(self, _mass_left: float, _mass_right: float) -> None:
        """
        构造方法

        Args:
            _mass_left (Decimal): 静止质点的质量
            _mass_right (Decimal): 运动质点的质量
        """
        self._total_mass = _mass_left + _mass_right
        self._mass_matrix = array(
            [
                [_mass_left - _mass_right, 2 * _mass_right],
                [2 * _mass_left, _mass_right - _mass_left]
            ]
        )
        # 两个物体的运动速度，此处速度并不重要，以向左为速度正方向
        self._velocity = array([0, 1])

    def _collide_together(self) -> None:
        """
        根据动量守恒和能量守恒更新碰撞后的速度关系

        参考公式：https://www.docin.com/p-2359663838.html
        """
        self._velocity = matmul(self._mass_matrix, self._velocity.squeeze().transpose())
        self._velocity = (self._velocity / self._total_mass).flatten()

    def run(self) -> None:
        """
        碰撞计数
        """
        counter = 0
        while not (0 >= self._velocity[0] >= self._velocity[1]):
            # 只要左侧物体不是静止或向右运动，且左侧物体追不上右侧物体
            # 那么它们还有发生弹性碰撞的可能
            self._collide_together()
            counter += 1
            print(f"第{counter}次碰撞，左侧物体速度为 {self._velocity[0]}m/s ，右侧物体速度为 {self._velocity[1]}m/s")
            if self._velocity[0] > 0:
                # 左侧物体有向墙的速度，必然发生碰撞
                self._velocity[0] = -self._velocity[0]
                counter += 1
                print(f"第{counter}次碰撞，左侧物体速度为 {self._velocity[0]}m/s ，右侧物体速度为 {self._velocity[1]}m/s")
        print(f"累计发生{counter}次碰撞")

    pass


if __name__ == "__main__":
    if len(argv) != 3:
        print("用法：python3 collisions.py <静止物体质量> <运动物体质量>")
        raise SyntaxError("命令行参数个数不符")
    if not match(FLOAT_FORMAT, argv[1]):
        raise ValueError("静止物体质量无法作为浮点数解析！")
    if not match(FLOAT_FORMAT, argv[2]):
        raise ValueError("运动物体质量无法作为浮点数解析！")
    engine = Engine(*map(float, argv[1:]))
    engine.run()
