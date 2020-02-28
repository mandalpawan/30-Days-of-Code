'''
Sample Input

2
Hacker
Rank
Sample Output

Hce akr
Rn ak
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
number_of_input = int(input())
for i in range(number_of_input):
    my_string = input()
    odd_place = ''
    even_place = ''
    count = 0
    for i in my_string:
        if count%2==0:
            even_place = even_place+i
        else:
            odd_place = odd_place + i
        count +=1
    print(even_place,odd_place)

'''
this is for onle line code

for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])
'''
