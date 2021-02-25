from cowpy import cow

# styles
def dots_style(msg):
    msg = msg.capitalize()
    msg = '.' * 10 + msg + '.' * 10
    return msg
def admire_style(msg):
    msg = msg.upper()
    return '!'.join(msg)
def cow_style(msg):
    msg = cow.milk_random_cow(msg)
    return msg
#####################################################
def main():
    msg = 'happy coding'
    style_list = [dots_style, admire_style, cow_style]
    [generate_banner(msg, s) for s in style_list]
    
def generate_banner(msg, style=dots_style):
    print('-- start of banner --')
    print(style(msg))
    print('-- end of banner --\n\n')

if __name__ == '__main__':
    main()