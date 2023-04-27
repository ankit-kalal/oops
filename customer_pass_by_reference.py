class Customer():

    def __init__(self,name):
        self.name = name



def greet(customer):

    print(id(customer))
    
    print(f"hello {customer.name} sir")

    return Customer("ankita")


cust = Customer("Ankit")

print(id(cust))

new_cust= greet(cust)

print(new_cust.name)