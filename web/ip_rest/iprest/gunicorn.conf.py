import os

bind = "0.0.0.0:8000"
workers = os.sysconf("SC_NPROCESSORS_ONLN") * 2
log_syslog = True
loglevel = "error"
