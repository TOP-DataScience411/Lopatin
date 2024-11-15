def countable_nouns(number,words = tuple[str, str, str]):
    if not isinstance(number,int):
        return None

    i=2
    if number%10==1:i=0
    elif (10 <= number <= 20): i=2
    elif (number%10 in [2,3,4]):i=1

    return words[i]
