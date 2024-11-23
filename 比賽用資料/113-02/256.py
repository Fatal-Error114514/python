from collections import Counter

def best(lst):
    card_count = Counter(lst)
    count = sorted(card_count.values(), reverse = True)
    cards = sorted(card_count.keys())
    for i in range(len(cards) - 4):
        if cards[i + 4] - cards[i] == 4:
            return 1
    if 3 in count and 2 in count:
        return 2
    
    if count.count(2) == 2 or count[0] == 4:
        return 3
    if count[0] == 2:
        return 4
    
    return 5

lst = list(map(int,input().rstrip().lstrip().replace('A', '1').replace('J', '11').replace('Q', '12').replace('K', '13').split(',')))
print(best(lst))