class Solution:
  def countPrimes(self, n: int) -> int:

    def getPrime(n):
      primes = [True] * n
      m = int(n ** 0.5)
      for i in range(2, m+1):
          if primes[i] == True:
              for j in range(i+i, n, i):
                  primes[j] = False
      return [i for i in range(2,n) if primes[i] == True]

    primeListn = getPrime(n)
    return len(primeListn)