# 8 三人斗地主手牌生成
import random
import time

cardSuit = ('Diamond', 'Club', 'Heart', 'Spade')
cardNum = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

def createCards():
    cardlist = []
    for suit in cardSuit:
        for num in cardNum:
            cardlist.append((suit, num))
    cardlist.append(('Red', 'Joker'))
    cardlist.append(('Black', 'Joker'))

    return cardlist

def dispatchCards(cards):
    random.shuffle(cards)
    player1Cards = []
    player2Cards = []
    player3Cards = []
    coverCardsNum = 3
    for index in range(0, len(cards) - coverCardsNum):
        cardPair = cards[index]
        if index % 3 == 0:  # 玩家1
            player1Cards.append(cardPair)
            print()  # 输出换行
        elif index % 3 == 1:  # 玩家2
            player2Cards.append(cardPair)
        else:  # 玩家3
            player3Cards.append(cardPair)
        print(' '.join(cardPair), '\t\t',)  # 输出当前发出的牌，模拟发牌效果
        time.sleep(0.5)
    print('\n')

    print(u"玩家1 手牌:", len(player1Cards))
    for cardPair in player1Cards:
        print(' '.join(cardPair))
    print()

    print(u"玩家2 手牌:", len(player2Cards))
    for cardPair in player2Cards:
        print(' '.join(cardPair))
    print()

    print(u"玩家3 手牌:", len(player3Cards))
    for cardPair in player3Cards:
        print(' '.join(cardPair))
    print()

    print(u"底牌:")
    rest_cards = cards[-3:]  # 剩余3张底牌
    for card in rest_cards:
        print(' '.join(card))


cards = createCards()
dispatchCards(cards)
