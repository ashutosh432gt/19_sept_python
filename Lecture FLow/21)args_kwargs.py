"""
 *args : arguments
 **kwargs : key with arguments
 
 
 args : tuple as a parameter
 kwargs : dictionary as a parameter
    """
#example 1 argument (args)
    
'''def myfun(*a):
     print(a)
     
myfun(12,23,34,45,76,45)'''

#example 2 key with arguments (**kwargs)

def mydict(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} = {v}")
        
mydict(name="AAA",subjects="Python")        
     