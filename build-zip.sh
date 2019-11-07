rm -f function.zip

virtualenv v-env #pip3 install virtualenv
source v-env/bin/activate

#pip3 install et_xmlfile
#pip3 uninstall lxml
#pip3 install --upgrade lxml
#pip3 install cssselect
pip3 install volkswagencarnet
pip3 install jsonpickle

deactivate
cd v-env/lib/python3.7/site-packages 
zip -r9 ${OLDPWD}/function.zip .
cd $OLDPWD
zip -g function.zip function.py

