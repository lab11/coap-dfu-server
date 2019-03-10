#! /usr/bin/env python2
import click
import os
import piccata
import sys
sys.path.append(os.getcwd() + '/pc-nrfutil')

from transport.tsocket import SocketTransport
from nordicsemi.thread.dfu_thread import create_dfu_server
from nordicsemi.dfu.package import Package

def pause():
    while True:
        try:
            raw_input()
        except (KeyboardInterrupt, EOFError):
            break

@click.command(short_help="Update the firmware on a device over an IP connection.")
@click.option('-pkg', '--package',
              help='Filename of the DFU package.',
              type=click.Path(exists=True, resolve_path=True, file_okay=True, dir_okay=False),
              required=True)
@click.option('-sp', '--server_port',
              help='UDP port to which the DFU server binds. If not specified the 5683 is used.',
              type=click.INT,
              default=5683)
@click.option('-mc', '--mcast_dfu',
              help='Use multicast. ',
              default=False)
@click.option('-r', '--rate',
              help="Multicast upload rate in blocks per second.",
              type=click.FLOAT)
@click.option('-rs', '--reset_suppress',
              help='Suppress device reset after finishing DFU for a given number of milliseconds. ' +
                   'If -1 is given then suppress indefinitely.',
              type = click.INT,
              metavar = '<delay_in_ms>')
def start_server(package, server_port, mcast_dfu, rate, reset_suppress):
    opts = type('DFUServerOptions', (object,), {})()
    opts.mcast_dfu = mcast_dfu
    opts.rate = rate
    opts.reset_suppress = reset_suppress

    transport = SocketTransport(server_port)
    dfu = create_dfu_server(transport, package, opts)
    try:
        sighandler = lambda signum, frame : transport.close()
        transport.open()
        pause()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    start_server()
