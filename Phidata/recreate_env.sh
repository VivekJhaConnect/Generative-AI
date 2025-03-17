#Wriet a sripts to delete env and create again and install all dependencies from requirements.txt and path is C:\\Users\\ADMIN\\Documents\\venv\\Scripts\\python.exe

# Delete the env
rm -rf C:\\Users\\ADMIN\\Documents\\venv

# Create a new env
python -m venv C:\\Users\\ADMIN\\Documents\\venv

# Activate the env
source C:\\Users\\ADMIN\\Documents\\venv\\Scripts\\activate

# Install all dependencies from requirements.txt
pip install -r requirements.txt

# how to execute this script in windows
# chmod +x recreate_env.sh
# ./recreate_env.sh



