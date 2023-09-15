def create_an_empty_list():
    return []

def create_a_list():
    my_list = [1, "apple", True, 3.14]
    return my_list

my_list = create_a_list()
print(my_list)

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
    l.pop()
    return l

def remove_element_from_start_of_list(l):
    l.pop(0)
    return l

def retrieve_first_element_from_list(l):
    new_l = l[0]
    return new_l

def retrieve_element_from_index(l, index):
    new_l = l[index]
    return new_l

def retrieve_last_element_from_list(l):
    return None
