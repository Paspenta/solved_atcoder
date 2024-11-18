# N:羊羹の切れ目の数、length:羊羹の長さ
N, length = list(map(int, input().split()))
# 選ぶ切れ目の数
K = int(input())
# 切れ目のリスト
A = list(map(int, input().split()))


def can_cut(score):
    """_summary_

    一切れの最短サイズを指定し、K個以上に分割できるか検証する関数

    Parameters
    ----------
    score : int
        スコア、つまり最も短い一切れの長さ

    Returns
    -------
    bool
        スコアを一切れの最短として切った時、
            K回以上きれればTrue
            K回以上きれなければFalse
    """
    cut = 0 # カット回数
    last = 0 # 最後に切った位置
    for i in range(N):
        # 最後に切った位置から現在の切れ目までの長さがscore以上
        # and 一切れ分以上残っている
        if A[i] - last >= score and length - A[i] >= score:
            cut += 1 # カット回数をカウント
            last = A[i] # 最後の切った位置を更新
    return cut >= K

L = 0 # 最小探索範囲
R = length+1 # 最大探索範囲

# 二分探索
while L < R:
    mid = (L+R+1)//2

    if can_cut(mid):
        L = mid
    else:
        R = mid - 1

print(L)
