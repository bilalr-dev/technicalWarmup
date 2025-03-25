def sortCards(cards):
    temp = 0
    for i in range(6):
        for j in range(6-i):
            if cards[j] > cards[j+1]:
                temp = cards[j]
                cards[j] = cards[j+1]
                cards[j+1] = temp
    return cards

cards = [7, 3, 5, 9, 11, 13, 6]
print("Original cards order : ")
for i in range(7):
    print(cards[i], end=" ")
print("\nCards sorted in ascending order : ")
cards = sortCards(cards)
for i in range(7):
    print(cards[i], end=" ")
