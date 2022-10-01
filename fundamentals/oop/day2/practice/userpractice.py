class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member, gold_card_points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

def user_info_dump(self):
    print(self.first_name,)
    print(self.last_name,)
    print(self.email,)
    print(self.age,)
    print(self.is_rewards_member,)
    print(self.gold_card_points,)

def enroll_user(self):
    if self.is_rewards_member == True:
        print("Member already enrolled")
    else:
        self.is_rewards_member = True
        self.gold_card_points = 200
        print("Member has been enrolled, point balance has been set to 200")
    return self

def spend_points(self,points):
    if self.gold_card_points >= points:
        self.gold_card_points = self.gold_card_points-points
        print(f"Your new point balance is",self.gold_card_points)
    else:
        print(f"Insufficient point balance, you only have",self.gold_card_points)
    return self

user_1 = User("Anthony", "Marsee", "anthonymarsee@gmail.com", 22,False,0)
user_2 = User("Kevin", "Eleven", "kevineleven@gmail.com", 20,False,0)
user_3 = User("Nick", "Olodean", "nickolodean@gmail.com", 24,False,0)

user_1user_info_dump()