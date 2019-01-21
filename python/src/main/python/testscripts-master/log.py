''' HAProxy Log Analyser:  Please find attached a sample log file 'input.log'. You  have to write a program 'log_analyser' in any language, which should do the following:
For example : 
Request                              Occurrence     Min(ms)   Avg(ms)   Max(ms) 
GET /index.html HTTP/1.1        10               100         105          111
'''
class LogFields(object):
    def __init__(self, list_line):
	self.process_name = list_line[4]
	self.client_address = list_line[5]
        self.accept_date = list_line[6]
	self.frontend_name = list_line[7]
	self.backend_info = server_info(list_line[8])
	self.tq_info = time_parameter(list_line[9])
	self.status_code = list_line[10]
	self.bytes_read = list_line[11]
	self.captured_request_cookie= list_line[12]
	self.captured_response_cookie = list_line[13]
	self.termination_state = list_line[14]
	self.actconn_info = actcon_info(list_line[15])
	self.queue_info = queue_info(list_line[16])
	self.captured_request_headers, self.captured_response_headers ,self.http_request = LogFields.process_data(list_line[17:])
    
    @staticmethod
    def process_data(list_data):
	captured_request_headers = None
        http_request = None
        captured_response_headers = None
        for index, data in enumerate(list_data):
	    if data.find("GET")>0 or data.find("POST")>0:
	       http_request = "".join(list_data[index:])
	       break
	    elif data.startswith("{"):
		if captured_request_headers is None:
		    captured_request_headers = data
		else:
		    captured_response_headers = data
	if captured_request_headers or captured_response_headers:
	    captured_request_headers, captured_response_headers = '{}','{}'
       
	return captured_request_headers, captured_response_headers, http_request
	    

class queue_info(object):
    def __init__(self, queue):
	self.srv_queue, self.backend_queue = queue.split('/')

class time_parameter(object):
    def __init__(self, tt_info):
	self.Tq, self.Tw, self.Tc, self.Tr, self.Tt = tt_info.split('/')	

class actcon_info(object):
    def __init__(self, actcon_info):
	self.actconn ,	self.feconn, 	self.beconn,	self.srv_conn,	self.retries = actcon_info.split('/')

class server_info(object):
    def __init__(self,server):
	self.server_name, 	self.backend_name = server.split('/')

class result_dict(object):
    def __init__(self,Occurrence,value):
	self.Occurrence = Occurrence
	self.Min = value
	self.Max = value
        self.all_value = [value]

def readlog(filename):
    f = open(filename,'r')
    processd_dict = {}
    x = f.xreadlines()
    while True:
        try:
        	line = x.next() 
	        list_line = list(line.split("\n")[0].split(" "))
	        lf = LogFields(list_line)  
		if processd_dict.has_key(lf.http_request):
		    result_obj = processd_dict[lf.http_request]
	            result_obj.Occurrence += 1
		    Min , Max = result_obj.Min, result_obj.Max
	       	    if int(lf.tq_info.Tt) > Max:
			result_obj.Max = int(lf.tq_info.Tt)
	       	    elif int(lf.tq_info.Tt) < Min:
			result_obj.Min = int(lf.tq_info.Tt)
	            result_obj.all_value.append(int(lf.tq_info.Tt))
	             
		else:
		   processd_dict[lf.http_request] = result_dict(1, int(lf.tq_info.Tt))
		
	except:
		break
    for k, v in processd_dict.iteritems():
	Occurrence = v.Occurrence
	Min = v.Min
	Max = v.Max
	Avg = sum(v.all_value)/Occurrence
	print  k, '    ',Occurrence,'    ', Min, '   ', Avg, '   ', Max
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print "Error:  Insufficient argument, expecting log file name"
    else:
	print "Request", '   ',"Ocurrence",'   ',"Min(ms)",'   ',"Avg(ms)",'   ',"Max(ms)"
        readlog(sys.argv[1])


