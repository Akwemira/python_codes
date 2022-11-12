# d is a dictionary that holds 2 lists (employees and owners). 
# Each of these lists holds multiple dictionaries
# my code will print out the last name of the second employee

d = { "employee" : [{"firstName" : "John", "lastName" : "Doe"},
                    {"firstName" : "Anna", "lastName" : "Smith"},
                    {"firstName" : "Peter", "lastName" : "Jones"}],
    "owners" : [{"firstName" : "Jack", "lastName" : "Petter"},
                {"firstName" : "Jessy", "lastName" : "Petter"}]}

second_employee_lastName = d["employee"][1]["lastName"] # new variable holds last name
print(f"The last name of the second employee is {second_employee_lastName}")

