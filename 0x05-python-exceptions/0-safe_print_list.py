#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
        try:
                sublist = my_list[:x]

                for element in sublist:
                        print(element, end=' ')

                print()
                return len(sublist)
        except:
                print("An error occurred")
                return 0
