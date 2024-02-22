# ჩემი მიზანია დავწერო პროგრამა, რომელიც ინფუთად მიიღებს პიროვნების სახელს, გვარს და დაბადების თარიღს
# შემდეგი ფორმატით: (დღე/თვე/წელი). Პროგრამაში მონაცემების შეტანის შემდეგ, ეკრანზე უნდა გამოიბეჭდოს მისალმება მითითებულ სახელზე და გვარზე, პიროვნების ასაკი და განსაზღვრება თუ რომელ ზოდიაქოს ნიშანს ეკუთვნის ის.

# ზოდიაქოს ნიშნების განაწილება თარიღების მიხედვით:
# ვერძი - 21 მარტი - 20 აპრილი Aries
# კურო - 21 აპრილი - 21 მაისი Taurus
# ტყუპები - 22 მაისი - 21 ივნისი Gemini
# კირჩხიბი - 22 ივნისი - 23 ივლისი Cancer
# ლომი - 24 ივლისი - 23 აგვისტო Leo
# ქალწული - 24 აგვისტო - 23 სექტემბერი Virgo
# სასწორი - 24 სექტემბერი - 23 ოქტომბერი Libra
# მორიელი - 24 ოქტომბერი - 22 ნოემბერი Scorpio
# მშვილდოსანი - 23 ნოემბერი - 21 დეკემბერი Sagittarius
# თხის რქა - 22 დეკემბერი - 20 იანვარი Capricorn
# მერწყული - 21 იანვარი - 19 თებერვალი Aquarius
# თევზები - 20 თებერვალი - 20 მარტი Pisces

from flask import Flask, render_template, request

app = Flask(__name__)

# შევქმნათ კლასი რომლის საშუალებითაც გამოვითვლით სხვადასხვა დეტალს:
class Zodiacsign(object):
    # შევქმნათო კონსტრუქტორის მეთოდი
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    # ამ მეთოდის საშუალებით კი გამოვითვლით მომხმარებლის დაბადების წელს და ასაკს
        
    # def age(self):
    #     birthyear = int((self.date_of_birth.split("/")[2]))
    #     current_year = 2024
    #     if int(self.date_of_birth[0]) > 2 and int(self.date_of_birth[1]) > 22:
    #         return current_year - birthyear - 1
    #     else:
    #         return current_year - birthyear
    # ამ მეთოდის საშუალებით ადამიანის ასაკს გამოვითვლით (გასათვალისწინებელია ფაქტი, რომ თუ დღევანდელ თარიღამდე აქვს მომხმარებელს დაბადების დღე ჩვეულებრივ უნდა გამოვაკლოთ მიმდინარე წელს დაბადების წელი, ხოლო თუ ჯერ არ ჰქონია დაბადების დღე ერთით ნაკლები ასაკი უნდა ვაჩვენოთ)
    def age(self):
        birth_month, birth_day, birth_year = map(int, self.date_of_birth.split("/"))
        current_year = 2024
        current_month = 2
        current_day = 22

        birth_year = int(birth_year)
        if current_month < birth_month or (current_month == birth_month and current_day < birth_day):
            return current_year - birth_year - 1
        else:
            return current_year - birth_year


    # შემდეგ დაგვჭირდება რომ გავწეროთ მეთოდი იფ ელს ლოგიკური ოპერატორებით რომლის საშუალებითაც გავიგებთ რომელ ზოდიაქოს მიეკუვნება ესა თუ ის პიროვნება, ამისათვის ვიყენებთ ლოგიკურ ოპერატორებს -
    def zodiac_sign(self):
        # data = int(self.date_of_birth.split("/"))
        data = list(map(int, self.date_of_birth.split("/")))
        # print(data)
        if (data[0] == 3 and data[1] >= 21) or (data[0] == 4 and data[1] <= 20):
            return "Aries"
        elif (data[0] == 4 and data[1] >= 21) or (data[0] == 5 and data[1] <= 21):
            return "Taurus"
        elif (data[0] == 5 and data[1] >= 22) or (data[0] == 6 and data[1] <= 21):
            return "Gemini"
        elif (data[0] == 6 and data[1] >= 22) or (data[0] == 7 and data[1] <= 23):
            return "Cancer"
        elif (data[0] == 7 and data[1] >= 24) or (data[0] == 8 and data[1] <= 23):
            return "Leo"
        elif (data[0] == 8 and data[1] >= 24) or (data[0] == 9 and data[1] <= 23):
            return "Virgo"
        elif (data[0] == 9 and data[1] >= 24) or (data[0] == 10 and data[1] <= 23):
            return "Libra"
        elif (data[0] == 10 and data[1] >= 24) or (data[0] == 11 and data[1] <= 22):
            return "Scorpio"
        elif (data[0] == 11 and data[1] >= 23) or (data[0] == 12 and data[1] <= 21):
            return "Sagittarius"
        elif (data[0] == 12 and data[1] >= 22) or (data[0] == 1 and data[1] <= 20):
            return "Capricorn"
        elif (data[0] == 1 and data[1] >= 21) or (data[0] == 2 and data[1] <= 19):
            return "Aquarius"
        elif (data[0] == 2 and data[1] >= 20) or (data[0] == 3 and data[1] <= 20):
            return "Pisces"
        else:
            return "Please enter the date of birth in the following format: mm/dd/yyyy"
        
    # ახლა დაგვჭირდება მეთოდი რომლითაც შესაბამის ფოტოს დავუკავშირებთ ზოდიაქოს
    def zodiac_image(self):
        zodiac_sign = self.zodiac_sign()
        if zodiac_sign == "Aries":
            return "/static/images/Aries.jpg"
        if zodiac_sign == "Taurus":
            return "/static/images/Taurus.jpg"
        if zodiac_sign == "Gemini":
            return "/static/images/Gemini.jpg"
        if zodiac_sign == "Cancer":
            return "/static/images/Cancer.jpg"
        if zodiac_sign == "Leo":
            return "/static/images/Leo.jpg"
        if zodiac_sign == "Virgo":
            return "/static/images/Virgo.jpg"
        if zodiac_sign == "Libra":
            return "/static/images/Libra.jpg"
        if zodiac_sign == "Scorpio":
            return "/static/images/Scorpio.jpg"
        if zodiac_sign == "Sagittarius":
            return "/static/images/Sagittarius.jpg"
        if zodiac_sign == "Capricorn":
            return "/static/images/Capricorn.jpg"
        if zodiac_sign == "Aquarius":
            return "/static/images/Aquarius.jpg"
        if zodiac_sign == "Pisces":
            return "/static/images/Pisces.jpg"

    # შევქმნათ მისალმების ფუნქცია მომხმარებლისთვის
    def greet_person(self):
        age = self.age()
        zodiac_sign = self.zodiac_sign()
        return f"Hello, {self.first_name} {self.last_name}. You are {age} years old. Your zodiac sign is {zodiac_sign}"

# Flask-ის ფუნქცია @app.route('/', methods=['GET', 'POST']), რომელიც გვაძლევს საშუალებას ვთხოვოთ მომხმარებელს მოგვაწოდოს ძირითადი ინოფრორმაცია
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        date_of_birth = request.form['date_of_birth']
        # შევამოწმოთ დაბადების თარიღი შეჰყავს თუ არა მომხმარებელს სწორ ფორმატში, წინააღმდეგ შემთხვევაში გაეშვას ერორი მესიჯით: Please enter the date of birth in the following format: mm/dd/yyyy.
        if '/' not in date_of_birth:
            error_message = 'Please enter the date of birth in the following format: mm/dd/yyyy'
            return render_template('index.html', error_message=error_message)
        # თუ ყველაფერი სწორადაა შეყვანილი, განაგრძოს კოდმა მუშაობა და ამოხსნას რომელ ზოდიაქოს ეკუთვნის კონკრეტული პიროვნება და საბოლოოდ ფოტოსთან ერთად გვიჩვენოს პასუხი
        person = Zodiacsign(first_name, last_name, date_of_birth)
        greeting = person.greet_person()
        zodiac_image = person.zodiac_image()
        return render_template('index.html', greeting=greeting, zodiac_image=zodiac_image)
    return render_template('index.html', greeting=None, zodiac_image=None)




# შევამოწმოთ რომ სკრიპტი სრულდება პირდაპირ და გავუშვათ ფლესკის აპლიკაცია ვებ ბრაუზერში
if __name__ == '__main__':
     app.run(debug=True) 