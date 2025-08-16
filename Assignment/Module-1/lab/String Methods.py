# String manipulation using methods
msg = "   hello python world   "

print("Original String:", msg)
print("Uppercase:", msg.upper())          
print("Lowercase:", msg.lower())          
print("Title Case:", msg.title())         
print("Stripped:", msg.strip())           
print("Replace 'python' with 'Java':", msg.replace("python", "Java"))
print("Check if starts with 'hello':", msg.strip().startswith("hello"))
print("Check if ends with 'world':", msg.strip().endswith("world"))
print("Split into words:", msg.split())   
print("Count 'o':", msg.count('o'))       
print("Find 'python':", msg.find("python"))  
