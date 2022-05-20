import random
from math import gcd
from re import split

from django.db import models


class Data_encryption(models.Model):
    email = models.EmailField(max_length=254, verbose_name='Email of user', null=True)
    user_text = models.TextField(verbose_name='Original text')
    open_key = models.CharField(max_length=15, verbose_name='Open key')
    secret_key = models.CharField(max_length=15, verbose_name='Secret key')
    encrypted_text = models.CharField(max_length=1000, verbose_name='Encrypted text')
    data_time_encryption = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{[self.email, self.user_text, self.open_key, self.secret_key, self.encrypted_text]!r}'

    class Meta:
        verbose_name = "Data of user's encryption"
        verbose_name_plural = "Data of user's encryption"

    def save(self, *args, **kwargs):
        if self.user_text:
            template = "{}, {}"
            list_prime_numbers1 = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                                   97,
                                   101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
                                   191,
                                   193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
                                   283,
                                   293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
                                   401,
                                   409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]

            random_number_for_keys = random.sample(list_prime_numbers1, 2)
            n = random_number_for_keys[0] * random_number_for_keys[1]
            f = (random_number_for_keys[0] - 1) * (random_number_for_keys[1] - 1)

            list = []
            for i in range(len(list_prime_numbers1)):
                if gcd(list_prime_numbers1[i], f) == 1:
                    list.append(list_prime_numbers1[i])
                else:
                    continue

            e = random.sample(list, 1)[0]

            self.open_key = template.format(e, n)

            template_2 = "{}, {}"
            list23 = []
            for i in range(1000000):
                if (i * e) % f == 1:
                    list23.append(i)
                else:
                    continue

            d = random.sample(list23, 1)[0]
            self.secret_key = template_2.format(d, n)

            text_new = ''

            self.open_key = str(self.open_key)
            e_1 = split(r', ', self.open_key)[0]
            n_1 = split(r', ', self.open_key)[1]
            self.user_text = str(self.user_text)
            text_length = len(self.user_text)
            for i in range(text_length):
                main_element = ord(self.user_text[i]) ** int(e_1) % int(n_1)
                new = chr(ord(self.user_text[i]) + main_element % 100)
                text_new += new

            self.encrypted_text = text_new

        super().save(*args, **kwargs)
