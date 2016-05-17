from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
new = Guitar("GG", 2010, 19000)
print(gibson)
print(gibson.get_age())
print(gibson.is_vintage())
print(new.get_age())
print(new.is_vintage())

