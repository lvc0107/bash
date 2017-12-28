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

#===================================
Django:
django-admin startproject apiexample
python manage.py migrate
python manage.py runserver 0.0.0.0:3010
python manage.py syncdb --all && python manage.py migrate --fake
python manage.py syncdb && python manage.py migrate
#==================================
docker



#===================================
git:

git config --global user.name "Migue"
git config --global user.email miguelmnr@gmail.com
git mergetool -t kdiff3
git clean -i
git config --global alias.tree 'log --graph --full-history --all --color --date=short --pretty=format:"%Cred%x09%h %Creset%ad%Cblue%d %Creset %s %C(bold)(%an)%Creset"'
git tree
git show <commit_id>
git log
git diff
git mv file1 file2
git checkout file
git checkout branch
git checkout -b <new_branch_name>
git branch
git branch -a
git fetch origin
git stash save "Stash descriptiion"
git stash apply @{NUM} // check stash description
git merge branch_2 (step in branch1)
git merge --no-ff branch_2 (step in branch1)
git mergetool -t kdiff3
TODO study
git revert
git cherry-pick
git rebase --continue
git rebase --abort
git reset 123455666:  this commit is the upper  after reseting : The reseted commits remains as local changes

git reset --hard 123454545 : WARNING: dengeraus operation. All reseted commits are erased

git push -f : WARNING: dengeraus operation. All reseted commits are erased
git push: Check  if changes in severals branches are pushed
git push origin remote_branch: specific push


#==================================
git-flow

#===================================
grep:
grep --color=auto -r  "word" .

#==================================
iptables:

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


#===================================
Postgres:
postgres createuser -P db_user;
sudo -u postgres createuser -P db_user;
sudo -u postgres createdb mmdb -O db_user;
service postgresql  status/start/restart/stop
psql --version

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
Slurm:
#==================================
ssh

ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
clip < ~/.ssh/id_rsa.pub
ssh -T git@github.com

#==================================
sublime:

wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-get install apt-transport-https
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install sublime-text

#=================================
tmux
ctrl+b up/down: Move between panels
ctrl+b+s: Switch between session
ctrl+b+\": new horizontal panel
ctrl+b+%: new vertical panel
ctrl+b+d: detach
ctrl+b+\[: search
tmux ls: list sessions
tmux a -t <sesionname>: Attach a session by name
tmux new -s <sessionname>:  new session
tmux rename <sessionname> <new_sessionname>: rename session
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

apt-get upgrade -y
apt-get dist-upgrade -y
apt-get install linux-headers-$(uname -r)
chmod 755 ./VBoxLinuxAdditions.run
./VBoxLinuxAdditions.run

#===================================
Virtualenv:
virtualenv -p /usr/bin/python3.6 venv                                                             │
workon
#==================================
vpn

apt-get install network-manager-{openvpn-gnome,pptp{,-gnome},strongswan,vpnc{,-gnome}}
openvpn --version
vim  ~/.cisco/csd-wrapper.sh
openconnect vpn.ngeo.com --csd-wrapper=/root/.cisco/csd-wrapper.sh




