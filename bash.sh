# install requirements
pip install -r requirements.txt

# set src to PYTHONPATH
export PYTHONPATH=${PWD}

mkdir data
mkdir logs
touch logs/log

# run app
python src/app.pys