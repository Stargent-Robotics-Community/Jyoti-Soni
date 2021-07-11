# 1.
movies_shows=["Loki","Alive","Riverdale",'Parasite','13 reasons why','Stranger Things','The Midnight Sky','Cats']

print("The list of favourite Shows and Movies: ")
n=0
while n<len(movies_shows):
        print(n+1,". ",movies_shows[n])
        n=n+1
        


####################################################################################################################
# 2.
i=2
while i>0:
    movies_shows.append(input("Enter any of your favourite movies and shows: "))
    i=i-1
for names in movies_shows:
        print(names)

####################################################################################################################
# 3.
print("Every 2nd element from the list: ")
print(movies_shows[2::2])

###################################################################################################################
# 4.
num_list=[]
print("Enter five numbers to be added: ")
i=0
while i<5:
    i=i+1
    num_list.append(int(input("enter: ")))

sum=0
for num in num_list:
    sum=sum+num
    

print("The sum of entered numbers: ",sum)  


###################################################################################################################
# 5. 

i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    i=i+1 
    print()   