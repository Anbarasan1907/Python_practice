#Variables are container to store the value .
num=10
#num is the variable name which holds the value 10 .
print("Variable scope")
#LOCAL VARIABLE
def order():
    delivery='swiggy'
    print(f"I drive {delivery}")
order()

#ENCLOSING

def order():
    delivery='swiggy'
    def time():
        in_time='eve'
        print(f"I drive {delivery} in {in_time}")
    time()
order()

#GLOBAL
delivery='zomato'
def job():
    time='noon'
    def vechicle():
        name='access125'
        print(f"I drive {delivery} in {name} scooty in {time}")
    vechicle()
job()