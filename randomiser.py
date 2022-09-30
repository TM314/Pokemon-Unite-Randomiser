from tkinter import *
from tkinter import ttk, font
import random
import numpy as np
from prettytable import PrettyTable, ALL

def load_data():
    mons = np.genfromtxt("mons.txt", delimiter=",", dtype="str", skip_header=1)
    battle_items = np.genfromtxt("battle_items.txt", delimiter=",", dtype="str", skip_header=1)
    held_items = np.genfromtxt("held_items.txt", delimiter=",", dtype="str", skip_header=1)
    return(mons, battle_items, held_items)

def randomise(mons, battle_items, held_items, team_size=1):
    res = []
    counter = 0

    while counter < team_size:
        selection = []

        mon_num = random.randint(0,len(mons)-1)
        mon = mons[mon_num]


        # print(selection)

        if mon[0] == "mew":
            selection.append(mon[0])
            # print("MEW")
            moveset1_nums = np.random.permutation(3)
            moveset2_nums = np.random.permutation(3)
            temp = []
            for i in zip(moveset1_nums, moveset2_nums):
                temp.append((mon[2].split("/")[i[0]], mon[4].split("/")[i[1]]))
            selection.append(temp)

            can_crit = ["no/no/no"]
        elif mon[0] == "scyther/scizor":
            # print('SCYTHER/SCIZOR')
            moveset_flip1 = random.randint(0,1)
            moveset_flip2 = random.randint(0,1)

            # print(mon[0].split("/"))
            selection.append(mon[0].split("/")[moveset_flip1])

            move1 = mon[2].split("/")[moveset_flip1]
            move2 = mon[4].split("/")[moveset_flip2]

            selection.append(move1)
            selection.append(move2)

            can_crit = []
            can_crit.append(mon[3].split("/")[moveset_flip1]+"/"+mon[5].split("/")[moveset_flip2])
        else:
            selection.append(mon[0])

            moveset_flip1 = random.randint(0,1)
            moveset_flip2 = random.randint(0,1)

            move1 = mon[2].split("/")[moveset_flip1]
            move2 = mon[4].split("/")[moveset_flip2]

            selection.append(move1)
            selection.append(move2)

            can_crit = []
            can_crit.append(mon[3].split("/")[moveset_flip1]+"/"+mon[5].split("/")[moveset_flip2])


        if mon[1] == "physical":
            phys_spec = 0
        else:
            phys_spec = 1

        possible_held_items = []

        for row in held_items:
            if row[1].split("/")[phys_spec] == "yes":
                if row[0] == "scope_lens":
                    if "yes" in can_crit[0] or mon[-1] == "yes":
                        possible_held_items.append(row[0])
                    else:
                        None
                else:
                    possible_held_items.append(row[0])

        # print(possible_held_items)

        held_item_nums = [random.randint(0,len(possible_held_items)-1)]
        # print(possible_held_items[held_item_nums[-1]])
        while len(held_item_nums) < 3:
            temp = random.randint(0,len(possible_held_items)-1)
            if temp in held_item_nums:
                None
            else:
                held_item_nums.append(temp)
            # print(possible_held_items[held_item_nums[-1]])


        # print(held_item_nums)

        for i in held_item_nums:
            selection.append(possible_held_items[i])

        # print(selection)

        selection.append(battle_items[random.randint(0,len(battle_items)-1)])

        res.append(selection)
        # print(selection)
        # print(mons[:,0])
        mons = np.delete(mons, mon_num, axis=0)
        # print(mons[:,0])
        counter += 1

    lanes = np.random.permutation(["jungler","top","top","bot","bot"])
    if team_size == 5:
        for i in range(len(res)):
            res[i].append(lanes[i])

    return(res)

def present_nicely(data):
    tab = PrettyTable()

    tab.field_names = ["Pokemon", "Lane", "Moves", "Held Items", "Battle Items"]

    for pokemon in data:
        if pokemon[0] == 'mew':
            # print(pokemon[1][0][0])
            row = [pokemon[0].replace('_',' ').title(), pokemon[6].replace('_',' ').title(), '('+pokemon[1][0][0].replace('_',' ').title()+', '+pokemon[1][0][1].replace('_',' ').title()+')\n'+'('+pokemon[1][1][0].replace('_',' ').title()+', '+pokemon[1][1][1].replace('_',' ').title()+')\n'+'('+pokemon[1][2][0].replace('_',' ').title()+', '+pokemon[1][2][1].replace('_',' ').title()+')', pokemon[2].replace('_',' ').title()+'\n'+pokemon[3].replace('_',' ').title()+'\n'+pokemon[4].replace('_',' ').title(), pokemon[5].replace('_',' ').title()]
        else:
            row = [pokemon[0].replace('_',' ').title(), pokemon[7].replace('_',' ').title(), pokemon[1].replace('_',' ').title()+'\n'+pokemon[2].replace('_',' ').title(), pokemon[3].replace('_',' ').title()+'\n'+pokemon[4].replace('_',' ').title()+'\n'+pokemon[5].replace('_',' ').title(), pokemon[6].replace('_',' ').title()]
        tab.add_row(row)

    tab.hrules = ALL

    return(tab)

def create_table(data):
    res = []

    for pokemon in data:
        if pokemon[0] == 'mew':
            # print(pokemon[1][0][0])
            row = [pokemon[0].replace('_',' ').title(), pokemon[6].replace('_',' ').title(), '('+pokemon[1][0][0].replace('_',' ').title()+', '+pokemon[1][0][1].replace('_',' ').title()+')\n'+'('+pokemon[1][1][0].replace('_',' ').title()+', '+pokemon[1][1][1].replace('_',' ').title()+')\n'+'('+pokemon[1][2][0].replace('_',' ').title()+', '+pokemon[1][2][1].replace('_',' ').title()+')', pokemon[2].replace('_',' ').title()+'\n'+pokemon[3].replace('_',' ').title()+'\n'+pokemon[4].replace('_',' ').title(), pokemon[5].replace('_',' ').title()]
        else:
            row = [pokemon[0].replace('_',' ').title(), pokemon[7].replace('_',' ').title(), pokemon[1].replace('_',' ').title()+'\n'+pokemon[2].replace('_',' ').title(), pokemon[3].replace('_',' ').title()+'\n'+pokemon[4].replace('_',' ').title()+'\n'+pokemon[5].replace('_',' ').title(), pokemon[6].replace('_',' ').title()]
        res.append(row)

    print(res)
    return(res)

def run_program():
    mons, battle_items, held_items = load_data()
    team = randomise(mons, battle_items, held_items, 5)
    # print(team)
    # table = present_nicely(team)
    table = present_nicely(team)

    newwindow = Toplevel(win)

    newwindow.title('Randomised Team')

    newwindow.geometry("1100x600")

    Label(newwindow, text = table.get_string(sortby='Lane', reversesort=True)).pack()


    # cols = ("Pokemon", "Lane", "Moves", "Held Items", "Battle Items")

    # tree = ttk.Treeview(win, column=cols, show="headings")
    # for ind, item in enumerate(cols):
    #     tree.column("# " + str(ind), anchor=CENTER)
    #     tree.heading("# " + str(ind), text=item)
    # for row in table:
    #     tree.insert('', 'end', text="1", values=row)
    #
    # tree.pack()

    # print(table.get_string(sortby='Lane', reversesort=True))
    # return(table)


# print(table.get_string(sortby='Lane', reversesort=True))

win = Tk()
win.title('Pokemon Unite Team Randomiser')
win.geometry("350x50")

style = ttk.Style()
style.theme_use("clam")

win.defaultFont = font.nametofont("TkDefaultFont")

win.defaultFont.configure(family="DejaVu Sans Mono", size=15)

btn = Button(win, text='Randomise!', command=run_program)
btn.grid(row=0, column=0, padx=107, pady=5)

win.mainloop()
