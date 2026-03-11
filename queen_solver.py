def solve_n_queens(n: int = 8) -> list[list[str]]:
    """
    求解n皇后问题，返回所有合法解
    
    Args:
        n: 皇后数量，默认为8
    
    Returns:
        所有合法解的列表，每个解为二维字符串列表
    
    Raises:
        ValueError: 当n < 1时
    """
    if n < 1:
        raise ValueError("n必须大于等于1")
    
    # 存储所有解
    solutions = []
    # 存储当前皇后的位置，索引为行号，值为列号
    queens = []
    
    def is_safe(row, col):
        """
        检查在(row, col)位置放置皇后是否安全
        
        Args:
            row: 当前行
            col: 当前列
        
        Returns:
            bool: 是否安全
        """
        for r, c in enumerate(queens):
            # 检查列冲突
            if c == col:
                return False
            # 检查对角线冲突
            if abs(r - row) == abs(c - col):
                return False
        return True
    
    def backtrack(row):
        """
        回溯算法求解n皇后问题
        
        Args:
            row: 当前处理的行
        """
        # 所有行都处理完毕，找到一个解
        if row == n:
            # 生成解的格式
            solution = []
            for col in queens:
                row_str = ['.'] * n
                row_str[col] = 'Q'
                solution.append(''.join(row_str))
            solutions.append(solution)
            return
        
        # 尝试在当前行的每一列放置皇后
        for col in range(n):
            if is_safe(row, col):
                # 放置皇后
                queens.append(col)
                # 处理下一行
                backtrack(row + 1)
                # 回溯，移除皇后
                queens.pop()
    
    # 从第0行开始回溯
    backtrack(0)
    return solutions


if __name__ == "__main__":
    # 演示n=8的情况
    n = 8
    solutions = solve_n_queens(n)
    print(f"n={n}时，共找到{len(solutions)}个解")
    
    # 打印前3个解作为示例
    print("\n前3个解示例：")
    for i, solution in enumerate(solutions[:3]):
        print(f"\n解 {i+1}:")
        for row in solution:
            print(row)