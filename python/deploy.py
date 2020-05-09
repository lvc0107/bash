from os import listdir, path, getenv, symlink, unlink
from subprocess import Popen, PIPE
from datetime import datetime
import argparse
import logging
import sys


def config_logger():
    """ Output log to file and stdout. """
    logging.basicConfig(
        filename='deploy.log',
        level=logging.INFO,
        format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )
    #TODO check this
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(logging.Formatter('%(levelname)-8s: %(message)s'))
    logging.getLogger('').addHandler(console)

def deploy_proxy(proxy_path=None, proxies=None, env=None):
    if path.isdir(proxy_path):
        logging.info(
            "\n%s\nProxy %s \nRun at %s \n",
            "#" * 10,
            proxies,
            datetime.utcnow(),
        )
        # mvn install -Pstaging -Dusername=$apigee_user -Dpassword=$apigee_pass -Dapigee.config.options=update
        # TODO check this
        p = Popen(
            [
                "mvn",
                "install",
                "-f{}/pom.xml".format(proxy_path),
                "-P{}".format(env),
                "-Dapigee.config.options=update",
                "-Dusername={}".format(getenv('bamboo.maven.deploy.username', ' ')),
                "-Dpassword={}".format(getenv('bamboo.maven.deploy.password', ' ')),
            ],
            stdout=PIPE,
            stderr=PIPE
        )
        # TODO check this
        output, error = p.communicate()
        logging.info(output)
        if error:
            logging.warning(error)
        if 'BUILD FAILURE' in output:
            sys.exit(1)


def main():
    config_logger()
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="path")
    parser.add_argument("--env", help="environment")
    parser.add_argument("--skip_proxies", help="List of proxies to be ignored in the deploy.")
    args = parser.parse_args()
    _path = args.path
    env = args.env
    skip_proxies = args.skip_proxies.split(",") if args.skip_proxies else []
    if _path and env:
        dir_path = path.dirname(path.realpath(__file__))
        base_proxy_path = path.join(dir_path, _path)
        deploy_proxy(proxy_path=path.join(base_proxy_path, 'config-core'), proxies='config-core', env=env)
        for proxies in listdir(base_proxy_path):
            proxy_path = path.join(base_proxy_path, proxies)

            if not path.isdir(proxy_path):
                continue

            edge_file_path = path.join(proxy_path, 'edge.json')

            if path.islink(edge_file_path):
                unlink(edge_file_path)

            if not path.isfile(edge_file_path):
                env_edge_file_path = path.join(
                    proxy_path,
                    'edge/',
                    'prod.json' if env == 'prod' else 'preprod.json'
                )
                symlink(env_edge_file_path, edge_file_path)

            if not proxies.lower() == 'config-core' and proxies not in skip_proxies:
                deploy_proxy(proxy_path=proxy_path, proxies=proxies, env=env)
    else:
        logging.error("You need to pass path and the environment.")


if __name__ == "__main__":
    main()
