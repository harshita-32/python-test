class Father:
    def property(self):
        print("Father's method: proprety()")
    def business(self):
        print("Father's method: businee()")
class Son(Father):
    def study(self):
        print("Son's method: study()")
class Daughter(Father):
    def dance(self):
        print("Daughter's method: dance()")
class Grandchild(Son,Daughter):
    def gaming(self):
        print("Grandchild's method: gaming()")

obj = Grandchild()
print("--- calling all methodds from Grandchild object ---")
obj.property()
obj.business()
obj.study()
obj.dance()
obj.gaming()
