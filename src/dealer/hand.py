from src.base import BaseHand


class DealerHand(BaseHand):
    pass


    def dealer_has(self):
        return 'Dealer has: \r\n' + self.show_hand()
