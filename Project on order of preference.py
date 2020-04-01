class Project:
    print 'our project is order of preference'
    while True:
        
        choice=input("enter the choice:")
        if choice==1:
            def fibo(n):
                print "fibo using looping for statement"
                a,b=0,1
                print a
                print b
                for i in range(2,n):
                    c=a+b
                    a=b
                    b=c
                    print c
            fibo(5) 
        elif choice==2:
            print "fibo using looping while statement"
            a,b=0,1
            while(b<100):
                print a
                a,b=b,a+b
        elif choice==3:
            print 'fibo using decision making statement' 
            def fibonacci(n):
                if n==1 or n==2:
                    return 1
                return fibonacci(n-1) + fibonacci(n-2)
        elif choice==4:
            print 'fibo using lambda'
            fib=lambda n:reduce(lambda a,b:a+[a[-1]+a[-2]],range(n-2),[0,1])
            print fib(10)
        elif choice==5:
            num = 7
            factorial = 1
            for i in range(1,num + 1):
                factorial = factorial*i
                print("The factorial of",num,"is",factorial)
        elif choice==6:
            class fib:
                def __init__(self,a,b):
                    self.a=a
                    self.b=b
                def fibb(self):
                    while(self.b<100):
                        class fibbb(fib):
                            def __init__(self,a,b,c):
                                fib.__init__(self,a,b)
                                self.c=c
            class fibo(fib):
                def __init__(self,a,b,c):
                    def volume(self):
                        self.c=self.a+self.b
                        self.a=self.b
                        self.b=self.c
                        return self.c
                b1=fibbb(0,1)
                b2=fibo(0,1)
                print b1.fibb()
                print b2.volume()
            
            
                

        
			
