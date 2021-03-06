#Author: c3nsored   

class ZitCard:
    """ An internet card """
    def __init__(self, bank, acnt, limit, customer):
        """ Create a new Zit card instance. The initial balance is 0"""
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._customer = customer
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._bank

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance
    
    def charge(self, price):
        """ Charge given price to the card, assuming sufficient balance """
        if price + self._balance > self._limit: # if charge would exceed limit
            return False                        # Cannot accept payment
        else:
            self._balance += price 
            return True

    def make_payment(self, amount):
        self._balance -= amount


class PredatoryCreditCard(ZitCard):
    def __init__(self, bank, acnt, limit, customer, apr):
        """ Create a new predatory credit card instance 
            
            customer: name of customer 
            bank: name of the bank 
            limit: credit limit (int)
            acnt: account number (String)
            apr: Annual precentage rate (float)
        """
        super().__init__(bank, acnt, limit, customer) # call super class constructor
        self._apr = apr 

    def charge(self, price):
        """Charge a price to the card assuming sufficient credit limit """
        # Return true if charge is processed
        # Return false and assess a 5$ fee if charge is denied 
        success = super().charge(price)
        if not success:
            # Charge 5$
            self._balance += 5 
        return success
    
    def process_month(self):
        """Assess monthly interset on outstanding balance """
        if self._balance > 0:
            # if positive balance, convert APD to monthly multiplicative factor 
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
    


if __name__ == "__main__":
    """ Run tests """
    cc = ZitCard('1st Bank', '5391 0375 9387 5309', 1000, "John Doe")
    wallet = []
    wallet.append(ZitCard('1st Bank,', '5391 0375 9387 5309', 1000, "John Doe"))
    wallet.append(ZitCard('1st Bank,', '5391 0375 9387 6309', 1000, "John lam"))
    wallet.append(ZitCard('1st Bank,', '5391 0375 9387 7309', 1000, "Richard lam"))
    
    print(len(wallet))
    # if cc:
    #     print('True')
    # print(len(cc)) # Will return type error 
    

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
    
    for c in range(len(wallet)):
        print('Customer = ', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
        print()
