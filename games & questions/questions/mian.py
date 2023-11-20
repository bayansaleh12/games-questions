# Write a function called reverse_string that takes a string as input and returns its reverse.
# example  "hello" => "olleh"
def reverse_string(word):
    return word[::-1]


print(reverse_string("bayan"))


# Write a function called is_palindrome that takes a string as input and
# returns True if the string is a palindrome and False otherwise.
# examoles "sosa" => False
# example  "A man, a plan, a canal: Panama" => True

def is_palindrome(word):
    clean_word = ''.join(char.lower() for char in word if char.isalnum())
    if clean_word == reverse_string(clean_word):
        return True
    else:
        return False


print(is_palindrome("sosa"))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("bayan"))
print(is_palindrome("aya"))


# Write a function called remove_duplicates that takes a list as input and
# returns a new list with duplicate elements removed.
# example [3,2,2,4,5] => [3,2,4,5]


def remove_duplicates(input_list):
    no_duplicate = []
    for i in input_list:
        if i not in no_duplicate:
            no_duplicate.append(i)
    return no_duplicate


print(remove_duplicates([3, 2, 2, 4, 5]))


# Write a function called list_sum that takes a list of numbers as input and
# returns the sum of all elements.
# example [5,5,5] => 15

def list_sum(input_list):
    return sum(input_list)


print(list_sum([3, 2, 10, 4, 5]))


# Write a function called remove_element that takes a list and an element
# as input and removes all occurrences of that element from the list.
# The function should return the modified list.
# example [1,2,6,5,3], 3 => [1,2,6,5]


def remove_element(input_list, element):
    while element in input_list:
        input_list.remove(element)
    return input_list


print(remove_element([3, 2, 10, 4, 5], 5))
