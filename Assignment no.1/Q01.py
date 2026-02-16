# Write a function using a while loop to print even numbers from 1 to 20.

def even_number():
    n=1
    while n<=20: # runing while loop for n<=20
        if n % 2 == 0: # to check the no. is even
            print(n)
        n+=1 # increase the no. by 1 for each iteration
even_number() # calling function tu run