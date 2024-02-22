from flask import Flask, render_template
# ჩემი მიზანია დავწერო პროგრამა, რომელიც ინფუთად მიიღებს პიროვნების სახელს, გვარს და დაბადების თარიღს 
# შემდეგი ფორმატით: (დღე/თვე/წელი). Პროგრამაში მონაცემების შეტანის შემდეგ, ეკრანზე უნდა გამოიბეჭდოს მისალმება მითითებულ სახელზე და გვარზე, პიროვნების ასაკი და განსაზღვრება თუ რომელ ზოდიაქოს ნიშანს ეკუთვნის ის.

# ზოდიაქოს ნიშნების განაწილება თარიღების მიხედვით:
# ვერძი - 21 მარტი - 20 აპრილი
# კურო - 21 აპრილი - 21 მაისი
# ტყუპები - 22 მაისი - 21 ივნისი
# კირჩხიბი - 22 ივნისი - 23 ივლისი
# ლომი - 24 ივლისი - 23 აგვისტო
# ქალწული - 24 აგვისტო - 23 სექტემბერი
# სასწორი - 24 სექტემბერი - 23 ოქტომბერი
# მორიელი - 24 ოქტომბერი - 22 ნოემბერი
# მშვილდოსანი - 23 ნოემბერი - 21 დეკემბერი
# თხის რქა - 22 დეკემბერი - 20 იანვარი
# მერწყული - 21 იანვარი - 19 თებერვალი
# თევზები - 20 თებერვალი - 20 მარტი



# შევქმნათ კლასი რომლის საშუალებითაც გამოვითვლით სხვადასხვა დეტალს:
class Zodiacsign(object):
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
    # ამ მეთოდის საშუალებით კი გამოვითვლით მომხმარებლის დაბადების წელს და ასაკს
    def age(self):
        birthyear = int((self.date_of_birth.split("/")[2]))
        current_year = 2024
        return current_year - birthyear
    # შემდეგ დაგვჭირდება რომ გავწეროთ მეთოდი რომლის საშუალებითაც გავიგებთ რომელ ზოდიაქოს მიეკუვნება ესა
    # თუ ის პიროვნება
    def zodiac_sign(self):
        # data = int(self.date_of_birth.split("/"))
        data = list(map(int, self.date_of_birth.split("/")))
        # print(data)
        if (data[0]==3 and data[1]>=21) or (data[0]==4 and data[1]<=20):
            return "ვერძი"
        elif (data[0]==4 and data[1]>=21) or (data[0]==5 and data[1]<=21):
            return "კურო"
        elif (data[0]==5 and data[1]>=22) or (data[0]==6 and data[1]<=21):
            return "ტყუპები"
        elif (data[0]==6 and data[1]>=22) or (data[0]==7 and data[1]<=23):
            return "კირჩხიბი"
        elif (data[0]==7 and data[1]>=24) or (data[0]==8 and data[1]<=23):
            return "ლომი"
        elif (data[0]==8 and data[1]>=24) or (data[0]==9 and data[1]<=23):
            return "ქალწული"
        elif (data[0]==9 and data[1]>=24) or (data[0]==10 and data[1]<=23):
            return "სასწორი"
        elif (data[0]==10 and data[1]>=24) or (data[0]==11 and data[1]<=22):
            return "მორიელი"
        elif (data[0]==11 and data[1]>=23) or (data[0]==12 and data[1]<=21):
            return "მშვილდოსანი"
        elif (data[0]==12 and data[1]>=22) or (data[0]==1 and data[1]<=20):
            return "თხის რქა"
        elif (data[0]==1 and data[1]>=21) or (data[0]==2 and data[1]<=19):
            return "მერწყული"
        elif (data[0]==2 and data[1]>=20) or (data[0]==3 and data[1]<=20):
            return "თევზები"
        else:
            return "გთხოვთ შეიყვანოთ დაბადების თარიღი შემდეგი ფორმატით: dd/mm/yy"
        
    def greet_person(self): 
        age = self.age() 
        zodiac_sign = self.zodiac_sign() 
        print(f"გამარჯობა, {self.first_name} {self.last_name}") 
        print(f"შენ ხარ {age} წლის") 
        print(f"შენი ზოდიაქოს ნიშანია {zodiac_sign}") 
        
# ვთხოვოთ მომხმარებელს მოგვაწოდოს ძირითადი ინფორმაცია:
name = input("შეიყვანეთ თქვენი სახელი: ")
surname = input("ახლა გვარი: ")
date_of_birth = input("შეიყვანეთ თქვენი დაბადების თარიღი შემდეგი ფორმატით (mm/dd/yyyy): ")

person = Zodiacsign(name, surname, date_of_birth)
person.greet_person()
