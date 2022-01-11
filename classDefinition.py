class Car(object):
    def _init_(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def start(self):
        print('started')
    def stop(self):
        print('stopped')
    def accelerate(self):
        print('accelerating')
    def change_gear(self, gear_type):
        print('gear changed')

audi = Car()
print(audi.start())