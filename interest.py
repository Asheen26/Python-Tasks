class Bank:
    def __init__(self, bank_name, base_rate):
        self.bank_name = bank_name
        self.base_rate = base_rate 
    
    def calculate_interest(self, principal, years):
        return (principal * self.base_rate * years) / 100


class Customer(Bank):
    def __init__(self, name, bank_name, base_rate, loan_amount, loan_term):
        super().__init__(bank_name, base_rate)
        self.name = name
        self.loan_amount = loan_amount
        self.loan_term = loan_term 

    def get_interest_rate(self):
        return self.calculate_interest(self.loan_amount, self.loan_term)

    def display_details(self):
        interest = self.get_interest_rate()
        print(f"Customer Name: {self.name}")
        print(f"Bank: {self.bank_name}")
        print(f"Loan Amount: {self.loan_amount}")
        print(f"Loan Term: {self.loan_term} years")
        print(f"Base Interest Rate: {self.base_rate}%")
        print(f"Total Interest to be Paid: {interest:.2f}")



customer = Customer("Vini", " State Bank of India", 5.0, 10000, 3)
customer.display_details()
