"""
This code runs continuously on the groundstation computer (rpi).

It does the following:
    - collects measurements from all sensors and stores them.
    - sends notifications via Slack based on configured triggering criteria.
"""
# standard library imports
import socket
import time

# 3rd party library imports (e.g. pip install'd)

# internal libraries
import credentials


class GroundStation():
    def __init__(self):
        # TODO: initialize the TCP socket listener(s). will use the 'socket' library, part of standard library

        # TODO: initialize data structure to hold measurements. a 'dictionary' is a good start

        # TODO: initialize slack bot connection. will need to install this to import it and set up
        #       'webhook' with the slack channel
        pass

    def updateProbeMeasurements(self):
        # TODO: tries to establish connection with every probe
        # TODO: gather measurements from connected probes, store them
        pass

    def sendAlerts(self):
        # TODO: inspect the state of the measurements data structure
        #       send slack alert if required. otherwise do nothing
        pass


def main():
    print("groundstation started")

    gs = GroundStation()

    iter = 0
    while True:
        print("groundstation iteration {}".format(iter))
        iter += 1

        gs.updateProbeMeasurements()
        gs.sendAlerts()

        time.sleep(2)


if __name__ == "__main__":
    main()
