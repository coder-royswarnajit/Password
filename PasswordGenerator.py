import random

Pass=['1','2','3','4','5','6','7','8','9','0',
      '!','@','#','$','%','^','&','*','_','+','-','=','<','>','/','|','`','~','.',
      'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M',
      'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

password=""
for i in range(16):
    password=password + random.choices(Pass)[0]

print("YOUR PASSWORD GENERATED BY MACHINE IS:",password)