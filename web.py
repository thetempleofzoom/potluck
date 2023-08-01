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

sl.subheader(":blue[Items already choped:]")
#sl.subheader("(delete permanently by ticking item)")
# add new list of items claimed and claimee
with open('brung.pkl', 'rb') as fp:
    brung = pickle.load(fp)
    if brung:
        for item in brung:
            tick = sl.checkbox(item[0] + " *bringing* " + item[1], key=item)
            if tick:
                brung.remove(item)
                with open('brung.pkl', 'wb') as pf:
                    pickle.dump(brung, pf)
                del sl.session_state[item]
                sl.experimental_rerun()
    else:
        sl.markdown(":red[No items choped yet]")

sl.subheader(":green[Chope things to bring:]")

if 'claimant' not in sl.session_state:
    sl.session_state.claimant = ''

sl.text_input("x", placeholder='enter your name', value='',
                         on_change=cleartext, key='name', label_visibility='collapsed')

claimant = sl.session_state.claimant

filepath = "tobrings.txt"
todos = readwrite.reading(filepath)
sl.markdown(":green[Items:]")

if not todos:
    sl.write(":red[No items - pls suggest some below]")
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
            sl.experimental_rerun()


sl.subheader("Or, please put additional items on the list:")

sl.text_input("x", placeholder="Enter a new potluck item",
              on_change=to_bring, key="new_todo" ,label_visibility='collapsed')








