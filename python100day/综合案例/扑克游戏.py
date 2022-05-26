import random


class Card(object):
    """一张牌"""

    def __init__(self, suite, face) -> None:
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self) -> str:
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)

    def __repr__(self):
        return self.__str__()


class Poker(object):
    """一副牌"""

    def __init__(self) -> None:
        self._cards = [Card(suite, face) for suite in '♠♥♣♦' for face in range(1, 14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌（税基乱序）"""
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌"""
        return self._current < len(self._cards)


class Player(object):
    """玩家"""

    def __init__(self, name) -> None:
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name
    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self):
        """摸牌"""
        self._cards_on_hand.append(Card)

    def arrange(self, card_key):
        """玩家整理手上的牌"""
        self._cards_on_hand.sort(key=card_key)


#  排序规则-先根据花色再根据点数排序
def get_key(card):
    return card.suite, card.face


def main():
    p = Poker()
    p.shuffle()
    players = [Player('刘亚龙'), Player('李鸣'), Player('赵恒哲'), Player('比少卿')]
    for _ in range(13):
        for player in players:
            player.get()
    for player in players:
        print(player.name + ':', end=' ')
        player.arrange(get_key)
        print(player.cards_on_hand)


if __name__ == '__main__':
    main()
