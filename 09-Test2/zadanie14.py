def f(arr):
    valid = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","_"]
    value = 0
    for username in arr:
        counter = 0
        for char in username:
            if char in valid:
                counter += 1
            elif char not in valid:
                counter = 0
                break
        if counter >= 4 and counter <= 12:
            value += 1
    return value

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))