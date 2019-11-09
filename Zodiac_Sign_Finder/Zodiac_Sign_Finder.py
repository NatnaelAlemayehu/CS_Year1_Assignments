print("Welcome to Zodiac Sign finder.")
Name = input("What is your First Name? \n")
Month = input("What Month were you born? (Type in your month as text only such that begins it with capital letter, for example January or March)? \n")
Date = int(input("What date were you born? (use number only, for example 02, 06 or 12)? \n"))


if Month == 'January':
	Zodiac_sign = 'Capricorn' if (Date <= 19) else 'aquarius'
elif Month == 'February':
	Zodiac_sign = 'Aquarius' if (Date <= 18) else 'pisces'
elif Month == 'March':
	Zodiac_sign = 'Pisces' if (Date <= 20) else 'aries'
elif Month == 'April':
	Zodiac_sign = 'Aries' if (Date <= 19) else 'taurus'
elif Month == 'May':
	Zodiac_sign = 'Taurus' if (Date <=19) else 'gemini'
elif Month == 'June':
	Zodiac_sign = 'Gemini' if (Date <= 20) else 'cancer'
elif Month == 'July':
	Zodiac_sign = 'Cancer' if (Date <= 22) else 'leo'
elif Month == 'August':
	Zodiac_sign = 'Leo' if (Date <= 22) else 'virgo'
elif Month == 'September':
	Zodiac_sign = 'Virgo' if (Date <= 22) else 'libra'
elif Month == 'October':
	Zodiac_sign = 'Libra' if (Date <= 24) else 'scorpio' 
elif Month == 'November':
	Zodiac_sign = 'scorpio' if (Date <= 21) else 'sagittarius'
elif Month == 'December':
	Zodiac_sign = 'Sagittarius' if (Date <= 21) else 'capricorn'
	


print("Hey {}".format(Name), "your zodiac sign is {}".format(Zodiac_sign))
k=input("press anykey to exit")

#
##rr
###