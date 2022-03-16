import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

def thread_function2(cont):
    logging.info("Cont %s: starting", cont)
    time.sleep(2)
    logging.info("Cont %s: finishing", cont)

cont = 0
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level = logging.INFO, datefmt = "%H:%M:%S")

    threads=list()
    for index in range(3):
        cont += 2
        #logging.info("Main      : create and start thread %d.", index)
        if index > 0:
            x = threading.Thread(target = thread_function, args = (index,))
        else:
            x = threading.Thread(target = thread_function2, args = (cont,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main      : before joining thread %d.", index)
        thread.join()
        logging.info("Main      : thread %d done.", index)
    logging.info("Contador  : %d.", cont)