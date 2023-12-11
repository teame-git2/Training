def is_palindrome(text):
  text = ''.join(c for c in text.lower() if c.isalnum())
  return text == text[::-1]

print(is_palindrome('1221'))
print(is_palindrome("hello"))  