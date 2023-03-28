# Probleme de algoritmica random
# Problema 1
# 1! + 2! + 3! + 4! + ... +n!
import random


def factorial(number):
    x = 1
    factorial_list = []
    while number > 0:
        x *= number
        number = number - 1
        if x not in factorial_list:
            factorial_list.append(x)
    return factorial_list[-1]

def algoritm(start_number, gap_number, last_number):
    next_number = start_number
    list = [start_number]
    lista_cu_factoriale = [start_number*start_number]

    while next_number != last_number:
        next_number += gap_number
        list.append(next_number)
        x = factorial(next_number)

        if x not in lista_cu_factoriale:
            lista_cu_factoriale.append(x)
    final_result = sum(lista_cu_factoriale)
    return final_result


# Problema 2
# Conversie din cifre romane in arabe si invers (clasa)

def roman(number):

    dictionaire = {
        1 : "I",
        2 : "II",
        3 : "III",
        4 : "IV",
        5 : "V",
        6 : "VI",
        7 : "VII",
        8 : "VIII",
        9 : "IX",
        10 : "X"
    }
    result = ""
    result += dictionaire.get(number, "nu corespunde")
    return result






# 3.) Write a Python program to create an instance of a specified class and display the namespace of the said instance






# 4.)4.) Write a Python class to get all possible unique subsets from a set of distinct integers. Go to the editor
# Input : [4, 5, 6]
# Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
def list_creator(*numbers):
    return numbers



def subsets1(*args):
    input=[*args]
    output = []
    string_lists= [[],[],[]]
    input_counted_numbers = len(input)
    counter = 0
    num=0
    #A.) This part gets all elements from the input
    while counter != input_counted_numbers:
        if input[num] not in string_lists:
            string_lists[num].append(input[num])
            for string in string_lists:
                if string not in output:
                    output.append(string)
            counter += 1
            num +=1
    return output

def subsets2(*args):
    input = [*args]
    count = 1
    output = []
    input_counted_numbers = len(input)
    while count != input_counted_numbers:
        output.append(list_creator(input[0],input[count]))
        count +=1
    return output




def givesubset(*args):
    output = subsets1(*args)
    output1=subsets2(*args)
    output2 = [args]
    return output+ output1 + output2


pp = givesubset(9,8,2)


#5.) Random strong password creator
def password_creator(ch_numbers):
    count = 0
    ch_list = []
    password = ""
    d = ["1", "2", "3", "4", "5", "6", "7", "8", "9","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"
        , "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    while count != ch_numbers:
        ch_list.append(random.choice(d))
        password += ch_list[count]
        count+=1
    return password


class Castellon:
    temperatura = (30,36)
    def __init__(self,ziua,luna,anul):
        self.ziua = ziua
        self.luna = luna
        self.anul = anul

    def go_to_beach(self, mijloc_de_transport):
        alternatives = ["by_bus","by_bike","by_car","by_walking"]
        if mijloc_de_transport == alternatives[0]:
            return 30
        if mijloc_de_transport == alternatives[1]:
            return 30
        if mijloc_de_transport == alternatives[2]:
            return 10
        if mijloc_de_transport == alternatives[3]:
            return 60
        else:
            return None

    def go_to_bar(self):
        bars =["centru","salera","la liviu"]
        return "You can go to : ",bars, "etc"

switch_case = {
    1: "spring",
    2: "summer",
    3: "autumn",
    4: "winter",
}

def switch(x):
    switch_case = {
        "01": "spring",
        "02": "summer",
        "03": "autumn",
        "04": "winter"
    }
    return switch_case[x]

switch_cases = {
        1: "spring",
        2: "summer",
        3: "autumn",
        4: "winter"
    }

patrat = lambda n,b,c : n*b*c




#PY100FUNCTIONS ex 1:
#Write a Python function to find the Max of three numbers.

def max_number(list):
    try_number = 0
    spot_number = 0
    while try_number != len(list)-1:
        try_number +=1
        if list[spot_number] < list[try_number]:
            spot_number = try_number
    return list[spot_number]



#PY100FUNCTIONS ex 2:
#Write a Python function to sum all the numbers in a list.

def sum_numbers(lista):
    try_number = 0
    result = 0
    while try_number != len(lista):
        result += lista[try_number]
        try_number += 1
    return result


output = [8,2,3,-1,7]


#PY100FUNCTIONS ex 3:
#Write a Python function to multiply all the numbers in a list.
def multiply_numbers(lista):
    try_number = 0
    result = 1
    while try_number != len(lista):
        result *= lista[try_number]
        try_number += 1
    return result

#PY100FUNCTIONS ex 4:
#Write a Python program to reverse a string.

sample_string = "1234abcd"

def string_reverser(string):
    counter = 0
    string_lenght = len(string)
    output = ""
    while counter != string_lenght:
        counter +=1
        output += string[-1*counter]
    return output

#PY100FUNCTIONS ex 5:
#Write a Python function to calculate the factorial of a number (a non-negative3 integer).
#The function accepts the number as an argument.

def check(*arguments):

    not_in = []
    in_numbers = []
    for numbers in arguments:
        if numbers not in range(100):
            not_in.append(numbers)
        elif numbers in range(100):
            in_numbers.append(numbers)
    return f"{not_in} are not in the range",f"{in_numbers} + are in the range"



#PY100FUNCTIONS ex 6:
#Write a Python function that takes a list and calculate the number of upper case letters and lower case letter


def upp_low_counter(phrase):
    upper_count = []
    lower_count = []
    uppers = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lowers = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
    for letters in phrase:
        if letters in uppers:
            upper_count.append(letters)
        elif letters in lowers:
            lower_count.append(letters)
    return len(upper_count), len(lower_count)



def interviu_problem(pback,p2,p3,p4,baterry_left):
    pback = input("Introdu un numar : ")
    list = []
    x = 0
    list = [1,2,3,4,5,6,7,8,9,10]

    persons = [p2,p3,p4]
    suma = []
    tpersback = (len(persons)-1)* int(pback)
    for time in persons:
        if time not in suma:
            suma.append(time)
    suma_suma = sum(suma)
    result = tpersback + suma_suma
    if result < baterry_left:
        return True
    if result > baterry_left:
        return False ,result
