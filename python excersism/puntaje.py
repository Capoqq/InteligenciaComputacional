def ultimo(scores):
    return scores[-1]


def mejor_personal(scores):
    return max(scores)


def top_tres(scores):
    list.sort(scores,reverse=True)
    return scores[0:3]