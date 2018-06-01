## ASGS-MSGR

### Send ASGS status messages to a amqp message queue

JSON message format:

```

{
   name: asgs
   physical_location: RENCI
   cluster_name: hatteras
   date-time: 2018-01-01 12:00:00
   message: This message is to let you know that the ASGS has been ACTIVATED using NAM forcing on the $GRIDFILE mesh.
   event_type: RSTR | PRE1 | NOWC | PRE2 | FORC | POST | REND
   storm: IRMA
   storm_number: 5
   advisory_number: 22
   process: bash_script.sh
   pctComplete: 34.5
   state: STRT | RUNN | PEND | FAIL | WARN | IDLE | EXIT
} 

```
