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

sl.title("Welcome to Wei's potluck!")

sl.subheader("Items already claimed:")
# add new list of items claimed and claimee
with open('brung.pkl', 'rb') as fp:
    try:
        brung = pickle.load(fp)
        for item in brung:
            sl.write(item[0] + " :red[bringing] " + item[1])
    except EOFError:
        sl.write(":red[No items claimed yet]")
        brung = []

sl.subheader("Please enter new items to bring:")
filepath = "tobrings.txt"
todos = defs.reading(filepath)

sl.text_input("", placeholder="Enter a new potluck item",
              on_change=to_bring, key="new_todo")

sl.subheader("Or, claim items to bring:")
claimant = ""
claimant = sl.text_input("", placeholder='enter your name', key='name')

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





