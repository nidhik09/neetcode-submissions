class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        leng = len(arr) 
        for i in range(leng -1):
            best = arr[i+1]
            for k in range(i+1, leng):
                if arr[k] > best:
                    best = arr[k]
            arr[i] = best
        arr[leng -1] = -1
        return arr
               


        