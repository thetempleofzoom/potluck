import streamlit as sl
import defs
import pickle

def to_bring():
    if sl.session_state["new_todo"]:
        todo = sl.session_state["new_todo"]
        todos.append(todo + "\n")
        defs.writing(todos, filepath)
        sl.session_state["new_todo"] = ""

def cleartext():
    #global claimant
    if sl.session_state['name']:
        claimant = sl.session_state['name']
        print(claimant)
        sl.session_state['name']=""

sl.title("Welcome to shabu potluck!")

sl.subheader("Items already choped:")
# add new list of items claimed and claimee
with open('brung.pkl', 'rb') as fp:
    try:
        brung = pickle.load(fp)
        print(brung[0])
        for item in brung:
            tick = sl.checkbox(item[0] + " *bringing* " + item[1], key=item)
            if tick:
                brung.remove(item)
                with open('brung.pkl', 'wb') as pf:
                    pickle.dump(brung, pf)
                del sl.session_state[item]
                sl.experimental_rerun()
    except IndexError or EOFError:
        sl.write(":red[No items claimed yet]")
        brung = []

sl.subheader("Chope things to bring:")
claimant = ""
claimant = sl.text_input("", placeholder='enter your name', key='name')

filepath = "tobrings.txt"
todos = defs.reading(filepath)

for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=index)
    if claimant and checkbox:
        with open("brung.pkl", 'wb') as fp:
            brung.append((claimant, todos[index]))
            pickle.dump(brung, fp)
        # delete item from list
        todos.pop(index)
        defs.writing(todos, filepath)
        del sl.session_state[index]
        sl.experimental_rerun()


sl.subheader("Or, please suggest additional items to bring:")

sl.text_input("", placeholder="Enter a new potluck item",
              on_change=to_bring, key="new_todo")






