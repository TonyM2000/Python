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

def spend_points(self,points):
    if self.gold_card_points >= points:
        self.gold_card_points = self.gold_card_points-points
        print(f"Your new point balance is",self.gold_card_points)
    else:
        print(f"Insufficient point balance, you only have",self.gold_card_points)

user_Anthony = User("Anthony", "Marsee", "anthonymarsee@gmail.com", 22,False,0)
user_Kevin = User("Kevin", "Eleven", "kevineleven@gmail.com", 20,False,0)
user_Nick = User("Nick", "Olodean", "nickolodean@gmail.com", 24,False,0)

user_info_dump(user_Anthony)

enroll_user(user_Anthony)

user_info_dump(user_Anthony)

user_info_dump(user_Nick)

user_info_dump(user_Kevin)

spend_points(user_Anthony,50)

enroll_user(user_Kevin)

spend_points(user_Kevin,80)

user_info_dump(user_Anthony)

user_info_dump(user_Nick)

enroll_user(user_Anthony)

spend_points(user_Nick,40)