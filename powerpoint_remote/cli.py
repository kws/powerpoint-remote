import click
import socket
from werkzeug.serving import get_interface_ip
import qrcode

from powerpoint_remote.app import app


@click.command("runserver")
@click.option("-p", "port", default=5555, type=int, help="Port to run the server on")
@click.option("-h", "host", default="0.0.0.0", help="Host to run the server on")
@click.option("--debug", is_flag=True, help="Run the server in debug mode")
def runserver(port, host, debug):
    ip = get_interface_ip(socket.AF_INET)
    url = f'http://{ip}:{port}'

    qr = qrcode.QRCode()
    qr.add_data(url)
    qr.print_ascii()

    app.run(host=host, port=port, debug=debug)
