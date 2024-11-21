N = int(input())

# 長さが奇数であれば正しい括弧列は存在しない
if N % 2 != 0:
    exit()

def gen_parentheses(output, rest_left, rest_right):
    """_summary_
    括弧列を辞書順で出力する再帰関数

    Parameters
    ----------
    output : str
        出力する文字列
    rest_left : int
        (の残り数
    rest_right : int
        現時点で挿入可能な)の数
    """
    # 全て入れ終わったら出力
    if rest_left == rest_right == 0:
        print(output)
        return
    # (を入れる
    if rest_left > 0:
        gen_parentheses(output+"(", rest_left-1, rest_right+1)
    # )を入れる
    if rest_right > 0:
        gen_parentheses(output+")", rest_left, rest_right-1)


# 再帰関数を実行
gen_parentheses("", N//2, 0)
