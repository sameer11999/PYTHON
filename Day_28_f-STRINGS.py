letter = "Hey my name is {} and Iam from {}"
country = "India"
name = "Sameer"

print(letter.format(name, country))

letter = "Hey my name is {0} and Iam from {1}"
country = "India"
name = "Sameer"

print(letter.format(name, country))

letter = "Hey my name is {0} and Iam from {1}"
country = "India"
name = "Sameer"

print(letter.format(name, country))
print(f"Hey my name is {name} and Iam from {country}")


price = 49.007382
txt = f"For only {price:.2f} dollors"
print(txt)