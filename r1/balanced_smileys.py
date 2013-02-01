input = open("balanced_smileys.in", "r")

def is_balanced(s, open_paren_count):
    #print str(open_paren_count) + " - " + s

    if len(s) == 0:
        if open_paren_count == 0:
            return True
        else:
            return False
    if len(s) == 1:
        if (s not in ("(", ")") and open_paren_count == 0) or (open_paren_count == 1 and s == ')') or (open_paren_count == 0 and s == ':'):
            return True
        else:
            return False

    candidates = []
    if s[0] == ")":
        if open_paren_count > 0:
            candidates += [(s[1:], open_paren_count - 1)]
        else:
            return False

    if s[0] == ":":
        if s[1] == ")" or s[1] == "(":
            candidates += [(s[2:], open_paren_count)]
        candidates += [(s[1:], open_paren_count)]

    if s[0] not in (":", "(", ")"):
        candidates += [(s[1:], open_paren_count)]

    if s[0] == "(":
        candidates += [(s[1:], open_paren_count + 1)]

    #print candidates

    return any(map(lambda x: is_balanced(x[0], x[1]), candidates))


for index, line in enumerate(input.readlines()[1:]):
    index = index + 1
    print "Case #" + str(index) + ": " + ("YES" if is_balanced(line, 0) else "NO")
