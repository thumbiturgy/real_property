import math
class ROI_estimate:

    def core_ui(self):
        while True:
            response = input("\nTo calculate your estimated ROI using detailed income and expense information, say 'new'. If you've already got your total income and expenses figured out and just want a quick ROI estimate, say 'quick'! If you're finished, say 'quit'.\n(new/quick/quit?)\n")
            if response == 'quit':
                print("\nThank you for visiting! See you next time!")
                break
            if response == 'new':
                self.create_property_profile()
            elif response == 'quick':
                print(self.quick_roi())
            else:
                self.invalid_entry()

    
    # simple input error check
    def invalid_entry(self):
        print("\nPlease enter a valid response.\n")

    # formatting numerical user entry for calculation purposes, filtering out commas and rounding to nearest whole dollar
    def format_number_entry(self, num_entry, decimal = 0):
        multiplier = 10 ** decimal
        num_entry.replace(',', '')
        try:
            formatted_num = int(num_entry)
        except:
            formatted_num = math.ceil((float(num_entry)*multiplier)/multiplier)
        return formatted_num



# the quick and dirty, bring your own figures ROI; slightly faster than the calculator on your phone
    def quick_roi(self):
        income_per_month = input("\nTotal monthly income?\n")
        expenses_per_month = input("\nTotal monthly expenses?\n")
        if not income_per_month.isdigit() or not expenses_per_month.isdigit():
            self.invalid_entry()
            self.quick_roi()
        else:
            income_per_month = self.format_number_entry(income_per_month)
            expenses_per_month = self.format_number_entry(expenses_per_month)
            monthly_cashflow = income_per_month - expenses_per_month
            initial_investment = input("\nTotal up-front costs including cash down, closing costs, rehab, etc?\n")
            if initial_investment.isdigit():
                return f"\nBased on these numbers, your estimated ROI is {self.format_number_entry((monthly_cashflow*12)/initial_investment, 2)}%."


            



# housing for other functions to run in sequence with error checks along the way, initializes dict to retain gathered info for later review
    def create_property_profile(self):
        self.new_property = {
            'income': {},
            'expenses': {
                'mortgage': None,
                'taxes': None,
                'repairs': None,
                'capital expenditures': None,
                'total expenses': 0
            },
            'property_info': {}
            }
        self.get_income()
        self.get_expenses()
        self.get_initial_investment()

    
       

    def get_income(self):
        while not self.new_property['income']:
            entered_rent = input("\nRent should be your largest source of income, so let's start there. How much will you receive for rent each month?\n")
            if entered_rent.isdigit() > 0:
                self.new_property['income']['rent'] = self.format_number_entry(entered_rent)
                self.new_property['income']['total income'] = self.format_number_entry(entered_rent)
            else:
                self.invalid_entry()
                self.get_income()
        while True:
            print("\n----Monthly Income----\n")
            for k, v in self.new_property.items():
                print(f"\n{k.title()}\t\t{v}")
            more_income = input("\nWill you receive any additional income from this property? ('yes'/'no')\n")
            if more_income == 'no':
                break
            elif more_income == 'yes':
                income_source = input("\nWhat is the source of additional income?\n")
                income_amount = input(f"\nHow much income will {income_source} supply each month?\n")
                if income_amount.isdigit() > 0:
                    self.new_property['income'][income_source] = self.format_number_entry(income_amount)
                    self.new_property['income']['total income'] += self.format_number_entry(income_amount)
                else:
                    self.invalid_entry()

    
    def get_expenses(self):
        while True:
            print("\n---- Monthly Expenses----\n")
            for k in self.new_property['expenses']:
                get_expense = (f"\nHow much will you pay monthly for {k.title()}?\n")
                if get_expense.isdigit() > 0:
                    self.new_property['expenses'][k] = self.format_number_entry(get_expense)
                    self.new_property['expenses']['total expenses'] += self.new_property['expenses'][k]
                else:
                    self.invalid_entry()

                


                
                
# calculate roi based on monthly income and expenses
# minimize user input required
# perform calculations "behind the scenes" while allowing user to see as much detail as they wish
# identify and remove/remedy pain points
