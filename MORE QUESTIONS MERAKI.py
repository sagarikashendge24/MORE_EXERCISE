# i=0
# while i <1000:
#     if i%3==0:
#         print("nav")    
#     elif i%7==0:
#         print("gurukul")
#     elif i%21==0:
#         print("navgurukul")
#     else:
#         print(i)
#     i=i+1  


# a=int(input("NUMBER OF STUDENTS"))
# b=int(input("EXPENCE OF ONE STUDENT"))
# c=b*a
# if c<=50000:
#     print("HAMARE BUJJET MAI HAI")
# if c>50000:
#     print("HAMARE BUJJET MAI NAHI HAI")

# string_name = "Shakrudin"
# print (len(string_name))

# string_name = "Rishabh Verma"
# print (len(string_name)) 

# string_name = "navgurukul"
# if "n" in string_name:
#     print ("n hai")
# else:
#     print ("n nahi hai") 
# print ("n" in string_name:)
# print (type("n" in string_name)) 

# n=input("ENTER THE PASSWORD")
# if len(n)>6 or len(n)<16:
#     if "$" in n:
#         if "2" in n or "8" in n:
#             if "A" in n or "Z" in n:
#                 print("it is a strong password")
#             else:
#                 print ("it is weak password")   
#         else:
#             print("it is weak password")
#     else:
#         print("it is weak password") 
# else:
#     print("it is weak password")       
                
# # a=int(input("enter the no"))      
# b=int(input("enter the no"))      
# c=int(input("enter the no"))         
# if  a>c and a>b :
#     print(a,"is greater")
# if b>a and b>c:
#     print(b,"is grater")
# if c>a and c>b:
#     print(c,"is greater") 
# else:
#     print("all are equal")                


# n=int(input("enter the number"))
# i=1
# c=1
# while i<=n:
#     c=c*i
#     i=i+1
# print(c)    


# a = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"] 
# i=0
# p=[]
# while i<len(a):
#     if a[i] not in p:
#         p.append((a[i]))
#     i=i+1
# print(p)            


# a=[1, 342, 75, 23, 98]
# b=[75, 23, 98, 12, 78, 10, 1] 
# i=0
# c=[]
# while i<len(b):
#     if b[i]  in a:
#         c.append((b[i]))
#     i=i+1
# c.sort()    
# print(c)        

# a= [1,5,10,12,16,20]
# b= [1,2,10,13,16] 
# i=0
# c=[]
# while i< len(a):
#     if a[i] not in c:
#         c.append(a[i]) 
#         j=0
#         while j <len(b):
#             if b[j] not in c:
#                 c.append(b[j])
#             j=j+1       
#     i=i+1
# c.sort()    
# print(c)       


# big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
# counter1 = 0
# while counter1 < len(big_list):
#     small_list_length = len(big_list[counter1])
#     counter2 = 0
#     while counter2 < small_list_length:
#         print (big_list[counter1][counter2])
#         counter2 = counter2 + 1
#     counter1 = counter1 + 1
#     print ('-----') 


# n=int(input("enter the number"))
# c=n
# sum=0
# while n>0:
#     sum+=n%10
#     n=n//10
# if (c%sum==0):
#     print( "is a harshad number")  
# else:   
#     print("is not a harshad number")

# i=1
# while i<100:
#     a=i%10
#     b=(i//10)%10
#     c=(i//10)//10
#     d=a+b+c
#     if i%d==0:
#         print(i,"is harshad number")
#     else:
#         print(i,"is not harshad nuber")
#     i=i+1    

# def isharshadno(a):
#     n=a
#     c=n
#     sum=0
#     while n>0:
#         sum+=n%10
#         n=n//10
#     if (c%sum==0):
#         print( "is a harshad number")  
#     else:   
#         print("is not a harshad number")
# isharshadno(10)

# marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13],
#  [94, 89, 78, 76], [87, 55, 98, 99]] 
# i=0
# while i<len(marks):
#     b=len(marks[i])
#     j=0
#     while j<b:
#         if marks[j]>b:
#             print(marks[j])
#         j=j+1
#     i=i+1

# s = [45,883, 21, 72, 63333,234,567,123,122,22222226,1] 
# i=0
# while i<len(s):
#     j=0
#     p=s[i]
#     while j<len(s):
#         if p<s[j]:
#             p=s[j]
#         j=j+1
#     i=i+1
# print(p)    


# def greater(a):
#     i=0
#     while i<len(a):
#         j=0
#         p=a[i]
#         while j>len(a):
#             if p>a[j]:
#                 p=a[j]
#             j=j+1
#         i=i+1
#     print(p)  
# marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13],
#  [94, 89, 78, 76], [87, 55, 98, 99]]    
# greater(marks) 


# def numbers_less_than_twenty(list):
#     counter = 0
#     while counter < len(list):
#         item = list[counter]
#         if item > 20:
#             list.remove(item)
#         else:
#             counter += 1
#     return list
# num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
# num_list_sub_20 = numbers_less_than_twenty(num_list)
# print ("Initial list", num_list)
# print ("List that doesn't contain numbers greate than 20", num_list_sub_20) 


# from random import randint
# def win():
#     print ('You win!')
# def lose():
#     print ('You lose!')
# while True :
#     player_choice = input('What do you pick? (rock, paper, scissors)')
#     player_choice.strip()
#     random_move = randint (0, 2)
#     moves = ['rock', 'paper', 'scissors']
#     computer_choice = moves[random_move]
#     if player_choice == computer_choice:
#         print ('Draw!')
#     elif player_choice == 'rock' and computer_choice == 'scissors':
#         win()
#     elif  player_choice== 'paper' and computer_choice == 'scissors':
#         lose()
#     elif player_choice == 'scissors' and computer_choice == 'paper':
#         win()
#     elif player_choice == 'scissors' and computer_choice == 'rock':
#         lose()
#     elif player_choice == 'paper' and computer_choice == 'rock':
#         win()
#     elif player_choice == 'rock' and computer_choice =='paper':
#         lose()
#     again = input('Do you want to play again? (y or n)').strip()
#     if again == 'n':
#         break


chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
def encrypt_message(plain_message):
    encrypted_msg = ""
    for character in encrypted_msg:
        if character in chars:
            char_index = find_in_list(character, chars)
            new_char = shifted_chars[char_index]
            encrypted_msg = encrypted_msg + new_char
        else:
            encrypted_msg = encrypted_msg + character
def decrypt_message(decrypted_msg):
    decrypted_msg = ""
    for character in decrypted_msg:
        if character in shifted_chars:
            char_index = find_in_list(character, shifted_chars)
            new_char = chars[char_index]
            decrypted_msg = decrypted_msg + new_char
        else:
            decrypted_msg = decrypted_msg + character
flag = True
while flag == True:
    choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
    if choice == 'e':
        plain_message = input("Enter message to encrypt??")
        encrypt_message(plain_message)
    elif choice == 'd':
        encrypted_msg = input("Enter message to decrypt?")
        decrypt_message(encrypted_msg)
    else:
        play_again = input(";Do you want to try agian or Do you want to exit? (Y/N)")
        if play_again == 'Y':
            continue
        elif play_again == 'N':
            break     
        
    



# def encrypt():
#       message = input("Enter the message you want to encrypt")
#   ascii_message = [ord(char)+3 for char in message]
#   encrypt_message = [ chr(char) for char in ascii_message]  
#   print (''.join(encrypt_message))


# def decrypt():
#   message = input("Enter the message you want to decrypt")
#   ascii_message = [ord(char) for char in message]
#   decrypt_message = [ chr(char) for char in ascii_message]  
#   print (''.join(decrypt_message))

# flag = True
# while flag == False
# choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!")
# if choice = 'e':
# encrypt()
# els choice = 'd':
#   decrypt()    
# else
#     play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
#     if play_again == 'Y'
#         continue
#     elif play_again == 'N':
#         break 