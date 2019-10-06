# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").

    user_history = {}

    for site, user in zip(site_list, user_list):
        if user not in user_history:
            user_history[user] = set()

        user_history[user].add(site)

    affinities = {}
    for user, history in user_history.items():
        history = list(history)
        history.sort()
        for i, site1 in enumerate(history):
            for site2 in history[i+1:]:
                pair = (site1, site2)
                if pair not in affinities:
                    affinities[pair] = 0
                affinities[pair] += 1

    return max(affinities, key=affinities.get)


def func1(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 3
    elif a == 4:
        return 4
    else:
        return 5


def func2(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 3
    elif a == 4:
        return 4
    else:
        return 5

def func3(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 3
    elif a == 4:
        return 4
    else:
        return 5

def func4(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 3
    elif a == 4:
        return 4
    else:
        return 5

def func5(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 3
    elif a == 4:
        return 4
    else:
        return 5

def func6(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 3
    elif a == 4:
        return 4
    else:
        return 5

def func7(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 3
    elif a == 4:
        return 4
    else:
        return 5

def func8(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 3
    elif a == 4:
        return 4
    else:
        return 5