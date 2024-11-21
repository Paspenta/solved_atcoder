# 002 Encyclopedia of Parentheses

## 問題
長さNの正しい括弧列を辞書順に出力  
( < )  
出力は"(",”)"のみ  
1 <= N <= 20  

## 括弧列の成立条件
- ()の数はそれぞれN/2
- 1行のある時点での)の数が(の数を超えない

## MEMO
まず(を全ていれる。そして残った)を出力する。
そして(を1ずつずらしていく。