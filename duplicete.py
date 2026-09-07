class Solution:
    def isPalindrome(self, x: int) -> bool:

      x_str = str(x)
      numero_2 = x_str[::-1]
      resultado = x_str == numero_2
      return resultado


