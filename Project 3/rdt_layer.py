import copy

from segment import Segment


# #################################################################################################################### #
# RDTLayer                                                                                                             #
#                                                                                                                      #
# Description:                                                                                                         #
# The reliable data transfer (RDT) layer is used as a communication layer to resolve issues over an unreliable         #
# channel.                                                                                                             #
#                                                                                                                      #
#                                                                                                                      #
# Notes:                                                                                                               #
# This file is meant to be changed.                                                                                    #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #


class RDTLayer(object):
    # ################################################################################################################ #
    # Class Scope Variables                                                                                            #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    DATA_LENGTH = 4 # in characters                     # The length of the string data that will be sent per packet...
    FLOW_CONTROL_WIN_SIZE = 15 # in characters          # Receive window size for flow-control
    sendChannel = None
    receiveChannel = None
    dataToSend = ''
    currentIteration = 0                                # Use this for segment 'timeouts'
    # Add items as needed

    # ################################################################################################################ #
    # __init__()                                                                                                       #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def __init__(self):
        self.sendChannel = None
        self.receiveChannel = None
        self.dataToSend = ''
        self.currentIteration = 0
        self.inputIndex = -1
        self.availableWindow = 15   # window size
        # Add items as needed

        # Segment list
        self.segmentList = ''       # so segment list isn't recreated multiple times

        # Window, sequence, acknowledge, data received
        self.received = []
        self.lastAck = 0
        self.sendBase = 0
        self.pipelineSeg= 0
        self.buffer = {}   # time out for segments
        self.timeoutIteration = 0
        self.dataReceived = ''
        self.charRvcd = 0
        self.currentAck = 0
        self.dataLength = 0



    # ################################################################################################################ #
    # setSendChannel()                                                                                                 #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to set the unreliable sending lower-layer channel                                                 #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def setSendChannel(self, channel):
        self.sendChannel = channel

    # ################################################################################################################ #
    # setReceiveChannel()                                                                                              #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to set the unreliable receiving lower-layer channel                                               #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def setReceiveChannel(self, channel):
        self.receiveChannel = channel

    # ################################################################################################################ #
    # setDataToSend()                                                                                                  #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to set the string data to send                                                                    #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def setDataToSend(self,data):
        self.dataToSend = data

    # ################################################################################################################ #
    # getDataReceived()                                                                                                #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to get the currently received and buffered string data, in order                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def getDataReceived(self):
        # ############################################################################################################ #
        # Identify the data that has been received...

        print('getDataReceived(): Complete this...')

        # ############################################################################################################ #
        return self.dataReceived

    # ################################################################################################################ #
    # processData()                                                                                                    #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # "timeslice". Called by main once per iteration                                                                   #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def processData(self):
        self.currentIteration += 1
        self.processSend()
        self.processReceiveAndSendRespond()

    # ################################################################################################################ #
    # processSend()                                                                                                    #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Manages Segment sending tasks                                                                                    #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def processSend(self):

        #no data, then skip
        if not self.dataToSend:
            return

        if self.sendBase == self.lastAck:
            while self.pipelineSeg < 3:
                segmentSend = Segment()
                seqnum = self.sendBase
                data = self.dataToSend[seqnum:seqnum + self.DATA_LENGTH]

        # ############################################################################################################ #
        print('processSend(): Complete this...')





        # You should pipeline segments to fit the flow-control window
        # The flow-control window is the constant RDTLayer.FLOW_CONTROL_WIN_SIZE
        # The maximum data that you can send in a segment is RDTLayer.DATA_LENGTH
        # These constants are given in # characters

        # Somewhere in here you will be creating data segments to send.
        # The data is just part of the entire string that you are trying to send.
        # The seqnum is the sequence number for the segment (in character number, not bytes)





        # ############################################################################################################ #
        # Display sending segment
        print("Sending segment: ", segmentSend.to_string())
        self.sendBase += 4
        self.buffer[seqnum] = 0
        segmentCopy = copy.deepcopy(segmentSend)
        self.sendChannel.send(segmentCopy)
        self.pipelineSeg += 1

        # Use the unreliable sendChannel to send the segment
        self.sendChannel.send(segmentSend)

    # ################################################################################################################ #
    # processReceive()                                                                                                 #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Manages Segment receive tasks                                                                                    #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def processReceiveAndSendRespond(self):
        # This call returns a list of incoming segments (see Segment class)...
        listIncomingSegments = self.receiveChannel.receive()

        # ############################################################################################################ #
        # What segments have been received?
        # How will you get them back in order?
        # This is where a majority of your logic will be implemented
        print('processReceive():')
        # Client side
        if self.dataToSend != '':
            #sort received packets
            listIncomingSegments.sort(key=lambda x:x.acknum)
            acknum = -1
            # Check that acks are execpted and in correct order
            for pkt in listIncomingSegments:
                if pkt.acknum == self.lastAck + 4 and self.lastAck not in self.received:
                    self.pipelineSeg -= 1
                    self.received.append(self.lastAck)
                    self.buffer.pop(self.lastAck)
                    self.lastAck += 4
                else:
                    acknum = pkt.acknum

            # check segment timeouts, if timed out, send packet
            for seqnum, count in self.buffer.items():
                if self.currentIteration - count > 4 and acknum == 1:
                    self.timeoutIteration += 1
                    acknum = seqnum
                self.buffer[seqnum] += 1


            # Send packets
            if acknum != 1:
                for seq in range(acknum,acknum +9, 4):
                    data = self.dataToSend[seq:seq + self.DATA_LENGTH]
                    segmentSend = Segment()
                    # Print sending seg
                    segmentSend.setData(seq,data)
                    print("Sending segment: ", segmentSend.to_string())

                    self.sendChannel.send(segmentSend)  # use unreliable send channel
        #Server side
        else:
            if listIncomingSegments:
                #sort received packets
                listIncomingSegments.sort(key=lambda x: x.seqnum)
                for packet in listIncomingSegments:
                    segmentAck = Segment()

                    #check if packet is already in data received, check the checksum for each packet
                    if packet.seqnum < len(self.dataReceived):
                        continue
                    if not packet.checkChecksum():
                        continue

                    else:
                        if packet.seqnum == self.lastAck :
                            print('processReceive(): Complete this...')
                            print('Received segment:', packet.payload)
                            self.lastAck += 4
                            acknum = self.lastAck
                            # add data received
                            self.dataReceived += packet.payload
                        else:
                            acknum = self.lastAck
                    segmentAck.setAck(acknum)
                    print('Sending Ack: ', segmentAck.to_string())
                    self.sendChannel.send(segmentAck)

        # ############################################################################################################ #
        # How do you respond to what you have received?
        # How can you tell data segments apart from ack segemnts?

        # Somewhere in here you will be setting the contents of the ack segments to send.
        # The goal is to employ cumulative ack, just like TCP does...



        # ############################################################################################################ #
        # Display response segment
  #  segmentAck.setAck(acknum)
    #print("Sending ack: ", segmentAck.to_string())

        # Use the unreliable sendChannel to send the ack packet
    #self.sendChannel.send(segmentAck)
