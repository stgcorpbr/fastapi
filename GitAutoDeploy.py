#!/usr/bin/env python

import json, sys, os
from http.server import BaseHTTPRequestHandler, HTTPServer
from subprocess import call

class GitAutoDeploy(BaseHTTPRequestHandler):

    CONFIG_FILEPATH = './GitAutoDeploy.conf.json'
    config = None
    quiet = False
    daemon = False
    payload = ''

    @classmethod
    def getConfig(myClass):
        if(myClass.config == None):
            try:
                configString = open(myClass.CONFIG_FILEPATH).read()
            except:
                sys.exit('Could not load ' + myClass.CONFIG_FILEPATH + ' file')

            try:
                myClass.config = json.loads(configString)
            except:
                sys.exit(myClass.CONFIG_FILEPATH + ' file is not valid json')

            for repository in myClass.config['repositories']:
                if(not os.path.isdir(repository['path'])):
                    sys.exit('Directory ' + repository['path'] + ' not found')
                # Check for a repository with a local or a remote GIT_WORK_DIR
                if not os.path.isdir(os.path.join(repository['path'], '.git')) \
                   and not os.path.isdir(os.path.join(repository['path'], 'objects')):
                    sys.exit('Directory ' + repository['path'] + ' is not a Git repository')

        return myClass.config

    def do_GET(self):
        print('link acessado via http', 'Alerta de acesso não permitido!')

    def do_POST(self):        
        event = self.headers.get('X-Github-Event')
        if event == 'ping':
            if not self.quiet:
                print ('Ping event received')
            self.respond(204)
            return
        if event != 'push':
            if not self.quiet:
                print('We only handle ping and push events')
            self.respond(304)
            return
        
        bd = self.rfile.read(int(self.headers.get('content-length')))      
        GitAutoDeploy.payload = json.loads(bd)
        
        self.respond(204)

        urls = self.parseRequest()
        for url in urls:
            paths = self.getMatchingPaths(url)
            for path in paths:
                payload = GitAutoDeploy.payload
                msg = payload.get('commits')[0].get('message')
                print('msg: ', msg)
                if 'task' in msg:
                    self.taskDeploy(path)
                else:
                    self.fetch(path)
                    self.deploy(path)

    def parseRequest(self):     
        payload = GitAutoDeploy.payload
        self.branch = payload['ref']
        return [payload['repository']['url']]

    def getMatchingPaths(self, repoUrl):
        res = []
        config = self.getConfig()
        for repository in config['repositories']:
            if(repository['url'] == repoUrl):
                res.append(repository['path'])
        return res

    def respond(self, code):
        self.send_response(code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def fetch(self, path):
        if(not self.quiet):
            print ("\nPost push request received")
            print ('Updating ' + path)
        call(['cd "' + path + '" && git fetch'], shell=True)

    def taskDeploy(self, path):
        config = self.getConfig()
        for repository in config['repositories']:
            if(repository['path'] == path):
                if 'deploy' in repository:
                    branch = None
                    if 'branch' in repository:
                        branch = repository['branch']

                    if branch is None or branch == self.branch:
                        if(not self.quiet):
                            print ('Executing deploy command')
                        print ('Executing deploy task command')
                        call(['cd "' + path + '" && git pull && ' + repository['deploy'] + '&& sudo systemctl restart nginx' + '&& sudo systemctl restart gufapi.service' +'&& sudo systemctl restart celery.service'], shell=True)
                        print ('deploy task finalized')
                        
                    elif not self.quiet:
                        print ('Push to different branch (%s != %s), not deploying' % (branch, self.branch))
                break

    def deploy(self, path):
        config = self.getConfig()
        for repository in config['repositories']:
            if(repository['path'] == path):
                if 'deploy' in repository:
                    branch = None
                    if 'branch' in repository:
                        branch = repository['branch']

                    if branch is None or branch == self.branch:
                        if(not self.quiet):
                            print ('Executing deploy command')
                        call(['cd "' + path + '" && git pull && ' + repository['deploy']  + '&& sudo systemctl restart nginx.service' + '&& sudo systemctl restart nginx'], shell=True)
                        print ('deploy finalized')
                        
                    elif not self.quiet:
                        print ('Push to different branch (%s != %s), not deploying' % (branch, self.branch))
                break

def main():
    try:
        server = None
        for arg in sys.argv: 
            if(arg == '-d' or arg == '--daemon-mode'):
                GitAutoDeploy.daemon = True
                GitAutoDeploy.quiet = True
            if(arg == '-q' or arg == '--quiet'):
                GitAutoDeploy.quiet = True
                
        if(GitAutoDeploy.daemon):
            pid = os.fork()
            if(pid != 0):
                sys.exit()
            os.setsid()

        if(not GitAutoDeploy.quiet):
            print('Github Autodeploy Service v1.0 started')
        else:
            print('Github Autodeploy Service v1.0 started in daemon mode')        
        
        with HTTPServer(('', GitAutoDeploy.getConfig()['port']), GitAutoDeploy) as server:            
            server.serve_forever()

    except (KeyboardInterrupt, SystemExit) as e:
        if(e): # wtf, why is this creating a new line?
            print(sys.stderr, e)

        if(not server is None):
            server.socket.close()

        if(not GitAutoDeploy.quiet):
            print('Goodbye')

if __name__ == '__main__':
     main()
