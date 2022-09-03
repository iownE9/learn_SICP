
05:

>>> first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
>>> autocorrect("wrod", ["word", "rod"], first_diff, 1)
'word'
>>> autocorrect("inside", ["idea", "inside"], first_diff, 0.5)
'inside'   # "inside" 在里面
>>> autocorrect("inside", ["idea", "insider"], first_diff, 0.5)
'idea'     # 使用重新赋值的first_diff    0 0
>>> autocorrect("outside", ["idea", "insider"], first_diff, 0.5)
'outside'  # 1 1