class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1,n+1):
            strAnswer = ""
            if i%3 == 0: strAnswer += "Fizz"
            if i%5 == 0: strAnswer += "Buzz"
            if strAnswer == "": strAnswer = str(i)
            answer.append(strAnswer)

        return answer