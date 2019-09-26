"""
CS2302
Lab 2 Part B
Purpose: Write a Python 3 program that finds the 20 most used password using linked list
Created on September 16, 2019
Diego Aguirre
@author: Nancy Hernandez
"""

import time

class Node(object):
    password = ""
    count = -1
    next = None

    def __init__(self, password, count, next):
        self.password = password
        self.count = count
        self.next = next


# List Functions
class LList(object):
    # Constructor
    def __init__(self):
        self.head = None


def Append(L, x):
    # Inserts x at end of list L
    if is_empty(L):
        L.head = Node(x)
        L.tail = L.head

    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next


def is_empty(L):
    return L.head is None


# Gets length of the linked list
def get_length(L):
    temp = L.head
    count = 0
    while temp is not None:
        count += 1
        temp = temp.next
    return count


def solution_a():
    password_file = open("password_file.txt", "r")
    lines = password_file.readline()
    linked_list = LList()
    temp = linked_list.head

    for lines in password_file:
        # Splits lines here
        lines = lines.strip().split("	")
        password = lines[-1]

        # If password isn't in the linked list already, it will add it here
        if not contained(password, linked_list):
            linked_list.head = Node(password, 1, linked_list.head)

    password_file.close()

    while temp is not None:
        print("Password:", temp.password, "Repeated:", temp.count)
        temp = temp.next

    return linked_list

# Most of the following code was taken from the lab instructions
def solution_b():
    password_dictionary = {}
    linked_list = LList()
    temp = linked_list.head

    password_file = open('password_file.txt', 'r')
    lines = password_file.readline()

    for lines in password_file:
        #Splits lines here
        lines = lines.strip().split(" ")
        password = lines[-1]

        # If password is in dictionary it increases count
        if password in password_dictionary:
            password_dictionary[password].count += 1

        else:
            linked_list.head = Node(password, 1, linked_list)
            password_dictionary[password] = linked_list.head

    password_file.close()

    while temp is not None:
        print("Password:", temp.password, "Repeated:", temp.count)
        temp = temp.next

    return linked_list


# Checks if password is already inside the linked list
def contained(password, L):
    temp = L.head

    while temp is not None:
        if temp.password != password:
            temp = temp.next
        else:
            #increase num of times password has been seen
            temp.count += 1
            return True
    return False


# Sorts liked list using bubble sort
def bubble_sort(L):
    sorted = False

    while not sorted:
        sorted = True
        temp = L.head
        current = L.head.next

        while current is not None:
            if temp.count.artistName > current.count.artistName:
                sorted = False
                temp.count, current.count = current.count, temp.count

            temp = current
            current = current.next


# Sorts list using merge sort
def mergeSort(L):
    counter = 0
    length = get_length(L)

    # returns list if there is only one element
    if length < 2:
        return L
    else:
        mid = length // 2
        # less than
        L1 = LList()
        # more than
        L2 = LList()

        temp = L.head
        left_temp = L1.head
        right_temp = L2.head
        while temp is not None:
            counter += 1
            # compares
            if counter <= mid:
                Append(L1, temp.item)
                temp = temp.next
            else:
                Append(L2, temp.item)
                temp = temp.next

        mergeSort(L1)
        mergeSort(L2)

        left_temp = L1.head
        right_temp = L2.head
        temp = L.head

        # while lists are not empty
        while left_temp and right_temp is not None:
            # compares
            if left_temp.item < right_temp.item:
                temp.item = left_temp.item
                left_temp = left_temp.next
                temp = temp.next
            else:
                temp.item = right_temp.item
                right_temp = right_temp.next
                temp = temp.next

        # checks numbers in first list
        while left_temp is not None:
            temp.item = left_temp.item
            left_temp = temp.next
            temp = temp.next

        # checks numbers in second list
        while right_temp is not None:
            temp.item = right_temp.item
            right_temp = temp.next
            temp = temp.next
    return L


# Prints 20 most used passwords
def print_duplicates(L):
    temp = L.head
    count = 20
    while count <= 20:
        print("Password: ", temp.password, "seen:", temp.count)
        temp = temp.next


def main():
    print("making linked list")

    start = time.time()
    a = solution_a()
    # b = solution_b()

    print("sorting list w/ bubble")

    bubble_sort(a)
    # merge_sort(b)
    end = (time.time() - start)

    print(end, "time")


main()
