from main import Pydemon
import argparse
import asyncio


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--exec', '-exec',default=None)
    parser.add_argument('--version', '-version', action='store_true')
    parser.add_argument('--create', '-create', action='store_true')
    args = parser.parse_args()
    if args.version == True:
        print('Version is 0.0.1')
    if args.create == True:
        print('create by Londarks')
    if args.version == False and args.create == False:
        server = Pydemon(args.exec)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(server.main())
