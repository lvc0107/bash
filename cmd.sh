#===================================
Apache:
wget http://mirrors.dcarsat.com.ar/apache/maven/maven-3/3.5.2/binaries/apache-maven-3.5.2-bin.tar.gz
tar xvfz apache-maven-3.5.2-bin.tar.gz
Add apache-maven-3.5.2/bin/ to  PATH  in ~/.bashrc
export PATH=$PATH:apache-maven-3.5.2/bin/
. ~/.bashrc
Check Java installation anf JAVA_HOME variable


#==================================
bash

#==================================
BATCH

ren  2015* 2016*

#===================================
building command:
ln -s  source target
echo "hi" &> file
echo "hi" | tee file
ls -lrtha
df -h
du -s
whoami
whereis package
which program
echo $?
echo "hi" > /dev/null
cat /proc/meminfo
cat /proc/cpuinfo
> file
history | less
history | grep <word>
history -d <line>
jobs
ctrl +z
fg job_id
bg job_id

command &
top
ps aux |  grep <pid> / <word>
diff file1 file2
file <filename>
stat <filename>
type <filename>
man command
dos2unix
> file
touch file
clear
tar -xvfz checkinstall_1.6.2-4.debian.tar.gz
src=$(mktemp -d) && cd $src
wget -N http://nodejs.org/dist/node-latest.tar.gz
date
mkdir -p
kill -9 PID

netstat -lx
https://www.linux-party.com/29-internet/8969-20-comandos-netstat-para-administradores-de-redes-linux
ipconfig TODO  complete  virtual interfaces
source
bash
sudo su
chmod 755 +- x +-r
chown  user file

sudo adduser intel
sudo adduser intel sudo
ssh-keygen -t rsa -b 4096 -v

grep -rl 'output_count' ./ | xargs sed -i 's/output_count/amount_output_kvertices/g' isExpandsNkvertices.py
grep -rl 'windows' ./ | xargs sed -i 's/windows/linux/g'
perl -p -i -e 's/\/home\/andres\/HPC\/En_Mendieta/archivos_grads\/home\/alighezzolo\/conae/\/gcc\/gradsfiles\/meteogramas/g' *.gs
perl -p -i -e 's/\/home\/andres\/HPC\/En_Mendieta\/archivos_grads/\/home\/alighezzolo\/conae\/gcc\/gradsfiles/g' *.gs
perl -p -i -e 's/\/home\/alighezzolo\/conae\/gcc\/gradsfiles/\./g' *.gs

perl -p -i -e 's/archivos_grads/gradsfiles/g' *.gs

CHequear dejo de funcionar
perl -p -i -e 's/wrfout_d01_[0-9]{4}-[0-9]{2}-[0-9]{2}_[0-9]{2}:[0-9]{2}:[0-9]{2}/wrfout_d01_$ENV{ACTUAL_START_DATE}/g' namelist.ARWpost

md5sum  apache-cassandra-3.7-bin.tar.gz | grep  39968c48cbb2a333e525f852db59fb48

sudo netstat -plnt



#==================================
CASSANDRA
cd apache-cassandra-3.7/bin/   cd /opt/cassandra/bin (para int)
./cqlsh 
cqlsh> use cassandra ;
cqlsh> drop keyspace cassandra;  case_mgmt(para int)
cqlsh> exit

#=================================
CORS
No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'http://www.webtoolkitonline.com' is therefore not allowed access.

Add this policy in apigee 



<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<AssignMessage async="false" continueOnError="false" enabled="true" name="add-cors">
    <DisplayName>Add CORS</DisplayName>
    <FaultRules/>
    <Properties/>
    <Add>
        <Headers>
            <Header name="Access-Control-Allow-Origin">{request.header.origin}</Header>
            <Header name="Access-Control-Allow-Headers">origin, x-requested-with, accept, content-type</Header>
            <Header name="Access-Control-Max-Age">3628800</Header>
            <Header name="Access-Control-Allow-Methods">GET, PUT, POST, DELETE</Header>
        </Headers>
    </Add>
    <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    <AssignTo createNew="false" transport="http" type="response"/>
</AssignMessage>

#==================================
Chrome
https://user:password@URL

#==================================
CORS:

    
Access-Control-Allow-Credentials →true
Access-Control-Allow-Origin →https://content.dev-tmp.com
Connection →keep-alive
Content-Length →162
Content-Type →application/json; charset=UTF-8
Date →Wed, 06 Jul 2016 14:23:48 GMT
Server →nginx/1.10.1
Vary →Origin
Via →kong/0.8.1-Kong-Proxy-Latency →0
X-Kong-Upstream-Latency →125
#==================================
curl

curl -v 'https://google.com'
curl -L -X GET --header "Content-Type: application/json"  "http://localhost:8000/api/v1/user/" | python -m json.tool | pygmentize -l json
curl -L -X GET --header "Content-Type: application/json"  "http://localhost:8000/api/v1/user/" -i

curl --request PATCH/POST/PUT --header 'authorization: Bearer ACCESS_TOKEN' \
curl -X PATCH/PATH/POST/PUT -H 'authorization: Bearer ACCESS_TOKEN' \
-H "Content-Type: application/json" \
-d \
'{"payload":{}
}' \
"https://SOME_URL" \
| python -m json.tool | pygmentize -l json | tee users

export USER=user1
export PASS=secret


data='
{
      "query":"MATCH (n) DETACH DELETE n;"
  }'

curl -u "$USER:$PASS" -b -j -k -H "Content-Type: application/json" -d "$data" $HOST:$PORT/neo4j/db/data/cypher

#===================================
Django:
django-admin startproject apiexample
python manage.py migrate
python manage.py runserver 0.0.0.0:3010
python manage.py syncdb --all && python manage.py migrate --fake
python manage.py syncdb && python manage.py migrate
#==================================
Docker:
sudo usermod -aG docker $(whoami)
docker ps
docker exec -ti [container id] bash 


#===================================
git:

git config --global user.name "Migue"
git config --global user.email miguelmnr@gmail.com
git config --global alias.tree 'log --graph --full-history --all --color --date=short --pretty=format:"%Cred%x09%h %Creset%ad%Cblue%d %Creset %s %C(bold)(%an)%Creset"'
git config --global alias.tree 'log --graph --full-history --all --color --date=short'
git tree
git config --global --add mergetool.kdiff3.path "C:/Program Files/KDiff3/kdiff3.exe"
git mergetool -t kdiff3

git clean -i
git show <commit_id>
git log
git diff
git mv file1 file2
git checkout file
git checkout branch
git checkout -b <new_branch_name>
git branch
git branch -a

If I have a branch feaure cloned in another working firectory
git branch -d feature/teamcity_integration


change the name of local repository:
git branch -m "feature/new_name"
git merge --abort


git fetch origin
git stash save "Stash descriptiion"
git stash apply @{NUM} // check stash description
git stash clear  #remove all in stash
git merge branch_2 (step in branch1)
git merge --no-ff branch_2 (step in branch1)
git mergetool -t kdiff3
TODO study
git revert
git cherry-pick
git rebase:
	git checkout branch
	git rebase master
	git mergetool -t kidff3 #if conflict
		git add <file>
		git rebase --continue
		git checkout master
		git merge branch
	git rm <file>
	git rebase --abort
		
git reset 123455666:  this commit is the upper  after reseting : The reseted commits remains as local changes

git reset --hard 123454545 : WARNING: dengeraus operation. All reseted commits are erased

git push -f : WARNING: dengeraus operation. All reseted commits are erased
git push: Check  if changes in severals branches are pushed
git push origin remote_branch: specific push


Problems with 2fA
https://help.github.com/articles/https-cloning-errors/#provide-access-token-if-2fa-enabled

git remote -v

Creating Acces Token
https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/

changing HTTPS by SSH
git remote set-url origin git@github.com:lvc0107/bash.git


#==================================
git-flow


git flow init -f 
production -> master
next release -> develop
Feature branches? [feature/]
 
o enter all

git flow feature start playbooks
git flow feature start update-integration-test
#Delete local branch
git branch -d feature/E2E-test-implementation
git flow feature publish

Pull the branch in another working directory
git init 
git flow feature track teamcity_integration
git flow feature delete teamcity_integration
git flow finish teamcity_integration


#===================================
grep:
grep --color=auto -r  "word" .

#==================================
iptables:

#==================================
JAVASCRIPT
POST
var data = { "data": "2" };

$.ajax({
    type: "POST",
    url: "http://natgeo-preprod-dev.apigee.net/tenantselector",
    data: JSON.stringify({"hola": "que tal"}),
    contentType: "application/json",
    crossDomain : true,
    dataType: "json",
    success: function(data){alert(data);},
    failure: function(errMsg) {
        alert("ERROR");
    }
});

TESTING
http://www.webtoolkitonline.com/javascript-tester.html
#==================================
Linux:
uname -a
Linux kali 4.9.0-kali4-amd64 #1 SMP Debian 4.9.30-2kali1 (2017-06-22) x86_64 GNU/Linux
uname -r
4.9.0-kali4-amd64
apt-cache search linux-headers-$(uname -r): Verificar headers instalados
apt-get install linux-headers-4.9.0-kali4-amd64: install linux  headers
find  -name edge.json .
mount -t vboxsf SHARE vm/SHARE: mount virtualbox share folder
reboot
shutdown now
ifconfig
TODO check virtual interfaces


debian:

dpkg -l | less
dpgk -i package
#==================================
mysql
#===================================
mvn
mvn install -Pdev -Dusername=$apigee_user -Dpassword=$apigee_pass -Dapigee.config.options=create

#=================================
network manager


#=================================
Neo4j:


si no muestra kvertices  borrar kookies de  (porjemplo de localhost)
chorme->setting-> content->stetting-> all cokkies and site data ->filtrar y remove


curl --user 'neo4j:intel123'   -H Accept:application/json -H Content-Type:application/json -v http://localhost:7474/db/data/

MATCH (n) DETACH DELETE n

MATCH n-[rel:INITIATED]->r 
WHERE n.id=f16dbb74efe0686172e3616f28cb6f47 AND r.id=9a97ad3363def2b8d8603d5174006edd
DELETE rel

MATCH (N:KVertex) RETURN "KVertex",COUNT(N)


MATCH ((kvt:KVertexType)<-[i:INSTANCE_OF]-(kv:KVertex),(kv)-[r:INITIATED]->(ic:InvestigationCase),(r:Rule)-[a:APPLYING]->(ra:RuleApplication), (ra)<-[ir:INPUT]-(kv),
, (ra)-[or:OUTPUT]->(kv)
RETURN kvt.attr__name, kv.attr__name, ic.attr__name, r.attr__name, ra.attr__name 


MATCH (n:KVertex)-[r:INITIATED]->(c:InvestigationCase) where c.id = "efdb1ddc-04f7-49d1-8f31-52d47574ae1c" return n


query para ver cuantas reglas  se ejecutaron correctamente

RULES-RULESAPPLICATION:
MATCH (ra:RuleApplication)<-[ir:INPUT]-(iv: KVertex), (ra)<-[a:APPLYING]-(r:Rule) WHERE ra.attr__state = "completed" RETURN ra,r    
17-30

NOMBRES DE  KVERTEXTYPES NO USADOS
MATCH (kv: KVertexType)
where not kv<-[:LEFT_HAND]-()
RETURN kv.attr__name


RULESAPPLICATION BLOQUEADOS
MATCH (ra:RuleApplication)<-[ir:INPUT]-(iv: KVertex), (ra)<-[a:APPLYING]-(r:Rule) WHERE ra.attr__state = "blocked" RETURN ra,r  



RULESAPPLICATION FAILED
MATCH (ra:RuleApplication) WHERE ra.attr__state = "failed" RETURN ra
0
RULESAPPLICATION COMPLETADOS
MATCH (ra:RuleApplication) WHERE ra.attr__state = "completed" RETURN ra
30

REturn sharedfolder kvertex and its type
$match (kvt:KVertexType)<-[i:INSTANCE_OF]-(kv:KVertex) where kvt.attr__name="SharedFolders" return kvt,kv,i

queryDNSRecord
match (kvt:KVertexType)<-[i:INSTANCE_OF]-(kv:KVertex) where kvt.attr__name="DnsQueryRecord" return kvt,kv,i


UnseenSystemFiles
match (kvt:KVertexType)<-[i:INSTANCE_OF]-(kv:KVertex) where kvt.attr__name="UnseenSystemFiles" return kvt,kv,i

match (kvt:KVertexType)<-[i:INSTANCE_OF]-(kv:KVertex), 
(kvt:KVertexType)<-[i:INSTANCE_OF]-(kv:KVertex)
(kvt2:KVertexType)<-[i2:INSTANCE_OF]-(kv2:KVertex)
where kvt.attr__name="DnsQueryRecord" and kvt2.attr__name="BadReputationIP", kvt2.attr__name="BadReputationIP" 
return kvt, kv, i, kvt2, kv2, i2



MATCH (rav:RuleApplication)<-[inr:INPUT]-(inv: KVertex), (rav)<-[apr:APPLYING]-(ruv: Rule),
    (ruv)-[xhr:LEFT_HAND|:RIGHT_HAND]->(xhv:KVertexType)
        OPTIONAL MATCH (rav)-[rer:RESULT]->(rev: KVertex)-[ior2:INSTANCE_OF]->(xhv)
            WHERE ra.attr__state = "completed"
                RETURN rav, inr, inv, apr, ruv,  rer, rev, ior2
                    
                    
                MATCH (ra:RuleApplication),(r:Rule)-[lh:LEFT_HAND]->(lhv: KVertexType)
                OPTIONAL MATCH (r)-[rh:RIGHT_HAND]->(rhv: KVertexType)
                RETURN r, lh, lhv, rh, rhv  

                MATCH (ra:RuleApplication)-[ir:RESULT]->(iv: KVertex), (ra)<-[a:APPLYING]-(r:Rule),  WHERE ra.attr__state = "completed" RETURN ra,r 



                MATCH (r:Rule {id:"ITTEST_3790950"})-[lh: LEFT_HAND]->(lhv: KVertexType)
                OPTIONAL MATCH (hub: HubKedgesType)-[hrh: HUB_RIGHT_HAND]->(rhv: KVertexType)
                OPTIONAL MATCH (hub: HubKedgesType)-[hke: HUB_KEDGE_TYPE]->(ket: KedgeType)
                OPTIONAL MATCH (nov: Note)-[anr:ANNOTATED]->(r)
                RETURN r, lh, lhv, hub, hrh, rhv, hke, ket, nov, anr    

data='
{
      "query":"MATCH (n) DETACH DELETE n;"
  }
  '
curl -b -j -H "Content-Type: application/json" -d "$data" $HOST:$PORT/neo4j/db/data/cypher  

o 
rm -rf  /var/lib/neo4j/data/databases/


#=================================
Ngnix:
#==================================
npm
wget -N http://nodejs.org/dist/node-latest.tar.gz
tar xzvf node-latest.tar.gz && cd node-v*
./configure
sudo fakeroot checkinstall -y --install=no --pkgversion $(echo $(pwd) | sed -n -re's/.+node-v(.+)$/\1/p') make -j$(($(nproc)+1)) install
sudo dpkg -i node_*
node  -v
npm install json
npm install -g wt-cli
wt init --container "test" --url "https://sandbox.it.auth0.com" --token "ACCESS_TOKEN"
wt logs -p "natgeo-test-default-logs"

#==================================
openssl


#==================================
Postgres:
postgres createuser -P <db_user>;
sudo -u postgres createuser -P <db_user>;
sudo -u postgres createdb <db_name> -O <db_user>;
sudo -u postgres dropdb <db_nbame>	
service postgresql  status/start/restart/stop
psql --version

AUTHENTICATION in psql
sudo -u postgres psql
could not change directory to "/home/luis.vargasb": Permission denied
Password:
psql: FATAL:  password authentication failed for user "postgres"

Fix:
sudo vim /etc/postgresql/9.5/main/pg_hba.conf
Add the first line:
local   all         postgres                          peer

service postgresql restart
Check:
https://stackoverflow.com/questions/7695962/postgresql-password-authentication-failed-for-user-postgres

PSQL interpreter
sudo -u postgres psql

\? list all the commands.
\l list databases.
\conninfo display information about current connection.
\c [DBNAME] connect to new database, e.g., \c template1.
\dt list tables.
\q quit psql.


dropdb db
psql -U db_user -c "drop database db"
psql -U "db_user" -c "drop database db"
psql -c "drop database db"
vim /etc/postgresql/9.6/main/pg_hba.conf
psql -d db -U db_user -W
psql -d db -U db -W
su - postgres
sudo -u postgres createuser -P db
#==================================
Python
wget get_pip.py: TODO COMPLETE
pip --version
pip install virtualenv
pip install virtualenvwrapper
pip install ipython
pip install pygments
pip install ipdb
import ipdb ; ipdb.set_trace()
#Add this lines to .bashrc
# Virtualenwrapper
export WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh


pip list
pip freeze
pip install -r path/to/requirments.txt
pip freeze | xargs pip uninstall -y

pysftp:

sudo apt-get install libssl-dev



json.dumps(kv,indent=4, sort_keys=True))
os.environt[] =
subprocess.check_call

parcial = functools.partial(api_utils.put_entity(context, api_path="case", entity_id=case_id))
map(lambda x: api_utils.save_entity_in_context(context, case_identifier, case_request['links'] + x), parcial(case_request['links'] + x)), [clue for clue in clues])


python

fatal error: Python.h: No such file or directory 	(Using  python3  in virtualenv)
Fix https://stackoverflow.com/questions/21530577/fatal-error-python-h-no-such-file-or-directory

	
Looks like you haven't properly installed the header files and static libraries for python dev. Use your package manager to install them system-wide.

For apt (Ubuntu, Debian...):

sudo apt-get install python-dev   # for python2.x installs
sudo apt-get install python3-dev  # for python3.x installs
For yum (CentOS, RHEL...):

sudo yum install python-devel
For dnf (Fedora...):

sudo dnf install python2-devel  # for python2.x installs
sudo dnf install python3-devel  # for python3.x installs


#==================================
Rabbit:

sudo apt-get install rabbitmq-server
sudo rabbitmqctl add_user members members
sudo service rabbitmqctl status
service rabbitmq-server start
service rabbitmq-server status
sudo rabbitmqctl add_user members members
sudo rabbitmqctl add_vhost /members
sudo rabbitmqctl set_permissions -p /members members "." "." ".*"

#==================================
Redsock:

REDSOCK

Set proxy variables temporarily
echo 'Acquire::http::Proxy "http://proxy-us.intel.com:911";' >> /etc/apt/apt.conf
export HTTP_PROXY=http://proxy-us.intel.com:911
export HTTPS_PROXY=http://proxy-us.intel.com:912
export FTP_PROXY=http://proxy-us.intel.com:911
export SOCKS_PROXY=http://proxy-us.intel.com:1080
export NO_PROXY=intel.com,.intel.com,10.0.0.0/8,192.168.0.0/16,localhost,.local,127.0.0.0/8,134.134.0.0/16

Update and install redsocks
apt-get update && apt-get install redsocks

Setup transparent proxy (you may need to make file executable with chmod +x enable_socks)
cd <METAMORPH_RELEASE>/redsocks
./enable_socks.sh stop
./enable_socks.sh start

ACA YA SE Puede probar

Persist changes
apt-get install iptables-persistent

Copy redsocks.conf to /etc
cp <METAMORPH_RELEASE>/redsocks/redsocks.conf /etc/redsocks.conf


#==================================
SBT

Run project
sbt -Dhttp.nonProxyHosts=localhost run
Run Cassandra (Ver CASSANDRA secction)
sbt -Dhttp.nonProxyHosts=localhost  run -DCASSANDRA_KS=cassandra

Build project
sbt stage universal:packageBin

UT 
sbt clean compile test
coverage
sbt clean coverage test coverageReport

IT
sbt -Dhttp.nonProxyHosts=localhost clean it:test

#==================================
Slurm:
#==================================
ssh

ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
clip < ~/.ssh/id_rsa.pub
ssh -T git@github.com


On the server side

xclip -sel clip < ~/.ssh/id_rsa.pub
touch ~/.ssh/authorized_keys
cat ~/id_rsa.pub >> ~/.ssh/authorized_keys


ssh -i private_key.pem ubuntu@ec2-xx-xxx-xxx-xxx.us-west-2.compute.amazonaws.com
If there is a docker image running into the ec2 instance
ssh -i private_key.pem core@11.0.11.77


docker ps  to show images running in component

Get inside a docker machine
docker exec -ti f56f78eecc07 bash


Analisis dentro del componente:
journalctl grep kube-scheduler
journalctl -u schduler

sudo service supervisor stop
sudo services supervisor start



CREATE CERTIFICATE 
openssl req -x509 -newkey rsa:2048 -keyout 10.218.86.84.pem -out cert.pem -days XXX



#==================================
sublime:

wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-get install apt-transport-https
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install sublime-text

install anaconda,git agila

{
	"auto_indent": true,
	"draw_white_space": "all",
	"font_size": 11,
	"ignored_packages":
	[
		"Vintage"
	],
	"rulers":
	[
		79
	],
	"smart_indent": true,
	"tab_size": 4,
	"theme": "Agila.sublime-theme",
	"trim_automatic_white_space": true,
	"use_tab_stops": true,
	"vintage_start_in_command_mode": true,
	"word_wrap": true,
	"wrap_width": 80,
	"save_on_focus_lost" :true
}


#=================================
tmux
ctrl+b up/down: Move between panels
ctrl+b+s: Switch between session
ctrl+b+\": new horizontal panel
ctrl+b+%: new vertical panel
ctrl+b+d: detach
ctrl+b+\[: search
ctrl+b+\$: rename session
ctrl+b+\:: new session
tmux ls: list sessions
tmux a -t <sesionname>: Attach a session by name
tmux new -s <sessionname>:  new session
tmux rename-session -t <number_session> <new_name_session>


#===================================

#===================================
utils:
sudo apt-get update
sudo apt-get install tree
sudo apt-get install kdiff3
sudo apt-get install lstopo
sudo apt-get install meld
sudo apt-get install htop
sudo apt-get install tmux
sudo apt-get install postgresql
sudo apt-get install ipython
sudo apt-get install xclip

#==================================
vim

:vsp new_file
:vsp existing file
:sp
/word
:ctrl+w -> <- up /down
:set nu
:set nu!
:u
:w
:qw!
:ctrl+r
1234G
yy
dd
:v
:x
set tab (COMPLETE)
:%s/foo/bar/g
#===================================
VirtualBox:


https://unix.stackexchange.com/questions/405862/headers-for-4-12-0-kali1-amd64-or-location-of-kali-4-13-installer

apt-cache search linux-image
apt-cache search linux-headers
Ejemplo  para version 4.14
apt-get install linux-image-4.14.0-kali3-amd64 
apt-cache search linux-headers
apt-get install linux-headers-4.14.0-kali3-amd64 
reboot


#===================================
Virtualenv:
virtualenv -p /usr/bin/python3.6 venv                                                             │

VirtualenvWrapper:
mkvirtualenv venv_name
workon
workon venv_name
deactivate
#==================================
vpn

apt-get install network-manager-{openvpn-gnome,pptp{,-gnome},strongswan,vpnc{,-gnome}}
openvpn --version
vim  ~/.cisco/csd-wrapper.sh
openconnect vpn.ngeo.com --csd-wrapper=/root/.cisco/csd-wrapper.sh



comparar  contra yopmail
https://10minutemail.com/10MinuteMail/index.html?dswid=7296



