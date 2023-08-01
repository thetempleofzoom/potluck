import streamlit as sl
import readwrite
import pickle

def to_bring():
    if sl.session_state["new_todo"]:
        todo = sl.session_state["new_todo"]
        todos.append(todo + "\n")
        readwrite.writing(todos, filepath)
        sl.session_state["new_todo"] = ""

def cleartext():
    sl.session_state.claimant = sl.session_state.name
    sl.session_state.name = ""


sl.title("Welcome to shabu potluck!")

sl.subheader("Items already choped:")
sl.subheader("(delete permanently by ticking item)")
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

sl.subheader("Chope things to bring by entering name and ticking item:")

if 'claimant' not in sl.session_state:
    sl.session_state.claimant = ''

sl.text_input("x", placeholder='enter your name', value='',
                         on_change=cleartext, key='name', label_visibility='collapsed')

claimant = sl.session_state.claimant

filepath = "tobrings.txt"
todos = readwrite.reading(filepath)
if len(todos)==1 and todos[0]=="\n":
    todos=[]
else:
    for index, todo in enumerate(todos):
        checkbox = sl.checkbox(todo, key=index)
        if claimant and checkbox:
            with open("brung.pkl", 'wb') as fp:
                brung.append((claimant, todos[index]))
                pickle.dump(brung, fp)
            # delete item from list
            todos.pop(index)
            readwrite.writing(todos, filepath)
            del sl.session_state[index]
            #can't delete name in input text field??
            del sl.session_state.name
            sl.experimental_rerun()


sl.subheader("Or, please suggest additional items to bring:")

sl.text_input("x", placeholder="Enter a new potluck item",
              on_change=to_bring, key="new_todo" ,label_visibility='collapsed')






