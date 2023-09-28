print("The temperature in the room is 25 degree celsius")
temp_cel= 25
print(f"The room temperature is {temp_cel} degree celsius")
word = "temperature"
can_form = word.capitalize()
print(f"The canonical form of '{word}' is '{can_form}'")
temp_in_cel = 25
temp_in_fah = (temp_in_cel * 9/5 + 32)
print(temp_in_fah)
def analyze_temp(temp):
    if temp<0:
        return "it is freezy"
    elif 0<=temp<20:
        return "it is cool"
    else:
        return "worm"
analy = analyze_temp(temp_in_cel)
print(f"The temperature of {temp_in_cel} degree celsius:{analy}")
