calls = 0
def count_calls():
    global calls
    calls = calls + 1
def string_info():
    n = input('Введите слово: ')
    string = (len(n), str.upper(n), str.lower(n))
    print(string)
    count_calls()
def is_contains():
    q = input('Введите строку: ')
    string = str.lower(q)
    list_to_search = []
    b = ""
    while b != "#":
        print(list_to_search)
        b = input('Введите слова списка, для завершения введите "#": ')
        b1 = str.lower(b)
        list_to_search.append(b1)
    if string in list_to_search:
        print("True")
    else:print("False")
    count_calls()
n = ""
while n != "3":
    n = input("Введите 1 для работы со словами, 2 для работы со списком, 3 для выхода: ")
    if n == "1":
        string_info()
        continue
    if n == "2":
        is_contains()
        continue
print("Досвидания, число операций: ", calls)
