#! /usr/bin/env python3
import argparse
import os
import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def pause():
    while True:
        time.sleep(1)

class MyHandler(FileSystemEventHandler):
    def __init__(self, path_of_interest, port, process):
        self.path = path_of_interest
        self.port = port
        self.process = process

    def on_created(self, event):
        if self.path in event.src_path:
            print(f'Created event type: {event.event_type}  path : {event.src_path}')
            self.process.kill()
            self.process = subprocess.Popen(("python3 coap-dfu-server.py -pkg " + self.path + " -sp " + str(self.port)).split(' '), stdout=sys.stdout)

    def exit(self):
        self.process.kill()

class dfuServerManager():

    def __init__(self, package, server_port):
        self.package = package
        self.port = server_port
        self.path = '/'.join(self.package.split('/')[:-2])

    def start_server(self):
        # start process
        server_process = subprocess.Popen(("python3 coap-dfu-server.py -pkg " + self.package + " -sp " + str(self.port)).split(' '), stdout=sys.stdout)
        event_handler = MyHandler(self.package, self.port, server_process)
        self.observer = Observer()
        self.observer.schedule(event_handler, self.path, recursive=True)
        self.observer.start()

        try:
            pause()
        except Exception as e:
            self.observer.stop()
            print(e)
        event_handler.exit()
        self.observer.join()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CoAP DFU server based on pc-nrfutil')
    parser.add_argument('package', type=str, help='Filename of the DFU package.')
    parser.add_argument('-sp', '--server_port',
              help='UDP port to which the DFU server binds. If not specified then 5683 is used.',
              type=int,
              default=5683)
    args = parser.parse_args()

    # wait until an image is available
    while True:
        time.sleep(1)
        if os.path.exists(args.package):
            break

    dfu_server = dfuServerManager(args.package, args.server_port)
    dfu_server.start_server()
