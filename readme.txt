----------------------
Author:  Kevin Linnane
YouTube Demo:
https://www.youtube.com/watch?v=d8bV1liDciw&t=2s

----------------------
This is an extensive project that relates Machine learning with a simulation attached.  
Or to say, the two go hand in hand and results could not be avaliable without the help of both.


All the data you need to do your own processing of the greenhouse gases I have gathered are in data folder.
All other *data* folders inside the project are created from code.

Analysis.ipynb is used to create and save the machine learning models we will be using.  

To run the Simulation there are currently three agents which generate Greenhouse gas data for the Machine learning models.  
There are usage statements for guidance...
------------------
To look at ML model analysis and model creation:
download jupyter notebook and open .ipynb with jupyter

To Run Simulation
------------------
Step 1) 
cd Simulation 

Step 2) 
./executeSimulation -o  (longitude) -a ( latitude) -f (agent to be tested) -m (b|l|a|z|e) [-y (start year) -g -p]
-g is a flag that represents if you want there to be a random initial GH rate for the simulation to start with.  
-m is different machine learning models 
b stands for bayes linear regression
l stands for linear regression
a stands for adaBoost
z stands for tree
e stands for ensemble

Step 3) examples; 
./executeSim.sh -f GreenHouseAgents/defaultAgent.py -a 33.25 -o -83.44 -m b
./executeSim.sh -f GreenHouseAgents/defaultAgent.py -a 33.25 -o -83.44 -m l
./executeSim.sh -f GreenHouseAgents/defaultAgent.py -a 33.25 -o -83.44 -m a
./executeSim.sh -f GreenHouseAgents/defaultAgent.py -a 33.25 -o -83.44 -m z
./executeSim.sh -f GreenHouseAgents/defaultAgent.py -a 33.25 -o -83.44 -m e

./executeSim.sh -f GreenHouseAgents/randomAgent.py -a 33.25 -o -83.44 -m b
./executeSim.sh -f GreenHouseAgents/randomAgent.py -a 33.25 -o -83.44 -m l
./executeSim.sh -f GreenHouseAgents/randomAgent.py -a 33.25 -o -83.44 -m a
./executeSim.sh -f GreenHouseAgents/randomAgent.py -a 33.25 -o -83.44 -m z
./executeSim.sh -f GreenHouseAgents/randomAgent.py -a 33.25 -o -83.44 -m e

Step 4) output
if a policy or chaos occurs, it goes to STD output, however all other data goes to SimResults.

To extend this project copy randomAgent.py in the same folder, with a different name.  And modify the policy/chaos rates which change how GH rates will be during
the simulation!!

Enjoy~
