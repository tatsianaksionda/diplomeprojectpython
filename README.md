# diplomeprojectpython
Data Encryption Project

The project uses an algorithm RSA with some addition.

>To find the open key:
>>1. Choose two prime numbers.
>>2. Calculate the modulus - the product of prime numbers (n).
>>3. Calculate the Euler function (φ).
>>4. Choose a number (e) that meets the following criteria:
>>>+ it must be simple,
>>>+ it must be less than φ,
>>>+ it must be relatively prime to φ.

Now the pair of numbers {e, n} is the public key.


>To find the secret key:

It is necessary to calculate the number (d), the inverse of (e) modulo (φ). That is, the modulo (φ) remainder of the product (d×e) must be equal to 1: (d×е)%φ=1.
The pair {d, n} is the secret key. It cannot be shared with anyone.

Only the owner of the private key can decrypt what was encrypted with the public key.

>Encryption stage:
>>Define the (main element): ord(source text character) ** (e) % (n)
>>The encrypted text character is found by the formula: chr(ord(source text character) + main_element % 100)
>>The encrypted text is ready.