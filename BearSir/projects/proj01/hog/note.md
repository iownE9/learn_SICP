英语基础太差 读懂题用了好久 

run_experiments 和 Optional: Problem 12 需要继续写
主因是 题意理解不透彻 没体会到项目的趣味性

>>> # Ensure that say is properly updated within the body of play.
>>> def total(s0, s1):
...     print(s0 + s1)
...     return echo
>>> def echo(s0, s1):
...     print(s0, s1)
...     return total
>>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=echo)
(line 1)? 2 0
(line 2)? 7
(line 3)? 4 5
(line 4)? 4 10
-- Not quite. Try again! --

(line 1)? 14
-- Not quite. Try again! --

(line 1)? 2 0
(line 2)? 7
(line 3)? 4 5
(line 4)? 14        之前是凑巧了 艹
(line 5)? 6 10
-- Not quite. Try again! --

(line 1)? 2 0
(line 2)? 7
(line 3)? 4 5
(line 4)? 14
(line 5)? 4 10
-- Not quite. Try again! --

(line 1)? 2 0
(line 2)? 7
(line 3)? 4 5
(line 4)? 14
(line 5)? 9 7
(line 6)? 21
-- OK! --


 # 不便于问题六
    # def player(strategy, player_score, opponent_score) :
    #     while  player_score < goal :
    #         player_score += take_turn(strategy(player_score, opponent_score), opponent_score, dice)
    #         if extra_turn(player_score, opponent_score) :
    #             continue
    #         else :
    #             break
    #     return player_score

    # while score0 < goal and score1 < goal :
    #     if who == 0 :
    #         score0 = player(strategy0, score0, score1) 
    #     else :
    #         score1 = player(strategy1, score1, score0) 
    #     who = other(who)

# NO.8 求评价 参数为 每次筛子个数 和 摇多少次