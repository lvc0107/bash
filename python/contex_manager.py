from threading import Lock

lock = Lock()


def foo1():
    def do_something_dangerous():
        lock.acquire()
        raise Exception('oops I forgot this code could raise exceptions')
        lock.release()

    try:
        do_something_dangerous()
    except:
        print('Got an exception')
    lock.acquire()
    print('Got here')


def foo2():
    def do_something_dangerous():
        with lock:
            raise Exception('oops I forgot this code could raise exceptions')

            try:
                do_something_dangerous()
            except:
                print('Got an exception')
            lock.acquire()
            print('Got here')


# foo1()
foo2()
