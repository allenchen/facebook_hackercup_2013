import collections
import string

input = open("beautiful_strings.in", "r")

for index, line in enumerate(input.readlines()[1:]):
    index = index + 1
    sanitized_line = filter(lambda s: s in string.lowercase,
                            map(lambda l: l.lower(), line))
    frequencies = collections.Counter(sanitized_line)
    current_value = 26
    score = 0
    for letter, count in frequencies.most_common():
        score += current_value * count
        current_value -= 1
    print "Case #" + str(index) + ": " + str(score)
