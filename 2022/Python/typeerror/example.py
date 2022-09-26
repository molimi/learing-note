"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/26
Description: error
"""
'''
def div(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Error: divisor should not be 0 !")
    except Exception as e:
        print('Unexpected Error: {}'.format(e))
    else:
        print('Run into else only when everything goes well')
    finally:
        print('Always run into finally block.')


# tests
div(2, 0)
div(2, 'bad type')
div(1, 2)

# Multiple exception in one line
try:
    print(a/b)
except (ZeroDivisionError, TypeError) as e:
    print(e)


# Exception block is optional when there is finally
try:
    open(database)
finally:
    close(database)

# catch all errors and log it
try:
    do_work()
except: 
    # get detail fro logging module
    logging.exception('Exception caught!')
    
    # get detail from sys.exc_info() method
    error_type, error_value, trace_back = sys.exc_info()
    print(error_value)
    raise
'''


def f1():
    print(1 / 0)


def f2():
    try:
        f1()
    except Exception as e:
        raise


f2()