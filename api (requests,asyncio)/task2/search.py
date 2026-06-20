import requests
import threading
import queue


class UserFinder:
    def __init__(self):
        self.q = queue.Queue()

        self.all_users = 0
        self.all_true = 0

    def new_thread(self, obj):
        thread = threading.Thread(
            target=self.create_users,
            daemon=True,
            args=(obj,)
        )

        thread.start()

    def create_users(self, obj):
        while self.all_users != int(obj.quantity.get()):
            self.one_page(obj)

    def one_page(self, obj):
        url = f"https://randomuser.me/api/?results={int(obj.quantity.get())}"
        response = requests.get(url).json()
        for i in response['results']:
            if self.all_users == int(obj.quantity.get()):
                break
            self.check_age(
                one_obj=i,
                age_min=int(obj.age_min.get()),
                age_max=int(obj.age_max.get())
            )

    def check_age(self, one_obj, age_min, age_max):
        age = int(one_obj['dob']['age'])
        if age_max >= age >= age_min:
            self.all_users += 1
            self.q.put(('user', self.all_users))
        else:
            self.all_true += 1
            self.q.put(('all_true', self.all_true))




factory = UserFinder()
