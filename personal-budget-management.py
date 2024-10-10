# Task 1: Define Budget Category Class Create a class `BudgetCategory` 
# with private attributes for category name and allocated budget. 
# - Initialize these attributes in the constructor.

# - Expected Outcome: A `BudgetCategory` class capable of storing category details securely.

# Task 2: Implement Getters and Setters - Write getter and setter methods for both the 
# category name and the allocated budget. - Ensure that the setter methods include validation 
# (e.g., budget should be a positive number).

# - Expected Outcome: Methods that allow controlled access and modification of the 
# private attributes, with validation checks in place.

# Task 3: Add Budget Functionality: Implement a method to add expenses to a category and 
# adjust the budget accordingly. - Validate the expense amount before making deductions 
# from the budget.

# - Expected Outcome: Ability to track expenses per category and update the remaining budget safely.

# Task 4: Display Budget Details: Create a method to display the details of a budget category, 
# including the name, allocated budget, and remaining budget after expenses.

# - Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.

class BudgetCategory: # Constructor and private attributes
    def __init__(self, category, budget):
        self.__category = category
        self.__budget = budget
    # Getters and setters for category name and budget
    def get__category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category

    def get_budget(self):
        return self.__budget

    def set_budget(self, budget):
        if isinstance(budget, (int)) and budget > 0:
            self.__budget = budget
        else:
            raise ValueError("Budget must be a positive number.")

    def add_expense(self, amount): # Method to add an expense to the category
        if 0 < amount < self.get_budget():
            self.set_budget(self.get_budget() - amount)
            print(f"Expense: {amount}")
        else:
            print('Insufficient balance.')
           
    def display_category_summary(self): # Method to display the budget category details
       print(f"Category: {self.__category}\n Budget: {self.__budget}") 
        

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.add_expense(50)
food_category.display_category_summary()