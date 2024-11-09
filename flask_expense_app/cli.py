import argparse
from flask_expense_app.mainapp import app

def create_parser():
    parser = argparse.ArgumentParser(description="Flask expense app ")
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Host to bind to')
    parser.add_argument('--port', type=int, default=5001, help='Port to listen on')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    return parser


def cli():
    "Flask expense app "
    parser = create_parser()
    args = parser.parse_args()
    mycommand(args)


def mycommand(args):
    app.run(host=args.host, debug=args.debug, port=args.port)