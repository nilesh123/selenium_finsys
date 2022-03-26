import logging as L

def log(level,message,file):
	L.basicConfig(level=L.INFO,filename=file,filemode="a",
				  format="%(asctime)-12s %(levelname)s %(message)s",
				  datefmt="%d-%m-%Y %H:%M:%S")
	if level == "INFO": L.info(message)
	if level == "WARNNG": L.warning(message)
	if level == "ERROR": L.error(message)
	if level == "CRITICAL": L.critical(message)