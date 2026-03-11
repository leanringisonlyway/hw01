# 八皇后问题求解器

## 工程功能
- 实现八皇后问题的求解算法，使用回溯法
- 支持n≥1的合法输入，n<1时抛出ValueError
- 返回所有合法解，格式为二维字符串列表

## 运行方式
1. 安装依赖：`pip install -r requirements.txt`
2. 运行测试：`pytest tests/test_queen_solver.py`
3. 执行求解器：
   ```python
   from src.queen_solver import solve_n_queens
   solutions = solve_n_queens(8)
   print(f"共找到{len(solutions)}个解")
   ```

## Bug说明
在步骤4中，我们故意在核心回溯逻辑中引入了一个逻辑Bug，导致n=4时解的数量错误。通过运行单元测试可以发现这个问题，然后进行修复。