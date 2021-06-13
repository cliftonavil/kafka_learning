from faker import Faker

fake = Faker()

def get_registed_user():
    return {
        'name':fake.name(),
        'address':fake.address(),
        'created_on':fake.year(),
    }

if __name__ == '__main__':
    print(get_registed_user())