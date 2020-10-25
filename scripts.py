''' Introduction'''

# Name_Exercise_1
print("Hello, World!")

# Name_Exercise_2
if __name__ == '__main__':
    n = int(input().strip())
    if 1 <= n <= 100:
        if (n % 2) == 0:
            if 2 <= n <= 5:
                print('Not Weird')
            elif 6 <= n <= 20:
                print('Weird')
            else:
                print('Not Weird')
        else:
            print('Weird')
    
    else:
        print('Number has to be between 1 and 100')

# Name_Exercise_3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# Name_Exercise_4
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# Name_Exercise_5
if __name__ == '__main__':
    n = int(input())
    if 1<= n <= 20:
        for i in range(n):
            print(i**2)
    else:
        print('n has to be between 1 and 20')

# Name_Exercise_6
def is_leap(year):
    leap = False
    
    # Write your logic here
    if 1900 <= year <= 10**5:
        if (year%4)==0:
            if (year%100) == 0:
                if (year%400) == 0:
                    leap = True
                
            else:
                leap = True
    else:
        print('year has to be between 1990 and 1000000')

    return leap

year = int(input())
print(is_leap(year))

# Name_Exercise_7
if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 150:
        i = 1
        while i<=n:
            print(i, end = '')
            i += 1


''' Data types'''

# Name_Exercise_1
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # create lists
    list_1 = [x for x in range(x+1)]
    list_2 = [y for y in range(y+1)]
    list_3 = [z for z in range(z+1)]
    #use list comprehension to generate all permutations
    all_perm = [[x, y, z]   for x in list_1
                            for y in list_2
                            for z in list_3
                            if (x+y+z) != n]
    
    print(all_perm)

# Name_Exercise_2
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    if 2 <= n <= 10:
        array = sorted(set(arr))[-2]
        print(array)
    else:
        print('n has to be between 2 and 10')

# Name_Exercise_3
if __name__ == '__main__':
    nested_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # set nested list to append name and scoring
        nested_list.append([name, score])

    
    N = len(nested_list)
    score_list = []
    for i in range(N):
        score_list.append(nested_list[i][1])
    # sort only the scores
    score_list = sorted(score_list)
    # get the minimum score
    min_score = min(score_list)
    # create new scoring list
    score_list_2 = score_list[:]
    # remove the minimum scores from the second list
    for i in range(N):
        if score_list[i] == min_score:
            score_list_2.remove(min_score)
        else:
            pass
    #append the second minimum score on new list
    min_second = []
    for i in range(N):
        if nested_list[i][1] == score_list_2[0]:
            min_second.append(nested_list[i][0])
    
    min_second = sorted(min_second)
    for name in min_second:
        print(name)
    
# Name_Exercise_4
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # sum the marks of the query name
    a = 0
    for i in student_marks[query_name]:
        a += i
    # average the marks
    average_mark = a / len(student_marks[query_name])
    #print with 2 decimals
    print("%.2f" % average_mark)

# Name_Exercise_5
if __name__ == '__main__':
    N = int(input())
    # create empty list
    ls = []
    # loop through N
    for i in range(N):
        # split the input
        x, *l = input().split()
        # map as integer the inputs
        ls_2 = list(map(int, l))
        # check if elements in list are 1 or 2
        if len(ls_2) == 2:
            a = [ls_2[0]]
            b = [ls_2[1]]
        elif len(ls_2) == 1:
            a = [ls_2[0]]
        # check the parameters of the input
        if x == 'insert':
            ls.insert(a[0], b[0])
        elif x == 'append':
            ls.append(a[0])
        elif  x == 'remove':
            ls.remove(a[0])
        elif x =='print':
            print(ls)
        elif x == 'reverse':
            ls.reverse()
        elif x == 'pop':
            ls.pop()
        elif x == 'sort':
            ls.sort()

# Name_Exercise_6
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = ()
    for i in integer_list:
        t += (i,)
    
    print(hash(t))


''' Strings '''

# Name_Exercise_1
def swap_case(s):
    # check the length of the sentence
    if 0 <= len(s) <= 1000:
        # initialize the new sentence
        sentence = ''
        for each in s:
            # check if each letter is upper
            if each.isupper() == True:
                # lower the letter 
                each = each.lower()
                # store the letter in the new variable
                sentence += each
            else:
                # upper the letter
                each = each.upper()
                sentence += each
    else:
        print('Word has to be between 0 and 1000 words')

    return sentence

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# Name_Exercise_2
def split_and_join(line):
    # write your code here
    line = line.split()
    line= '-'.join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# Name_Exercise_3
def print_full_name(a, b):

    print("Hello " + a +' '+ b +'! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# Name_Exercise_4
def mutate_string(string, position, character):
    new_string = string[:position] + character + string[position+1:]
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Name_Exercise_5
def count_substring(string, sub_string):
    a = 0
    for i in range(len(string)):
        if sub_string == string[i:i+len(sub_string)]:
            a += 1
    
    return a

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# Name_Exercise_6
if __name__ == '__main__':
    s = input()
    # initialize the storage variable 
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    # loop through each letter
    for i in s:
        if i.isalnum():
            a += 1   
        if i.isalpha():
            b += 1
        if i.isdigit():
            c += 1
        if i.islower():
            d += 1
        if i.isupper():
            e += 1
   # check if each variable is higher than zero 
    if a > 0:
        print(True)
    else:
        print(False)
    if b > 0:
        print(True)
    else:
        print(False)
    if c > 0:
        print(True)
    else:
        print(False)
    if d > 0:
        print(True)
    else:
        print(False)
    if e > 0:
        print(True)
    else:
        print(False)

# Name_Exercise_7
thickness = int(input()) #This must be an odd number
c = 'H'

    #Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    #Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

    #Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

    #Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Name_Exercise_8
import textwrap

def wrap(string, max_width):       

    textwrap.wrap(string, max_width) 

    return textwrap.fill(string, max_width) 

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Name_Exercise_9
# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int,input().split())
for i in range(0,N//2): 
    print(('.|.'*i).rjust((M-2)//2,'-')+'.|.'+('.|.'*i).ljust((M-2)//2,'-'))
print('WELCOME'.center(M,'-'))
for i in range((N//2)-1,-1,-1): 
    print(('.|.'*i).rjust((M-2)//2,'-')+'.|.'+('.|.'*i).ljust((M-2)//2,'-'))

# Name_Exercise_10
def print_formatted(number):
    # your code goes here
    width=len(bin(number)[2:])
    for i in range(1,number+1):
        # used str function for decimal
        deci=str(i)
        # used oct function for octal
        octa=oct(i)[2:]
        # used hex function for hexadecimal
        hexa=(hex(i)[2:]).upper()
        # used bin function for binary
        bina=bin(i)[2:]
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# Name_Exercise_11 (I look for the help of Hackerrack)
def print_rangoli(size):
    # your code goes here
    for i in range (-(size-1),size):
        for j in range (-2*(size-1),2*(size-1)+1):
            if j%2==0 and (abs(j//2)+abs(i))< size:
                print((chr(abs(j//2)+abs(i)+ord('a'))), end='')
            else:
                print('-',end='')
        print()
     
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# Name_Exercise_12
# Complete the solve function below.
def solve(s):
    x = s.split(' ')
    y = ''
    for i in range(len(x)):
        if x[i].isalpha() == True:
            y += x[i][0].upper() + x[i][1:]
            if i != len(x)-1:
                y += ' '
            else:
                continue
        else:
            y += x[i]
            if i != len(x)-1:
                y += ' '
            else:
                continue

    return y

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# Name_Exercise_13
def minion_game(string):
    # your code goes here
    vow = 0
    con = 0
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    N = len(string)

    for i, each in enumerate(string):
        if each in vowels:
            vow += N - i
        else:
            con += N - i
    if vow == con:
        print('Draw')
    elif vow > con:
        print('Kevin %.0f' %vow)
    else:
        print('Stuart %.0f' %con)

    

if __name__ == '__main__':
    s = input()
    minion_game(s)

# Name_Exercise_14
def merge_the_tools(string, k):
    # your code goes here
    # get len of string
    n = len(string)
    # floor divion for guaranteed that n is a multiple of k.
    s = n // k
    # loop for getting the correct values and distances
    for i in range(s):
        l = string[i*k:(i+1)*k]
        # initialize the variable
        a = ''
        for j in l:
            if j not in a:
                # if the value is not reapeted, store it in the variable
                a += j
        
        print(a)
                
         

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


''' Sets '''

# Name_Exercise_1
def average(array):
    # your code goes here
    s = set(array)
    n = len(s)
    average = sum(s)/n
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# Name_Exercise_2
ln = map(int, input().split())
n = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

tot_happyness = 0
for j in n:
    if j in A:
        tot_happyness += 1
    elif j in B:
        tot_happyness -= 1

print(tot_happyness)

# Name_Exercise_3
M = input()
m = set(map(int, input().split()))
N = input()
n = set(map(int, input().split()))

a = m.union(n)
b = m.intersection(n)
c = sorted(a.difference(b))
for i in c:
    print(i)

# Name_Exercise_4
N = int(input())
n = set(input() for i in range(N))

print(len(n))

# Name_Exercise_5
n = int(input())
s = set(map(int, input().split()))
m=int(input())
for i in range(m):
    l = input().split()
    if l[0] == 'remove':
        s.remove(int(l[1]))
    elif l[0] == 'discard':
        s.discard(int(l[1]))
    else:
        s.pop()
print(sum(list(s)))

# Name_Exercise_6
n = int(input())
N = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))

print(len(N.union(B)))

# Name_Exercise_7
n = int(input())
N = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))

print(len(N.intersection(B)))

# Name_Exercise_8
n = int(input())
N = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))

print(len(N.difference(B)))

# Name_Exercise_9
n = int(input())
N = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))

print(len(N.symmetric_difference(B)))

# Name_Exercise_10
a = int(input())
A = set(map(int, input().split()))
for i in range(int(input())):
    x, y = input().split()
    if x == 'intersection_update':
        A.intersection_update(set(map(int, input().split())))
    elif x == 'update':
        A.update(set(map(int, input().split())))
    elif x == 'symmetric_difference_update':
        A.symmetric_difference_update(set(map(int, input().split())))
    else:
        A.difference_update(set(map(int, input().split())))

print(sum(A))

# Name_Exercise_11

