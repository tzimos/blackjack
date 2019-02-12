from src.base import BaseHand


class DealerHand(BaseHand):
    
    def dealer_has(self):
        return 'Dealer has: \r\n' + self.show_hand()
