# carnet-aws-lambda

AWS lambda that uses the [robinostlund/volkswagencarnet](https://github.com/robinostlund/volkswagencarnet) library.


## Build zip file
```bash
./build-zip.sh
```

## Run locally

```bash
# install dependencies
pip3 install volkswagencarnet
pip3 install jsonpickle

# set we-connect username and password
export USER=username
export PASS=password
python3 function.py
```

## Deploying to AWS Lambda

```bash
# build the zip file
./build-zip.sh

```

**NOTE!** 

You might get a error when running
the lambda that says:
```
Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
```

As a workaround, you can edit
`v-env/lib/python3.7/site-packages/volkswagencarnet.py` and replace:

```diff
-bs = BeautifulSoup(req.text, 'lxml')
+bs = BeautifulSoup(req.text, 'html.parser')
```

on line 103 and 136 (2019-11-07)

See: https://github.com/robinostlund/volkswagencarnet/issues/7

After this is done, you can manually add it back to the zip file with:
```bash
cd v-env/lib/python3.7/site-packages 
zip -r9 ${OLDPWD}/function.zip .
cd $OLDPWD
zip -g function.zip function.py
```

Now, the zip file can be deployed as an AWS Lambda.