import re
from collections import OrderedDict
from datetime import datetime

# location of log file
log_file =  './ZOC17y-03m-17h-33m-01s.LOG'

# start marker
START = '/Firmware: Hw found, Proj found => OK!'
END1 = 'SWL cycle complete'
END2 = 'Software Loading complete'
FAIL = 'Software Download Failed!'

date_reg = re.compile('\[([0-9:.]+)\]')

ZADATA = OrderedDict()


def  get_timer(line):
    eltime = None
    timer = date_reg.match(str(line))
    if timer:
        eltime = timer.group(1).split('.')[0]

    return eltime


start_counter = 1
with open(log_file, 'r') as log:
    for line in log:
        # we are looking for a start marker
        if START in line:
            index  =  start_counter
            if index not in ZADATA.keys():
                ZADATA[index] = {}
                ZADATA[index]['start_time'] = get_timer(line)
                ZADATA[index]['status'] = 'SUCCESS'
        else:
            if END1 in line or END2 in line:
                ZADATA[index]['end_time'] = get_timer(line)
                ZADATA[index]['complete'] = True
            elif FAIL in line:
                ZADATA[index]['status'] = 'FAILURE'
                ZADATA[index]['end_time'] = get_timer(line)
                ZADATA[index]['complete'] = True
            else:
                continue

        if ZADATA[index].get('complete', False):
            start_t = datetime.strptime(ZADATA[index]['start_time'], '%H:%M:%S')
            end_t = datetime.strptime(ZADATA[index]['end_time'], '%H:%M:%S')
            diff = end_t - start_t
            ZADATA[index]['duration'] = diff
            start_counter += 1



for run in ZADATA.keys():
    data = ZADATA[run]
    run_id = run
    start_time = data['start_time']
    end_time = data['end_time']
    duration = data['duration']
    status = data['status']
    print '#' * 100
    print "Data for test {}".format(run_id)
    print "Start time: {} End time: {} Duration: {}".format(start_time, end_time, duration)
