from logging import NullHandler, getLogger, StreamHandler, FileHandler, Formatter
import logging
import datetime


def get_logger(modname,mode=logging.DEBUG):
    logger = getLogger(modname)
    if mode == None:
        logger.addHandler(NullHandler())
        return logger
    logger.setLevel(mode)
    #create handler1 for showing info
    handler1 = StreamHandler()
    my_formatter  = MyFormatter()
    handler1.setFormatter(my_formatter)

    handler1.setLevel(mode) 
    logger.addHandler(handler1)
    #create handler2 for recording log file
    if mode <= logging.DEBUG:
        handler2 = FileHandler(filename="log.txt", encoding='utf-8')
        handler2.setLevel(logging.ERROR)
        handler2.setFormatter(my_formatter)


        logger.addHandler(handler2)
    return logger

class MyFormatter(logging.Formatter):
    def format(self, record):
        s =(datetime.datetime.fromtimestamp(record.created)).strftime("%m-%d %H:%M:%S")+'| '+ (record.module).ljust(15)+(' { '+record.funcName).ljust(20) +":"+str(record.lineno).rjust(4)+'} - '+record.getMessage()
        return s
