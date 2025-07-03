# simple.py

is_cold = True
age = 30
def add(x, y):
    # breakpoint()  # This will start the debugger when the function is called
    return x + y

# Debugging using breakpoint() and pdb
adding = add('hello', ' world')
print('DEBUG: adding =', adding)                    # hello world
print('DEBUG with repr: adding =', repr(adding))    # 'hello world'
# repr() shows you an accurate representation of a value. Not the nice printing output.

"""pdb commands
(Pdb) h(elp)          # Get help on commands
(Pdb) q(uit)          # Quit the debugger
(Pdb) p(rit) var      # Print variable value
(Pdb) pp(var)         # Pretty print variable value
(Pdb) n(ext)          # Execute next line, but don't step into functions
(Pdb) r(eturn)        # Continue execution until the current function returns
(Pdb) c(ontinue)      # Continue execution until the next breakpoint
(Pdb) l(ist)          # List source code around the current line
(Pdb) w(here)         # Print the current stack trace
(Pdb) d(own)          # Move down one level in the stack trace
(Pdb) u(p)            # Move up one level in the stack trace; max up is the breakpoint() location
(Pdb) b(reak) loc     # Set a breakpoint at the specified location
(Pdb) s(tep)          # Step into the next line of code
(Pdb) c(ontinue)      # Continue execution until the next breakpoint
(Pdb) l(ist)          # List source code around the current line
(Pdb) a(rgs)          # Print the arguments of the current function
(Pdb) !statement      # Execute a statement in the current context  

# To run
# 1. Either set a breakpoint in the code using `breakpoint()` or 
# 2. run the script with pdb:
$ python3 -m pdb someprogram.py    
"""