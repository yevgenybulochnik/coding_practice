from itertools import cycle

# Fails becuase it does not retain posiitoning of values. Each letter needs to
# be mapped one-to-one to another letter. This function only looks at unique
# mappings. Keeping this for now tho since its an interesting use of cycle.


def isIsomorphicFailed(s: str, t: str) -> bool:
    s_list = set(list(s))
    t_list = set(list(t))

    dict_s = dict(zip(s_list, cycle(t_list)))
    dict_t = dict(zip(t_list, cycle(s_list)))

    if list(dict_s.keys()) == list(dict_t.values()) and list(
        dict_t.keys()
    ) == list(dict_s.values()):
        return True

    return False


def isIsomorphic(s: str, t: str) -> bool:
    mapST, mapTS = {}, {}

    for c1, c2 in zip(s, t):

        if (c1 in mapST and mapST[c1] != c2) or (
            c2 in mapTS and mapTS[c2] != c1
        ):
            return False
        mapST[c1] = c2
        mapTS[c2] = c1

    return True


assert isIsomorphic("egg", "add") is True
assert isIsomorphic("foo", "bar") is False
assert isIsomorphic("paper", "title") is True
assert isIsomorphic("bbbaaaba", "aaabbbba") is False
