import logging
logging.basicConfig(level=logging.INFO,filename="demologs.log",filemode="a",format='%(asctime)s - %(levelname)s : %('
                                                                                   'message)s')
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")