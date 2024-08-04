from OOPS.Item import Item
from OOPS.Phone import Phone

print(Item.is_integer(7.5))
Item.instantiate_from_csv("items.csv")
print(Item.store_list)

item1 = Item("Phone", 1000, 5)  # whenever you create an instance(object) of the class,
# the __init__ method of that class will be called by default.
item2 = Item("Laptop", 10000, 2)  # again __init__ will be called now

item1.company = "Lenovo"  # attributes other than the ones mentioned in the __init__ can also be created
#  The parameters which are compulsory have to me mentioned in __init__

item1.apply_discount()
print(item1.price)

item2.apply_discount()
print(item2.price)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
print(Item.__dict__)  # all the attributes for class level
print(item1.__dict__)  # all the attributes for instance level

print(Item.store_list)  # This list consists of all the values of all attributes for each object(instance).

for instance in Item.store_list:  # when you want to access particular attribute values from the list.
    print(instance.name)

phone1 = Phone("OnePlus", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("Apple", 700, 6, 2)

print(Item.store_list)
print(Phone.store_list)

print(item1.name)
# setting an attribute
item1.name = "OtherItem"
# getting an attribute
print(item1.name)

item1.apply_increment(0.2)
print(item1.price)
item1.send_email()
# To check Data-Type
print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))
