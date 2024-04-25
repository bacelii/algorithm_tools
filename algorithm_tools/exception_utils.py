"""
Tutorial: https://realpython.com/python-exceptions/

List of possible exceptions

AssertionError: Raised when assert statement fails
AttributeError: Raised when attribute assignment or reference fails
EOFError: Raised when the input() function hits end-of-file condition
FloatingPointError: Raised when a floating point operation fails
GeneratorExit: Raised when a generator's close() method is called
ImportError: Raised when the imported module is not found
IndexError: Raised when index of a sequence is out of range
KeyError: Raised when a key is not found in a dictionary
KeyboardInterrupt: Raised when the user hits interrupt key (CTRL+C or Delete)
MemoryError: Raised when an operation runs out of memory
NameError: Raised when a variable is not found in local or global scope
NotImplementedError: Raised by abstract methods
OSError: Raised when system operation causes system related error
OverflowError: Raised when result of an arithmetic operation is too large to be represented
ReferenceError: Raised when a weak reference proxy is used to access a garbage collected referent
RuntimeError: Raised when an error does not fall under any other category
StopIteration: Raised by next() function to indicate that there is no further item to be returned by iterator
SyntaxError: Raised by parser when syntax error is encountered
IndentationError: Raised when there is incorrect indentation
TabError: Raised when indentation consists of inconsistent tabs and spaces
SystemError: Raised when interpreter detects internal error
SystemExit: Raised by sys.exit() function
TypeError: Raised when a function or operation is applied to an object of incorrect type
UnboundLocalError: Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable
UnicodeError: Raised when an Unicode-related encoding or decoding error occurs
UnicodeEncodeError: Raised when an Unicode-related error occurs during encoding
UnicodeDecodeError: Raised when an Unicode-related error occurs during decoding
UnicodeTranslateError: Raised when an Unicode-related error occurs during translating
ValueError: Raised when a function gets argument of correct type but improper value
ZeroDivisionError: Raised when second operand of division or modulo operation is zero


Notes:
1) raise is the keyword used to throw an exception
2) the assert keyword is used to throw an AssertionError (that will only be thrown if condition isn't met)
- python disables assertions when run in optimized mode
- not a reliable way of catching exceptions in production
3) try...except...else blocks are for catching errors
4) Can always put custom message as argument to []Error
5) a try...except without except []Error as e will currently catch any exception
6) can have multiple exceptions caught, but only executes the first one

basic structure:

try:
except:
else:
finally: always runs no matter if exception encountered or not (so excecutes before the program stops after exception occured)
"""

def error_types_to_study():
    """
    Acronym: 
    AttributeError: when assigning or referencing attribute not go well
    TypeError: when function applied to incorrect type
    ValueError: when argument has improper value
    IndexError: when index is out of range
    KeyError: When key not found in dictionary
    """
    errors = [
        "AttributeError: Raised when attribute assignment or reference fails",
        "IndexError: Raised when index of a sequence is out of range",
        "KeyError: Raised when a key is not found in a dictionary",
        "TypeError: Raised when a function or operation is applied to an object of incorrect type",
        "ValueError: Raised when a function gets argument of correct type but improper value"
    ]
    
    
def assert_example():
    """
    Just put statement 
    """
    x = 10
    assert(x < 5), f"The number should not exceed 5. (x = {x})"
    
def raising_and_catching_exception():
    def linux_interaction():
        import sys
        if "linux" not in sys.platform:
            raise RuntimeError("Function can only run on Linux systems.")
        print("Doing Linux things.")
    
    try:
        linux_interaction()
    except RuntimeError as error:
        print(error)
        print("The linux_interaction() function wasn't executed.")
        
        
def multiple_exceptions_caught():
    try:
        linux_interaction()
        with open("file.log") as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except RuntimeError as error:
        print(error)
        print("Linux linux_interaction() function wasn't executed.")
        
def only_first_exception_caught_ever():
    """
    NOT MATTER WHAT ORDER YOU WRITE THE EXCEPT STATEMENTS
    """
    def my_func():
        x = 10
        0/0
        assert(x == 5), "x was not 5"
        return 0/0

    try:
        my_func()
    except AssertionError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
        
        
def executing_code_right_before_errors_with_finally():
    try:
        linux_interation()
    finally:
        print(f"Some final cleanup before any exceptions are thrown")