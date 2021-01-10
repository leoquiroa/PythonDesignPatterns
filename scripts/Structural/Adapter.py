class Computer:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'the {} computer'.format(self.name)
    def execute(self):
        return 'executes a program'
    
class Synthesizer:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'the {} synthesizer'.format(self.name)
    def play(self):
        return 'is playing an electronic song'

class Human:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return '{} the human'.format(self.name)
    def speak(self):
        return 'says hello'

class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)
    
    def __str__(self):
        return str(self.obj)
    
def main():
    computer = Computer('Asus')
    synth = Synthesizer('moog')
    human = Human('Bob')

    objects = [computer]
    adapter_for_synth = Adapter(synth, dict(execute=synth.play))
    objects.append(adapter_for_synth)
    adapter_for_human = Adapter(human, dict(execute=human.speak))
    objects.append(adapter_for_human)
    for i in objects:
        print('{} {}'.format(str(i), i.execute()))

if __name__ == "__main__":
    main()