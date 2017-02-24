import sys

# saveToInteractive works by allowing the user to move objects from one environment to the global interactive session.  
# This has been tested and works within the ipython debugger.  the dic argument takes a dictionary containing the 
# name and object itself e.g. {'foo': bar}; max_frames is the number of frames to search through...


def saveToInteractive(dic, max_frames = 20):
    n = 0
    # Walk up the stack looking for '__name__'
    # with a value of '__main__' in frame globals
    for n in range(max_frames):
        cur_frame = sys._getframe(n)
        name = cur_frame.f_globals.get('__name__')
        if name == '__main__':
            # Yay - we're in the stack frame of the interactive interpreter!
            # So we update its frame globals with the dict containing our data
            cur_frame.f_globals.update(dic)
            break