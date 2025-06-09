class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        five = 0
        ten = 0

        for b in bills:
            if b ==5:
                five+=1
            elif b ==10:
                if five == 0:
                        return False  # 没5块找他
                five -= 1
                ten += 1
            else:
                if five>0 and ten>0:
                     five -=1 
                     ten -=1
                elif five >=3:
                    five-=3
                else:
                    return False
            
        return True

            
