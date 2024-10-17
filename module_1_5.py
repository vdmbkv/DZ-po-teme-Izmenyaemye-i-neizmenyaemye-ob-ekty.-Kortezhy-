# 1

immutable_var = ([1, 5], "Benediktiner", True)
print(immutable_var)

# 2

immutable_var[0][0] = 5
immutable_var[0][1] = 10
print(immutable_var)

# Кортеж полезен в тех случаях, когда в процессе кодинга нам необходимо хранить данные в неизменном виде.
# Неизменяемость кортежа обеспечивает стабильность данных и безопасность кода.
# Также кортеж используем меньше места в памяти, чем список.

# 3

mutable_list = [15, 30, False]
mutable_list[0], mutable_list[2] = 3, True
print(mutable_list)
