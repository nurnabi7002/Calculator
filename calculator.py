# Making a calculator

# instraction
print("""   This is a simple calculator softowre that's make 2 numbers math.
                Instraction -
                1. for sum  use "sum"
                2. for minus use "min"
                3. for multiply use "mul"
                4. for divide use "div"
                
                
""")

def sum(a, b):
	print("Your sum is",a + b) #sum code func
	
def min(a, b):
	print("Your minus is",a - b) #min code func
	
def mul(a, b):
	print("Your Multiple is",a*b) #mul code func
	
def div(a, b):
	print("Your division is",a//b) #div code func
	
t = input("    What you want : ") #want input

x = int(input("a : ")) #input of a
y = int(input("b : ")) #input of b

if t == "sum":
	sum(x, y) #sum func call
	
elif (t == "min"):
	min(x, y) #min func call

elif(t == "mul"):
	mul(x, y) #mul func call
	
elif(t == "div"):
	div(x, y) #div func call
	
else:
	print("use valid instractions") #else system