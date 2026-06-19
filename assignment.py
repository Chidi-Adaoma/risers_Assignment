
#Assignment 1


dob = (1, 8, 1997)
today = (18, 6, 2026)

bd, bm, by = dob
td, tm, ty = today

def leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def total_days(day, month, year):
    months = [31, 28, 31, 30, 31, 30,
              31, 31, 30, 31, 30, 31]
    days = day

    for y in range(1, year):
        days += 366 if leap(y) else 365

    for m in range(month - 1):
        days += months[m]

    if month > 2 and leap(year):
        days += 1

    return days


days_old = total_days(td, tm, ty) - total_days(bd, bm, by)


def weekday(day, month, year):

    if month < 3:
        month += 12
        year -= 1

    k = year % 100
    j = year // 100

    h = (day + (13 * (month + 1)) // 5 +
         k + k // 4 + j // 4 + 5 * j) % 7

    names = ["Saturday", "Sunday", "Monday",
             "Tuesday", "Wednesday", "Thursday", "Friday"]

    return names[h]


born_day = weekday(bd, bm, by)

next_year = ty

if (tm > bm) or (tm == bm and td > bd):
    next_year += 1

days_until = (
    total_days(bd, bm, next_year)
    - total_days(td, tm, ty)
)


print("\n    MY BIRTHDAY REPORT")
print("=" * 30)
print("Date of Birth :", dob)
print("Born On       :", born_day)
print("Days Old      :", days_old)
print("Days Until Birthday :", days_until)


# Assignment 2

full_name = "CHIDI ADAOMA ELIZABETH"

first_name = full_name.split()[0]
shift = len(first_name)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text, shift):
    encrypt = ""

    for character in text:
        if character in alphabet:
            position = alphabet.index(character)
            new_position = (position + shift) % 26
            encrypt += alphabet[new_position]
        else:
            encrypt += character

    return encrypt
def decrypt(text, shift):
    decrypt = ""

    for character in text:
        if character in alphabet:
            position = alphabet.index(character)
            new_position = (position - shift) % 26
            decrypt += alphabet[new_position]
        else:
            decrypt += character

    return decrypt


encrypted_name = encrypt(full_name, shift)
decrypted_name = decrypt(encrypted_name, shift)




print("=" * 30)
print("      ADVANCED CIPHER REPORT")
print("=" * 30)
print("Original Name :", full_name)
print("Shift Value   :", shift)
print("Encrypted Name:", encrypted_name)
print("Decrypted Name:", decrypted_name)


# Assignment 3

expenses = [
    ('rice', 2000, 4000),
    ('beans', 2000, 1500),
    ('garri', 5000, 3500),
    ('fan', 30000, 40000),
    ('board', 3000, 3000),
    ('book', 1000, 1000),
    ('mouse', 5000, 9000),
    ('pen', 100, 100),
    ('keyboard', 100, 100),
    ('bag', 2000, 1500)
]

overspent = 0
underspent = 0

for x in expenses:
    if x[1] < x[2]:
        overspent_per_item = x[2] - x[1]
        overspent += overspent_per_item

for y in expenses:
    if y[1] > y[2]:
        underspent_per_item = y[1] - y[2]
        underspent += underspent_per_item

worst_item = ""
worst_percentage = 0

for z in expenses:
    if z[2] > z[1]:
        percentage = ((z[2] - z[1]) / z[1]) * 100

        if percentage > worst_percentage:
            worst_percentage = percentage
            worst_item = z[0]


total_budget = 0
total_actual = 0

for a in expenses:
    total_budget += a[1]
    total_actual += a[2]

budget_efficiency = (total_budget / total_actual) * 100


print("\n🤑 EXPENSE TRACKING REPORT 🤑")
print("=" * 55)

print(f"{'📦 ITEM':<15}{'💵 BUDGET':>12}{'🧾 ACTUAL':>12}")
print("-" * 55)

for item, budget, actual in expenses:
    print(f"{item:<15}{budget:>12,}{actual:>12,}")

print("=" * 55)

print(f" Total Overspent      : ₦{overspent:,}")
print(f" Total Underspent     : ₦{underspent:,}")
print(f"  Worst Budget Breach : {worst_item.title()}")
print(f" Overspend Percentage : {worst_percentage:.2f}%")
print(f" Budget Efficiency    : {budget_efficiency:.2f}%")

print("=" * 55)

if budget_efficiency >= 90:
    print(" Excellent Budget Management!")
elif budget_efficiency >= 75:
    print("Good Budget Management!")
else:
    print("Budget Needs Improvement!")




# Assignment 4

buildings = [
    ("Blue House", "Residential", 1995),
    ("City Mall", "Commercial", 2005),
    ("Green Villa", "Residential", 1980),
    ("Ngwa high school", "Education", 1990),
    ("Grneral Hospital", "Health", 2010),
    ("Old Post Office", "Government", 1975),
    ("Sky Towers", "Commercial", 2018),
    ("Unity Church", "Religious", 1988)
]
current_year = 2026

types = set()
after_2000 = []
ages = []
oldest = buildings[0]

for name, btype, year in buildings:

    types.add(btype)

    age = current_year - year
    ages.append(age)

    if year > 2000:
        after_2000.append(name)

    if year < oldest[2]:
        oldest = (name, btype, year)

average_age = sum(ages) / len(ages)

print("\nBUILDING REPORT")
print("=" * 30)

print("Oldest Building:", oldest[0], "-", oldest[2])

print("\nUnique Types:", types)

print("\nBuilt After 2000:")
for b in after_2000:
    print("-", b)

print("\nAverage Age:", round(average_age, 1), "years")