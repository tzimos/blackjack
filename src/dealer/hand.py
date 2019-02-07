from src.base import BaseHand


class DealerHand(BaseHand):
    pass


    def dealer_has(self):
        return 'Dealer has: \r\n' + self.show_hand()

    def must_continue(self):
        minimun = min(self.evaluate_hand())
        if minimun <= 16:
            return True
        return False
