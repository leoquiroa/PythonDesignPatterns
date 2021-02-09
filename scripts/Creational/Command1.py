import os

verbose = True

class RenameFile:
    def __init__(self, path_src, path_dest):
        self.src, self.dest = path_src, path_dest
    def execute(self):
        if verbose:
            print("[renaming '{}' to '{}']".format(self.src, self.dest))
        os.rename(self.src, self.dest)
    def undo(self):
        if verbose:
            print("[renaming '{}' back to '{}']".format(self.dest,self.src))
        os.rename(self.dest, self.src)

class CreateFile:
    def __init__(self, path, txt='hello world\n'):
        self.path, self.txt = path, txt
    def execute(self):
        if verbose:
            print("[creating file '{}']".format(self.path))
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)
    def undo(self):
        if verbose:
            print("deleting file '{}".format(self.path))
        os.remove(self.path)

class ReadFile:
    def __init__(self, path):
        self.path = path
    def execute(self):
        if verbose:
            print("[reading file '{}']".format(self.path))
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')
    
def main():
    orig_name, new_name = 'file1', 'file2'
    
    commands = []
    action1 = CreateFile(orig_name)
    commands.append(action1)
    action2 = ReadFile(orig_name)
    commands.append(action2)
    action3 = RenameFile(orig_name, new_name)
    commands.append(action3)
    [c.execute() for c in commands]
    
    answer = input('reverse the executed commands? [y/n] ')
    if answer not in 'yY':
        print("the result is {}".format(new_name))
        exit()

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            pass

if __name__ == "__main__":
    main()