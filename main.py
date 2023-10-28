import random

# wybiera liczbę do zgadnięcia i przypisuje ją do to_guess
to_guess = random.randint(0, 100)

# zawsze wykona to, co w pętli
while True:
    # 1. Wypisze "Please provide number: "
    # 2. Wczyta z konsoli to, co użytkownik wpisze z klawiatury
    # 3. To, co przyszło z klawiatury, jest stringiem (napisem). Trzeba to zamienić na int
    # 4. Przypisuje wynik tych operacji do zmiennej answer
    answer = int(input("Please provide number: "))
    # porównuje wartość zmiennej answer z to_guess
    # jeśli jest równy to
    if answer == to_guess:
        # przerwij pętlę i idź do pierwszej linii poza nią
        break
    # w przeciwnym przypadku, jeśli wartość zmiennej answer jest większa od to_guess
    elif answer > to_guess:
        # wypisz komunikat
        print("Provided number is too big!")
    # jeśli żadna z powyższych porównań nie była prawdziwa to
    else:
        # wypisz komunikat
        print("Provided number is too small!")
# wypisz komunikat z wartością liczby to_guess
print(f"Bravo you guessed correctly! The number was {to_guess}!")
