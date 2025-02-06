import math

def generate_sqrt_table(start=0.0, end=5.0, step=0.1):
    latex = []
    # 表格头部
    latex.append(r'''\begin{table}[ht]
    \centering
    \resizebox{\linewidth}{!}{%
    \begin{tabular}{|c|cccccccccc|ccccccccc|}
        \hline
        N   & 0     & 1     & 2     & 3     & 4     & 5     & 6     & 7     & 8     & 9     & 1     & 2     & 3     & 4     & 5     & 6     & 7     & 8     & 9 \\
        \hline''')

    current = start
    while current <= end:
        row = [f"{current:.1f}"]
        # 计算前10列
        for i in range(10):
            num = current + i * 0.01
            sqrt_val = math.sqrt(num)
            row.append(f"{sqrt_val:.3f}")
        
        # 正确计算后的修正值部分
        corrections = []
        for d in range(1, 10):  # 处理千分位修正
            num = current + d * 0.001
            delta = math.sqrt(num) - math.sqrt(current)
            corrections.append(f"{int(round(delta * 1000))}")
        
        row_str = " & ".join(row + corrections)
        latex.append(f"        {row_str} \\\\")

        current = round(current + step, 1)

    latex.append(r'''        \hline
    \end{tabular}%
    }
\end{table}''')
    return "\n".join(latex)

print(generate_sqrt_table(start=0.0, end=9.9))
