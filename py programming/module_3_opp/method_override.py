class master:

    def header(self,home,about,contact):
        print("Home:",home)
        print("About:",about)
        print("Contact:",contact)

class index(master):

    def header(self,home,about,contact):
        return super().header(home,about,contact)
    
class profile(master):

    def header(self,home,about,contact):
        return super().header(home,about,contact)    
    
ind=index()
ind.header("H","A","C")

pro=profile()
pro.header("H","A","C")

# same method and also same number of arguments but different class

# super() function is used to give access to the methods of a parent class from a child class.