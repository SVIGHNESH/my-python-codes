celsius = [33,32,38,24]
fahrenheit = [x*9/5 +32 for x in celsius]
# fahrenheit = list(map(lambda x : x*9/5 +32 ,celsius))
print(fahrenheit)