"""
Stream lit GUI for hosting TerminalMusic
"""

# Imports
import os
import functools
import streamlit as st
import json

from TerminalMusic import *

# Main Vars
config = json.load(open('./StreamLitGUI/UIConfig.json', 'r'))

# Main Functions
def main():
    # Create Sidebar
    selected_box = st.sidebar.selectbox(
    'Choose one of the following',
        tuple(
            [config['PROJECT_NAME']] + 
            config['PROJECT_MODES']
        )
    )
    
    if selected_box == config['PROJECT_NAME']:
        HomePage()
    else:
        correspondingFuncName = selected_box.replace(' ', '_').lower()
        if correspondingFuncName in globals().keys():
            globals()[correspondingFuncName]()
 

def HomePage():
    st.title(config['PROJECT_NAME'])
    st.markdown('Github Repo: ' + "[" + config['PROJECT_LINK'] + "](" + config['PROJECT_LINK'] + ")")
    st.markdown(config['PROJECT_DESC'])

    # st.write(open(config['PROJECT_README'], 'r').read())

#############################################################################################################################
# Repo Based Vars

# Util Vars
TERMINAL_HISTORY_MAX_LENGTH = 10
TERMINAL_HISTORY = []

# Util Functions

# Main Functions
# Print Functions
def PrintObj_Terminal(x, overwrite=False):
    '''
    Prints data to terminal.
    '''
    if overwrite:
        print("\r" + " "*100 + "\r", end="")
        print(str(x), end="")
    else:
        print(x)

def PrintObj_StObject(x, st_obj=None, overwrite=False):
    '''
    Prints data to Streamlit object.
    '''
    global TERMINAL_HISTORY_MAX_LENGTH
    global TERMINAL_HISTORY
 
    if not overwrite:
        if len(TERMINAL_HISTORY) >= TERMINAL_HISTORY_MAX_LENGTH:
            TERMINAL_HISTORY.pop(0)
        TERMINAL_HISTORY.append(x)
        x = "\n".join(TERMINAL_HISTORY)

    st_obj.markdown("```\n" + x + "\n```")

# UI Functions


# Repo Based Functions
def terminal_waves():
    global TERMINAL_HISTORY_MAX_LENGTH
    global TERMINAL_HISTORY
    # Title
    st.header("Terminal Waves")

    # Prereq Loaders

    # Load Inputs
    TERMINAL_HISTORY_MAX_LENGTH = st.sidebar.number_input("Terminal Height", min_value=1, max_value=15)
    USERINPUT_WaveName = st.selectbox("Select Wave", TERMINAL_WAVES.keys())
    USERINPUT_c = st.text_input("Select Display Char", "*")
    USERINPUT_delay = st.slider("Select Delay", 0.0, 1.0, 0.1, 0.01)
    USERINPUT_Overwrite = st.checkbox("Overwrite")

    # Process Inputs
    TERMINAL_HISTORY = []
    WaveFunc = TERMINAL_WAVES[USERINPUT_WaveName]

    # Display Outputs
    TerminalObj = st.empty()
    PrintObj = functools.partial(PrintObj_StObject, st_obj=TerminalObj, overwrite=USERINPUT_Overwrite)
    WaveFunc(PrintObj, USERINPUT_c, USERINPUT_delay, -1, (1, 10))
    
#############################################################################################################################
# Driver Code
if __name__ == "__main__":
    main()