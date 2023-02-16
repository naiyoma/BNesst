# def pay(hour, rate):
#     rate = rate * 1.5
#     hours = hours - 40
#     if hours > 40:
#         return hours * rate



# def grade(score):
   
#     try:
#         score = float(score)
#         if score >= 0.9:
#             print("Grade A")
#         elif score >= 0.8:
#             print("Grade b")
#         elif score >= 0.7:
#             print("Grade C")
#         elif score >= 0.6:
#             print("Grade D")
#         elif score < 0.6:
#             print("Grade F")
#     except:
#         print("Use Numbers")
# grade(score=input("Entre your score"))


# def feelings():
#     x = ["Goodmorning", "Afternoon", "Evening"]
#     for i in x:
#         greet = input("How are you feeling ")
#         print(i)
#         print("I am happy to hear you are feeling " + greet)
# feelings()


# username = "Test"
# password = "Pass"
# while True:
#     username = input("Username")
#     password = input("password")
#     if username  == username and password == password:
#         print("Access Granted")
#         break
#     else:
#         print("Try Again")
#         continue
# count = 0
# while True:
#     user_input = input("Entre a number: ")

# import statistics

# def program():
#     nums = 0
#     mean_arr = []
#     while True:
#         user_input = input("Enter a number: ")
#         if user_input == "done":
#             break
#         try:
#             num = int(user_input)
#             nums += num
#             mean_arr.append(num)
#         except ValueError:
#             print("Invalid input, please enter a number")
#     import pdb; pdb.set_trace()
#     print("Sum: ", nums, "Count: ", mean_arr.count(), "Mean: ", statistics.mean(mean_arr) )

# program()

# fruits = ["apple", "Mangoes"]

# for i in fruits:
#     print(i.upper())


# import math
# nums = [1,2,3]
# for k in nums:
#     print(math.pow(k, 2))

# dict_name = {
#     "nisa": "town",
#     "tina": "maria",
# }

# for key in dict_name:
#     print(
#     dict_name["nisa"],
#     dict_name["tina"])

# list_a = [1,3,4]
# for i in list_a:
#     print(max(list_a))


# list_nums = [[1,2,3], [2,2]]
# for i in list_nums:
#     print(sum(i))

# vowels = ["a", "e", "i","o","u" ]
# def vowel(string):
#     # import pdb; pdb.set_trace()
#     string = string.lower()
#     count_vowels=0
#     for x in string:
#         if x in vowels:
#            count_vowels = count_vowels+1
#     print(count_vowels)

# vowel("Hello, world!")

# strings = ["apple", "banana", "cherry", "date"]

# def str_a(strings):
#     arr = []
#     for i in strings:
#         if i[0].lower() == "a":
#             arr.append(i)
#     print(arr)


# str_a(["apple", "banana", "cherry", "date"])

#nuber 4
# def dict_count(sentence):
#     sentence = sentence.replace(" ", "")
#     dict_nums = {}
#     for i in sentence:
#         if i not in dict_nums:
#             count = sentence.count(i)
#             dict_nums[i] = count
#     print(dict_nums)
# dict_count("this is a test sentence")



#number 5
# def list_count(list1, list2):
#     new_arr = []
#     for i in list1:
#         if i in list2:
#             new_arr.append(i)
#     print(new_arr)
# list_count([1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 4, 6, 8, 10, 12, 14, 16, 18])



# def prime_numbers(numbers):
#     new_list = []
#     for num in numbers:
#         if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     break
#             else:
#                 new_list.append(num)
#     print(new_list)


# prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

#7
# def str_count(string):
#     count = string.split()
#     print(len(count))




# str_count("Write a program that takes a string")


# #8
# def palindrome_strings(strings):
#     pal_list = []
#     for string in strings:
#         if string == string[::-1]:
#             pal_list.append(string)
#     print(pal_list)
# palindrome_strings(["madam", "level", "civic"])

#9

# def most_frequent_word(sentence):
#     dict_nums = {}
#     words = sentence.split()
#     for i in words:
#         if i not in dict_nums:
#             count = sentence.count(i)
#             dict_nums[i] = count
#     word = max(dict_nums, key=dict_nums.get)
#     return (word, dict_nums[word])
# sentence = "this is a test sentence to test the test"
# most_frequent_word(sentence)



# def find_largest(numbers):
#     largest = None
#     for number in numbers:
#         if largest is None:
#             largest = number
#         else:
#             if number > largest:
#                 largest = number
#     return largest

# print(find_largest([-2,-3,-4, -1]))


# def find_duplicates(arr):
#     result = []
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] == arr[j] and arr[i] not in result:
#                 result.append(arr[i])
#     return result

# input_arr = [1, 2, 3, 4, 2, 3, 5, 6, 7, 3]
# output = find_duplicates(input_arr)
# print(output)




# data = ["item1", "item2", "item3"]
# for i in range(len(data)):
#     print(data[i])
#     data.pop(i)


# data = ["item1", "item2", "item3"]
# for i in data:
#     # import pdb; pdb.set_trace()
#     print(i)
#     data.pop(data.index(i))


# def list_nums(list_nums):
#     num_total = 0
#     for i in list_nums:
#         try:
#             num_total +=  int(i)
#         except ValueError:
#             print ("use nums only")
#     return num_total

# print(list_nums([1,2,3,5]))


# def files(filename):
#     try:
#         with open(filename, 'r') as file:
#             contents = file.read()
#             return contents
#     except FileNotFoundError:
#         print(f" file not found.")
        
# print(files("file.txt"))



def anagrams(words):
    words_map = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in words_map:
            words_map[sorted_word].append(word)
        else:
            words_map[sorted_word] = [word]

    print(set(words_map.values()))

A = ["cat",  "tea", "act", "eat"]
print(anagrams(A))