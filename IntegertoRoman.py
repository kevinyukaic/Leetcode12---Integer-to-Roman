#Method 1: transfer to string to handle
class Solution:
    def intToRoman(self, num: int) -> str:
        #Guaranteed to be within the range of 1 to 3999
        #no need to perform edge check here
        
        
        Result = ""
        Roman_Digit = {1:"I",2:"V",3:"X",4:"L",5:"C",6:"D",7:"M"}
        RomanP = 1
        num = str(num)
        while(num != ""):
            cur = num[-1]
            #Case: 4 or 9
            if(cur == "4"):
                Result = Roman_Digit[RomanP] + Roman_Digit[RomanP+1] + Result
            elif(cur == "9"):
                Result = Roman_Digit[RomanP] + Roman_Digit[RomanP+2] + Result
            #Case: others
            else:
                if(int(cur)>=5):
                    Result = Roman_Digit[RomanP+1] + Roman_Digit[RomanP] * (int(cur) - 5) + Result
                else:
                    Result = Roman_Digit[RomanP] * int(cur) + Result
                
            num = num[:-1]
            RomanP+=2
            
        return Result

        
#Method 2: Pure int solution (Faster)
class Solution:
    def intToRoman(self, num: int) -> str:
        #Guaranteed to be within the range of 1 to 3999
        #no need to perform edge check here
        
        Result = ""
        Roman_Digit = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        RomanP = 1
        #num = str(num)
        while(num):
            num, remainder = divmod(num,10)
            
            #Case: 4 or 9
            if(remainder == 4):
                Result = Roman_Digit[RomanP] + Roman_Digit[RomanP*5] + Result
            elif(remainder == 9):
                Result = Roman_Digit[RomanP] + Roman_Digit[RomanP*10] + Result
            #Case: others
            else:
                if(remainder>=5):
                    Result = Roman_Digit[RomanP*5] + Roman_Digit[RomanP] * (remainder - 5) + Result
                else:
                    Result = Roman_Digit[RomanP] * remainder + Result                
            
            RomanP*=10
            
        return Result
        
        