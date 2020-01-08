

# 构建主流程/构建主类==================================================================
class Satoshi:
    def __init__(self, wait=1000):
        Bot.wait = wait
        self.bots = []
        
    def add(self,bot):
        self.bots.append(bot)
        
    def _prompt(self,s):
        print(s)
        print()
        
    def run(self):
        self._prompt("This is Satoshi dialog system. Let's talk.")
        for bot in self.bots:
            bot.run()
#构建父类======================================================
from time import sleep 
from termcolor import colored

class Bot:
    
    wait = 1
    
    def __init__(self,runtype='once'):
        self.runtype = runtype
        self.q = ''
        self.a = ''
        
    def _think(self, s):
        return s
    
    def _format(self, s):
        return colored(s, 'red')

    def _run_once(self):
        sleep(Bot.wait)
        print(self._format(self.q))
        self.a = input()
        sleep(Bot.wait)
        print(self._format(self._think(self.a)))

    def _run_looped(self):
        sleep(Bot.wait)
        print(self._format(self.q))
        while True:
            self.a = input()
            if self.a.lower() in ['q','x','quit','exit']:
                break
            sleep(Bot.wait)
            print(self._format(self._think(self.a)))
    
    def run(self):
        if self.runtype =='once':
            self._run_once()
        elif self.runtype =='looped':
            self._run_looped()
        

#构建子类======================================================
#子类1
class HelloBot(Bot):
    def __init__(self, runtype='once'):
        super().__init__(runtype)
        self.q = "Hi,what is your name?"
    
    def _think(self,s):
        return f"Hello {s}"
#子类2
class GreetingBot(Bot):
    def __init__(self, runtype='once'):
        super().__init__(runtype)
        self.q = "How are you today?"
    def _think(self,s):
        if 'good' in s.lower() or 'fine' in s.lower():
            return "I'm feeling good too"
        else:
            return "sorry to hear that"
#子类3
import random

class FavoriteColorBot(Bot):
    def __init__(self, runtype='once'):
        super().__init__(runtype)
        self.q = "What's your favorite color?"
    def _think(self,s):
        colors = ['red','orange','yellow','green','blue','indigo','purple']
        return f"You like {s.lower()}? My favorite color is {random.choice(colors)}"

#子类4
from simpleeval import simple_eval

class CalcBot(Bot):
    def __init__(self, runtype='once'):
        super().__init__(runtype)
        self.q = "通过最近的升级，我现在可以进行数学计算了，输入一些算数表达式试试吧。输入 'q' 'x' 'quit' 或 'exit'可退出."

    def _think(self, s):
        result = simple_eval(s)
        return f"Done. Result = {result}"

    def run(self):
        sleep(Bot.wait)
        print(self._format(self.q))
        while True:
            self.a = input()
            if self.a.lower() in ['q','x','quit','exit']:
                break
            else:
                sleep(Bot.wait)
                print(self._format(self._think(self.a)))




#初始化=================================
satoshi = Satoshi(1)
satoshi.add(HelloBot())
satoshi.add(GreetingBot())
satoshi.add(FavoriteColorBot())
satoshi.add(CalcBot('looped'))
satoshi.run()