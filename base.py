import tkinter
import pandas as pd
from tkinter import messagebox
from score_file import SCORE


window = tkinter.Tk()
window.minsize(230, 230)
window.title('quiz game')
window.config(bg='black')



entry_label = tkinter.Label(text='GUESS THE STATES OF INDIA ONE BY ONE', font=("Helvetica",9))
entry_label.grid(row=0, column=0, columnspan=2, pady=5)

entry = tkinter.Entry(width=20)
entry.grid(row=2, column=0, columnspan=2, pady=5)

score_var = SCORE()
score_var.creator()



# DATA FORMATION USING CSV
states_data = pd.read_csv('states_data.csv')
states_list = states_data['state_names'].to_list()


# PREREQUISITES FOR THE LOGIC
bools = [True for i in range(29)]
show_states = []


def receive(event=None):

    # CHECKING GAME STATUS
    def check_status():
            if True not in bools:
                window.config(bg='purple')
                messagebox.showinfo(title='congrats'.upper(), message=' you won the game'.upper())
                window.destroy()


    # ACCEPTING THE INPUT
    guessed_state = entry.get().lower().strip()

    #LOGICS
    if guessed_state == 'quit':
        window.destroy()

    elif guessed_state in states_list:
        show_states.append(guessed_state)
        entry.delete(0, len(entry.get()))


        guessed_state_index = states_list.index(guessed_state)
        if bools[guessed_state_index]:
            bools[guessed_state_index] = False
            score_var.score_updater()

            window.config(bg='green')

            true_label = tkinter.Label(text='True', font=("Helvetica", 9))
            true_label.grid(row=3, column=0, columnspan=2, pady=5)

            check_status()

            window.after(2000, lambda :window.config(bg='black'))
            true_label.after(2000, lambda :true_label.destroy())



        else:
            already_label = tkinter.Label(text='this state is already entered'.upper())
            already_label.grid(row=4, column=0, columnspan=2, pady=5)

            window.after(2000, lambda :already_label.destroy())



    elif not guessed_state:
        alt_text_label = tkinter.Label(text='enter the state name'.upper(),font=("Helvetica",9))
        alt_text_label.grid(row=5, column=0, columnspan=2, pady=5)

        alt_text_label.after(2000, lambda:alt_text_label.destroy())


    else:
        entry.delete(0, len(entry.get()))
        window.config(bg='red')
        false_label= tkinter.Label(text='no match found or check the spelling'.upper(),font=("Helvetica",9))
        false_label.grid(row=6, column=0, columnspan=2, pady=5)

        window.after(2000,lambda : window.config(bg='black'))
        false_label.after(2000, lambda :false_label.destroy())



submit_button = tkinter.Button(text='SUBMIT', command=receive,font=("Helvetica",9))
submit_button.grid(row=7, column=0, columnspan=2, pady=5)
window.bind('<Return>', receive)

# GUESS FUNCTION
def guess_func():
    unique_states = set(show_states)
    final_states = list(unique_states)
    for states in final_states:
        print(f'{final_states.index(states) + 1} {states.upper()}')
    print(f'number of guessed states - {len(final_states)} ')
    messagebox.showinfo(title='INFO', message='CHECK THE CONSOLE')

# GUESS BUTTON

guessed_states_button = tkinter.Button(text='GUESSED STATES',
                                       command= guess_func
                                       ,font=("Helvetica",9))
guessed_states_button.grid(row=8, column=0, columnspan=2, pady=5)
quit_label = tkinter.Label(text='TYPE"quit"TO QUIT GAME',font=("Helvetica",8))
quit_label.grid(row=9, column=0, columnspan=2, pady=5)

window.mainloop()
