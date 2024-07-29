import threading
import sys
from queue import Queue
from attr import attrs, attrib


class ThreadBot(threading.Thread):
    def __init__(self, bot_id=0):
        self.bot_id = bot_id
        super().__init__(target=self.manage_table)
        self.cutlery = Cutlery(knives=0, forks=0)
        self.tasks = Queue()

    def manage_table(self):
        n_prepare = 0
        n_clear_table = 0
        while True:
            task = self.tasks.get()
            if task == 'prepare table':
                n_prepare += 1
                print("==" * 20)
                print(f"BOT ID {self.bot_id} WORKING ON:")
                print("==" * 20)
                print(f"bot id {self.bot_id} prepare table... go 4 forks and 4 knives to table :", n_prepare)
                kitchen.give(to=self.cutlery, knives=4, forks=4)
            elif task == 'clear table':
                n_clear_table +=1
                print("==" * 20)
                print(f"BOT ID {self.bot_id} WORKING ON:")
                print("==" * 20)
                print(f"bot id {self.bot_id} clear table... return 4 forks and 4 knives from table", n_clear_table)
                self.cutlery.give(to=kitchen, knives=4, forks=4)
            elif task == 'shutdown':
                return


@attrs
class Cutlery:
    knives = attrib(default=0)
    forks = attrib(default=0)

    def give(self, to: 'Cutlery', knives=0, forks=0):
        self.change(-knives, -forks)
        to.change(knives, forks)

    def change(self, knives, forks):
        self.knives += knives
        self.forks += forks


kitchen = Cutlery(knives=100, forks=100)
bots = [ThreadBot(bot_id=i) for i in range(10)]


for bot in bots:
    for i in range(int(sys.argv[1])):
        bot.tasks.put('prepare table')
        bot.tasks.put('clear table')
    bot.tasks.put('shutdown')


print('Kitchen inventory before service:', kitchen)
for bot in bots:
    bot.start()
for bot in bots:
    bot.join()
print('Kitchen inventory after service:', kitchen)