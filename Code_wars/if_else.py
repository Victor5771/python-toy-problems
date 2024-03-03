def check_alive(health):
    if health <= 0:  
        return False 
    else:
        return True 


# print:
print(check_alive(5))  
print(check_alive(-3)) 
