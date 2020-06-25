# python3
# written by zibo

import random
import tkinter
import tkinter.font as tkFont

query = []
result = []

char_root_dict = {}
for line in open('char_root.txt'):
    char, char_key = line.split()
    char_root_dict[char] = char_key

full_code_dict = {}
level1_dict = {}
level2_dict = {}
level3_dict = {}

for line in open('code_table.txt'):
    hex_code, character, *codes = line.split()
    full_code_dict[character] = codes
    for i in codes:
        if len(i) == 1: level1_dict[character] = i
        elif len(i) == 2: level2_dict[character] = i
        elif len(i) == 3: level3_dict[character] = i

keyname_dict = {}
keyboard_dict = {}

for i in list('金人月白禾言立水火之工木大土王目日口田山已子女又纟'):
    keyname_dict[i] = full_code_dict[i]

for i in list('文方广六辛门小米儿夕八用乃手斤竹彳七戈丁西犬古石三厂士二干十寸匸豕'
              +'雨一五卜上止虫川甲四皿车力幺匕弓巴马刀九臼孑了也耳巳己由贝几廿戋'):
    keyboard_dict[i] = full_code_dict[i]


def call_charroot():
    e.delete(0, tkinter.END)
    query = []
    result = []
    for _ in range(100):
        query.append(random.choice(list(char_root_dict.keys())))
        result.append(char_root_dict[query[-1]])
    t.delete(0.0, tkinter.END)
    t.insert(0.0, ''.join(query))

    def entry_action(event):
        if event.char == result[0]:
            del(query[0])
            t.delete(0.0, tkinter.END)
            t.insert(0.0, ''.join(query))
            del(result[0])
            lb_hint['text'] = ''
        else: lb_hint['text'] = 'hint: ' + result[0]
        e.delete(0, tkinter.END)
    e.bind('<Key>', entry_action)

def call_level1():
    e.delete(0, tkinter.END)
    query = []
    result = []
    for _ in range(100):
        query.append(random.choice(list(level1_dict.keys())))
        result.append(full_code_dict[query[-1]])
    t.delete(0.0, tkinter.END)
    t.insert(0.0, ''.join(query))

    def entry_action(event):
        if event.char == ' ':
            if e.get().strip() in result[0]:
                del(query[0])
                t.delete(0.0, tkinter.END)
                t.insert(0.0, ''.join(query))
                del(result[0])
                lb_hint['text'] = ''
            else: lb_hint['text'] = 'hint: ' + ' '.join(result[0])
            e.delete(0, tkinter.END)
    e.bind('<Key>', entry_action)

def call_level2():
    e.delete(0, tkinter.END)
    query = []
    result = []
    for _ in range(100):
        query.append(random.choice(list(level2_dict.keys())))
        result.append(full_code_dict[query[-1]])
    t.delete(0.0, tkinter.END)
    t.insert(0.0, ''.join(query))

    def entry_action(event):
        if event.char == ' ':
            if e.get().strip() in result[0]:
                del(query[0])
                t.delete(0.0, tkinter.END)
                t.insert(0.0, ''.join(query))
                del(result[0])
                lb_hint['text'] = ''
            else: lb_hint['text'] = 'hint: ' + ' '.join(result[0])
            e.delete(0, tkinter.END)
    e.bind('<Key>', entry_action)

def call_level3():
    e.delete(0, tkinter.END)
    query = []
    result = []
    for _ in range(100):
        query.append(random.choice(list(level3_dict.keys())))
        result.append(full_code_dict[query[-1]])
    t.delete(0.0, tkinter.END)
    t.insert(0.0, ''.join(query))

    def entry_action(event):
        if event.char == ' ':
            if e.get().strip() in result[0]:
                del(query[0])
                t.delete(0.0, tkinter.END)
                t.insert(0.0, ''.join(query))
                del(result[0])
                lb_hint['text'] = ''
            else: lb_hint['text'] = 'hint: ' + ' '.join(result[0])
            e.delete(0, tkinter.END)
    e.bind('<Key>', entry_action)

def call_keyname():
    e.delete(0, tkinter.END)
    query = list(keyname_dict.keys())
    result = []
    random.shuffle(query)
    for i in query:
        result.append(full_code_dict[i])
    t.delete(0.0, tkinter.END)
    t.insert(0.0, ''.join(query))

    def entry_action(event):
        if event.char == ' ':
            if e.get().strip() in result[0]:
                del (query[0])
                t.delete(0.0, tkinter.END)
                t.insert(0.0, ''.join(query))
                del (result[0])
                lb_hint['text'] = ''
            else:
                lb_hint['text'] = 'hint: ' + ' '.join(result[0])
            e.delete(0, tkinter.END)

    e.bind('<Key>', entry_action)

def call_keyboard():
    e.delete(0, tkinter.END)
    query = list(keyboard_dict.keys())
    result = []
    random.shuffle(query)
    for i in query:
        result.append(full_code_dict[i])
    t.delete(0.0, tkinter.END)
    t.insert(0.0, ''.join(query))

    def entry_action(event):
        if event.char == ' ':
            if e.get().strip() in result[0]:
                del (query[0])
                t.delete(0.0, tkinter.END)
                t.insert(0.0, ''.join(query))
                del (result[0])
                lb_hint['text'] = ''
            else:
                lb_hint['text'] = 'hint: ' + ' '.join(result[0])
            e.delete(0, tkinter.END)

    e.bind('<Key>', entry_action)

def call_random():
    e.delete(0, tkinter.END)
    query = []
    result = []
    for _ in range(100):
        query.append(random.choice(list(full_code_dict.keys())))
        result.append(full_code_dict[query[-1]])
    t.delete(0.0, tkinter.END)
    t.insert(0.0, ''.join(query))

    def entry_action(event):
        if event.char == ' ':
            if e.get().strip() in result[0]:
                del(query[0])
                t.delete(0.0, tkinter.END)
                t.insert(0.0, ''.join(query))
                del(result[0])
                lb_hint['text'] = ''
            else: lb_hint['text'] = 'hint: ' + ' '.join(result[0])
            e.delete(0, tkinter.END)
    e.bind('<Key>', entry_action)


if __name__ == '__main__':
    root=tkinter.Tk()
    root.title('五笔练习1.0')
    t=tkinter.Text(root, font=tkFont.Font(size=20), height=6, width=30)

    tkinter.Button(root,text='字根练习',command=call_charroot).pack(fill=tkinter.X)
    tkinter.Button(root,text='一级简码',command=call_level1).pack(fill=tkinter.X)
    tkinter.Button(root,text='二级简码',command=call_level2).pack(fill=tkinter.X)
    tkinter.Button(root,text='三级简码',command=call_level3).pack(fill=tkinter.X)
    tkinter.Button(root,text='键名汉字',command=call_keyname).pack(fill=tkinter.X)
    tkinter.Button(root,text='键面汉字',command=call_keyboard).pack(fill=tkinter.X)
    tkinter.Button(root,text='随机汉字',command=call_random).pack(fill=tkinter.X)

    lb_hint = tkinter.Label(root)
    e = tkinter.Entry(root)

    t.pack()
    e.pack()
    lb_hint.pack()

    root.mainloop()
