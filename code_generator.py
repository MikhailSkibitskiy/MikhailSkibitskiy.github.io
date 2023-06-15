def generator():
    import random

    small_s = "qwertyuiopasdfghjklzxcvbnm"
    big_s = "QWERTYUIOPASDFGHJKLZXCVBNM"
    number_s = "0123456789"

    use_for = small_s + big_s + number_s
    length_code = 9

    code = "".join(random.sample(use_for, length_code))
    print(code)

a = generator()