"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime

###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    # 第 k 个满足select为True的段落,而不是第 k 段是否满足select为True
    "*** YOUR CODE HERE ***"
    for p in paragraphs:
        if select(p):
            k -= 1
            if k < 0:
                return p
    return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"

    def select(p):
        p = remove_punctuation(p)
        words = lower(p).split()

        for word in words:
            # for t in topic:
            #     if word == t:
            #         return True

            # BearSir's
            if word in topic:
                return True

        return False

    return select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BearSir’s
    # zip() 往短的截取
    # BEGIN PROBLEM 3
    count = 0
    for typed_word, reference_word in zip(typed_words, reference_words):
        if typed_word == reference_word:
            count += 1
    return 100 * count / len(typed_words) if typed_words else 0.0
    "*** YOUR CODE HERE ***"
    # typed_len, reference_len = len(typed_words), len(reference_words)
    # length_min = min(typed_len, reference_len)
    # i, n = 0, 0

    # while i < length_min:
    #     if typed_words[i] == reference_words[i]:
    #         n += 1
    #     i += 1

    # return n / typed_len * 100 if typed_len != 0 else 0.0
    # END PROBLEM 3


# >>> accuracy(" a b \tc" , "a b c") # Tabs don't count as words
# ? 66.7
# -- Not quite. Try again! --
# ? 100.0


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed) / 5 * 60 / elapsed
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # if user_word in valid_words:
    #     return user_word

    # # lowest 初始值设置有问题
    # lowest, res = len(user_word), ""
    # for word in valid_words:
    #     # diff = diff_function(word, user_word, limit) # Error 顺序
    #     diff = diff_function(user_word, word, limit)
    #     if diff < lowest:
    #         lowest, res = diff, word
    # if lowest <= limit:  #  greater than limit 等于的情况也是要返回的
    #     return res

    # return user_word
    # END PROBLEM 5

    # BearSir's
    # min() 返回 第一个 条件最小值
    if user_word in valid_words:
        return user_word
    cloest_word = min(
        valid_words,
        key=lambda valid_word: diff_function(user_word, valid_word, limit))
    if diff_function(user_word, cloest_word, limit) > limit:
        return user_word
    return cloest_word


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line'
    len_start, len_goal = len(start), len(goal)
    dif, len_min = abs(len_start - len_goal), min(len_start, len_goal)

    # 先普通后recursion
    # i, n = 0, 0
    # while i < len_min and n <= limit:
    #     if start[i] != goal[i]:
    #         n += 1
    #     i += 1

    def recursion(i, n):
        if not (i < len_min and n <= limit):
            return n

        if start[i] != goal[i]:
            return recursion(i + 1, n + 1)
        return recursion(i + 1, n)

    return dif + recursion(0, 0)

    # END PROBLEM 6

    # BearSir 的做法是切片 自调用 perfect
    # shifty_shifts(start[1:], goal[1:], limit)


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # assert False, 'Remove this line'
    # 2nd 思想就是遍历 求最小
    if not start or not goal:  # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        # return abs(len(start) - len(goal))
        return len(start) + len(goal)
        # END

    elif start[0] == goal[0]:  # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return pawssible_patches(start[1:], goal[1:], limit)
        # END

    else:
        add_diff = pawssible_patches(
            start, goal[1:], limit -
            1) if limit > 0 else 2  # Fill in these lines
        remove_diff = pawssible_patches(start[1:], goal, limit -
                                        1) if limit > 0 else 2
        substitute_diff = pawssible_patches(start[1:], goal[1:], limit -
                                            1) if limit > 0 else 2
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 1 + min(add_diff, remove_diff, substitute_diff)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    i, N = 0, len(typed)
    while i < N and typed[i] == prompt[i]:
        i += 1
    progress = i / len(prompt)
    send({'id': user_id, 'progress': progress})
    return progress

    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    for play in times_per_player:
        for i in range(len(play) - 1):
            play[i] = play[i + 1] - play[i]
        play.pop()
    return game(words, times_per_player)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(
        all_times(game)))  # contains an *index* for each player
    word_indices = range(len(
        all_words(game)))  # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    # 题意 对于每一个单词 谁打字最快
    # 2nd
    # 修补 用上面提示 替换自定义
    result = [[] for _ in player_indices]
    word_time = {}

    for word_index in word_indices:
        word = word_at(game, word_index)
        for player_num in player_indices:
            if player_num == 0 or time(game, player_num, word_index) < time(
                    game, word_time[word], word_index):
                word_time[word] = player_num

    for k, v in word_time.items():
        result[v].append(k)
    return result

    # 使用字典 多此一举
    # BearSir's better
    words = [[] for _ in player_indices]
    for word_index in word_indices:
        fastest_player = 0
        for player_num in player_indices:
            if time(game, player_num, word_index) < time(
                    game, fastest_player, word_index):
                fastest_player = player_num
        words[fastest_player].append(word_at(game, word_index))
    return words
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str
                for w in words]), 'words should be a list of strings'
    assert all([type(t) == list
                for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times
                for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words)
                for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print(
            'If you only type part of it, you will be scored only on that part.\n'
        )
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)