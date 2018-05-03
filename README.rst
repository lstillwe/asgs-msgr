##ASGS-MSGR

Send ASGS status messages to a amqp message queue

JSON message format:

```
{
   name: asgs
   uid?:
   physical_location:
   cluster_name: hatteras
   run_type: weather | hurricane
   date-time: 2018-01-01 12:00:00
   hurricane {
      storm: IRMA
      storm_number: 5
      advisory_number: 22
   }
   weather {
      other_stuff?:
   }
   message: This message is to let you know that the ASGS has been ACTIVATED using NAM forcing on the $GRIDFILE mesh.
   message_type: startup | info | warning | error| fatal | etc
}
    
```