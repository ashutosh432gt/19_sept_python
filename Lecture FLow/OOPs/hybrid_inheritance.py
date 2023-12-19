"""
                                RBI
            ---------------------------------------
            |                   |                 |
            |                   |                 |
            V                   V                 V
           SBI                 BOI               HDFC   
    
    """
class RBI:
    def intro(self):
        print("Welcome To banking Sector")
       
class SBI(RBI):
    def intro(self):
        print("6.5")
        
class BOI(RBI):
    def intro(self):
        print("5.5")
        
class HDFC(RBI):
    def intro(self):
        print("7.5")
        
sbi = SBI()
hdfc = HDFC()
boi = BOI()

sbi.intro()
sbi.ROI()

hdfc.intro()
hdfc.ROI

boi.intro()
boi.ROI()        
        
            