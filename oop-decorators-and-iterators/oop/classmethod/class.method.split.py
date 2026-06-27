
""" 
“Class and static methods play well together. 
Static methods are actually quite helpful in breaking up the logic of a class method to improve its layout.”
"""


class StringUtil:
    
    @classmethod
    def is_palindrome(cls, s,case_insensitive = True):
        
        s = cls._strip_string(s) 
        
        if case_insensitive:
            s= s.lower()
        return cls._is_palindrome(s)
            
    @staticmethod
    def _strip_string(s):
        return ' '.join(c for c in s if c.isalnum()) 
            
    @staticmethod
    def _is_palindrome(s):
        for c in range(len(s) // 2 ):
            if s[c] != s[-c-1]:
                return False
        return True
  
    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())

print(StringUtil.is_palindrome('Radar',case_insensitive=False)) # False: Case Sensitive
print(StringUtil.is_palindrome('A nut for a jar of tuna”')) 
print(StringUtil.is_palindrome('Never Odd, Or Even!'))
print(StringUtil.is_palindrome('In Girum Imus Nocte Et Consumimur Igni'))
print(StringUtil.get_unique_words('I love palindromes. I really really love them!'))

"""
output: 

False
True
True
True
{'really', 'love', 'I', 'palindromes.', 'them!'}
"""