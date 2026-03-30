class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                total = 1
            else:
                total = 0
        else:
            for i in range(0,len(flowerbed)):
                if i == 0:
                    if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        total = total+1
                        flowerbed[i] = 1

                elif i == len(flowerbed)-1:
                    if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                        total = total+1
                        flowerbed[i] = 1

                else:
                    if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                        total = total+1
                        flowerbed[i] = 1


        if n > total:
            return False
        else:                
            return True
        