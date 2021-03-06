import sys
import datetime
import getopt
import pika
import json

def usage():
	print('\nUsage:\n')
	print('send-msg.py -h -l <LocationName> -c <ClusterName>  -d <UTCDateTime> -s <StormName> -n <StormNumber> -a <AdvisoryNumber> -m <Message> -y <EventType> -p <Process> -t <PctComplete> -r <State>')
	print('		')		
	print(' where -h | --Help		the text you are looking at right now')
	print('       -l | --LocationName	name of location where model is running, i.e. UNC')
	print('       -c | --ClusterName 	name of cluster running model, i.e. Hatteras')
	print('       -d | --UTCDateTime	UTC date time - ISO 8601 format; if not provided defaults to now')
	print('       -s | --StormName		hurricane name, i.e. Irene')
	print('       -n | --StormNumber 	hurricane id number')
	print('       -a | --AdvisoryNumber	NHC advisory number for this run')
	print('       -m | --Message		the actual message to send')
	print('       -y | --EventType		event type, RSTR | PRE1 | NOWC | PRE2 | FORC | POST | REND ')
	print('       -p | --Process		software process issuing this message')
	print('       -t | --PctComplete	numeric percentage of completion of process running, i.e. 34.2')
	print('       -r | --State		ASGS run state, STRT | RUNN | PEND | FAIL | WARN | IDLE | EXIT')
	print(' ')

def JsonifyMessage(LocationName,
                   ClusterName,
                   UTCDateTime,
                   StormName,
                   StormNumber,
                   AdvisoryNumber,
                   Message,
                   EventType,
                   Process,
                   PctComplete,
                   State):
	
	msg_obj = {'name': 'asgs', 'physical_location': LocationName, 'clustername': ClusterName, 'date-time': UTCDateTime, 'message': Message, 'event_type': EventType, 'process': Process, 'pctcomplete': PctComplete, 'state': State, 'storm': StormName, 'storm_number': StormNumber, 'advisory_number': AdvisoryNumber}

	return json.dumps(msg_obj)


def queue_message(message):

	print(message)

########## NEED TO GET THIS STUFF FROM YAML FILE #########################
	credentials = pika.PlainCredentials('user', 'password')
	parameters = pika.ConnectionParameters('hostname', 5672, '/', credentials, socket_timeout=2)
	connection = pika.BlockingConnection(parameters)
	channel = connection.channel()
	channel.queue_declare(queue="asgs_queue")
	channel.basic_publish(exchange='',routing_key='asgs_queue',body=message)
	connection.close()


def main(argv):

	LocationName = 'RENCI'
	ClusterName = 'hatteras'
	tmpDateTime = datetime.datetime.utcnow()
	UTCDateTime = tmpDateTime.strftime("%Y-%m-%d %H:%M:%S")
	StormName = ''
	StormNumber = ''
	AdvisoryNumber = ''
	Message = 'test message'
	EventType = ''
	Process = 'asgs'
	PctComplete = '0'
	State = 'IDLE'

	try:
        	opts, args = getopt.getopt(argv,"hl:c:d:s:n:a:m:y:p:t:r:",["Help","LocationName=","ClusterName=","UTCDateTime=","StormName=", "StormNumber=", "AdvisoryNumber=", "Message=", "EventType=", "Process=", "PctComplete=", "State="])
	except getopt.GetoptError as err:
        	print('\nCommand line option error: ' + str(err))
        	usage()
        	sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h", "--Help"):
			usage()
			sys.exit(2)
		elif opt in ("-l", "--LocationName"):
			LocationName = arg
		elif opt in ("-c", "--ClusterName"):
			ClusterName = arg
		elif opt in ("-d", "--UTCDateTime"):
			UTCDateTime = arg
		elif opt in ("-s", "--StormName"):
			StormName = arg
		elif opt in ("-n", "--StormNumber"):
			StormNumber = int(arg)
		elif opt in ("-a", "--AdvisoryNumber"):
			AdvisoryNumber = arg     
		elif opt in ("-m", "--Message"):
			Message = arg
		elif opt in ("-y", "--EventType"):
			EventType = arg
		elif opt in ("-p", "--Process"):
			Process = arg
		elif opt in ("-t", "--PctComplete"):
			PctComplete = arg
		elif opt in ("-r", "--State"):
			State = arg

	msg = JsonifyMessage(
			LocationName, 
			ClusterName, 
			UTCDateTime, 
			StormName, 
			StormNumber, 
			AdvisoryNumber, 
			Message, 
			EventType,
                        Process,
                        PctComplete,
                        State
			)

	queue_message(msg)


if __name__ == "__main__":
    	main(sys.argv[1:])
