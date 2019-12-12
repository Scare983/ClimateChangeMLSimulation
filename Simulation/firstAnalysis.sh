

rm -rf SimResults/*
fName="SimResults/defaultAgent-1960-$model-0-0-0"
myFileArray=()
myModels=("a" "z" "l" "e" "b")

month=("Jan" "Feb" "Mar" "Apr" "May" "Jun" "Jul" "Aug" "Sep" "Oct" "Nov" "Dec")
./executeSim.sh -f GreenHouseAgents/defaultAgent.py -a 33.25 -o -83.44 -m a >>/dev/null 2>&1
./executeSim.sh -f GreenHouseAgents/defaultAgent.py -a 33.25 -o -83.44 -m z >>/dev/null 2>&1
./executeSim.sh -f GreenHouseAgents/defaultAgent.py -a 33.25 -o -83.44 -m l >>/dev/null 2>&1
./executeSim.sh -f GreenHouseAgents/defaultAgent.py -a 33.25 -o -83.44 -m e >>/dev/null 2>&1
./executeSim.sh -f GreenHouseAgents/defaultAgent.py -a 33.25 -o -83.44 -m b >>/dev/null 2>&1
# for all dirs, we want the MSE,
ada=()
tree=()
lin=()
ensem=()
blin=()
ada+=($(head -n1 -q "SimResults/defaultAgent-1960-a-0-0-0/Jan/MSE.txt"))
ada+=($(head -n1 -q "SimResults/defaultAgent-1960-a-0-0-0/Feb/MSE.txt"))
ada+=($(head -n1 -q "SimResults/defaultAgent-1960-a-0-0-0/Mar/MSE.txt"))
ada+=($(head -n1 -q "SimResults/defaultAgent-1960-a-0-0-0/Apr/MSE.txt"))
ada+=($(head -n1 -q "SimResults/defaultAgent-1960-a-0-0-0/May/MSE.txt"))
ada+=($(head -n1 -q "SimResults/defaultAgent-1960-a-0-0-0/Jun/MSE.txt"))
ada+=($(head -n1 -q "SimResults/defaultAgent-1960-a-0-0-0/Jul/MSE.txt"))
ada+=($(head -n1 -q "SimResults/defaultAgent-1960-a-0-0-0/Aug/MSE.txt"))
ada+=($(head -n1 -q "SimResults/defaultAgent-1960-a-0-0-0/Sep/MSE.txt"))
ada+=($(head -n1 -q "SimResults/defaultAgent-1960-a-0-0-0/Oct/MSE.txt"))
ada+=($(head -n1 -q "SimResults/defaultAgent-1960-a-0-0-0/Nov/MSE.txt"))
ada+=($(head -n1 -q "SimResults/defaultAgent-1960-a-0-0-0/Dec/MSE.txt"))

tree+=($(head -n1 -q "SimResults/defaultAgent-1960-z-0-0-0/Jan/MSE.txt"))
tree+=($(head -n1 -q "SimResults/defaultAgent-1960-z-0-0-0/Feb/MSE.txt"))
tree+=($(head -n1 -q "SimResults/defaultAgent-1960-z-0-0-0/Mar/MSE.txt"))
tree+=($(head -n1 -q "SimResults/defaultAgent-1960-z-0-0-0/Apr/MSE.txt"))
tree+=($(head -n1 -q "SimResults/defaultAgent-1960-z-0-0-0/May/MSE.txt"))
tree+=($(head -n1 -q "SimResults/defaultAgent-1960-z-0-0-0/Jun/MSE.txt"))
tree+=($(head -n1 -q "SimResults/defaultAgent-1960-z-0-0-0/Jul/MSE.txt"))
tree+=($(head -n1 -q "SimResults/defaultAgent-1960-z-0-0-0/Aug/MSE.txt"))
tree+=($(head -n1 -q "SimResults/defaultAgent-1960-z-0-0-0/Sep/MSE.txt"))
tree+=($(head -n1 -q "SimResults/defaultAgent-1960-z-0-0-0/Oct/MSE.txt"))
tree+=($(head -n1 -q "SimResults/defaultAgent-1960-z-0-0-0/Nov/MSE.txt"))
tree+=($(head -n1 -q "SimResults/defaultAgent-1960-z-0-0-0/Dec/MSE.txt"))

lin+=($(head -n1 -q "SimResults/defaultAgent-1960-l-0-0-0/Jan/MSE.txt"))
lin+=($(head -n1 -q "SimResults/defaultAgent-1960-l-0-0-0/Feb/MSE.txt"))
lin+=($(head -n1 -q "SimResults/defaultAgent-1960-l-0-0-0/Mar/MSE.txt"))
lin+=($(head -n1 -q "SimResults/defaultAgent-1960-l-0-0-0/Apr/MSE.txt"))
lin+=($(head -n1 -q "SimResults/defaultAgent-1960-l-0-0-0/May/MSE.txt"))
lin+=($(head -n1 -q "SimResults/defaultAgent-1960-l-0-0-0/Jun/MSE.txt"))
lin+=($(head -n1 -q "SimResults/defaultAgent-1960-l-0-0-0/Jul/MSE.txt"))
lin+=($(head -n1 -q "SimResults/defaultAgent-1960-l-0-0-0/Aug/MSE.txt"))
lin+=($(head -n1 -q "SimResults/defaultAgent-1960-l-0-0-0/Sep/MSE.txt"))
lin+=($(head -n1 -q "SimResults/defaultAgent-1960-l-0-0-0/Oct/MSE.txt"))
lin+=($(head -n1 -q "SimResults/defaultAgent-1960-l-0-0-0/Nov/MSE.txt"))
lin+=($(head -n1 -q "SimResults/defaultAgent-1960-l-0-0-0/Dec/MSE.txt"))

ensem+=($(head -n1 -q "SimResults/defaultAgent-1960-e-0-0-0/Jan/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/defaultAgent-1960-e-0-0-0/Feb/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/defaultAgent-1960-e-0-0-0/Mar/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/defaultAgent-1960-e-0-0-0/Apr/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/defaultAgent-1960-e-0-0-0/May/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/defaultAgent-1960-e-0-0-0/Jun/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/defaultAgent-1960-e-0-0-0/Jul/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/defaultAgent-1960-e-0-0-0/Aug/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/defaultAgent-1960-e-0-0-0/Sep/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/defaultAgent-1960-e-0-0-0/Oct/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/defaultAgent-1960-e-0-0-0/Nov/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/defaultAgent-1960-e-0-0-0/Dec/MSE.txt"))

blin+=($(head -n1 -q "SimResults/defaultAgent-1960-b-0-0-0/Jan/MSE.txt"))
blin+=($(head -n1 -q "SimResults/defaultAgent-1960-b-0-0-0/Feb/MSE.txt"))
blin+=($(head -n1 -q "SimResults/defaultAgent-1960-b-0-0-0/Mar/MSE.txt"))
blin+=($(head -n1 -q "SimResults/defaultAgent-1960-b-0-0-0/Apr/MSE.txt"))
blin+=($(head -n1 -q "SimResults/defaultAgent-1960-b-0-0-0/May/MSE.txt"))
blin+=($(head -n1 -q "SimResults/defaultAgent-1960-b-0-0-0/Jun/MSE.txt"))
blin+=($(head -n1 -q "SimResults/defaultAgent-1960-b-0-0-0/Jul/MSE.txt"))
blin+=($(head -n1 -q "SimResults/defaultAgent-1960-b-0-0-0/Aug/MSE.txt"))
blin+=($(head -n1 -q "SimResults/defaultAgent-1960-b-0-0-0/Sep/MSE.txt"))
blin+=($(head -n1 -q "SimResults/defaultAgent-1960-b-0-0-0/Oct/MSE.txt"))
blin+=($(head -n1 -q "SimResults/defaultAgent-1960-b-0-0-0/Nov/MSE.txt"))
blin+=($(head -n1 -q "SimResults/defaultAgent-1960-b-0-0-0/Dec/MSE.txt"))

len=${#month[@]}
for i in {0..11}; do
  echo -n "${ada[$i]}, "
done
echo ""
for i in {0..11}; do
  echo -n "${ensem[$i]}, "
done
echo ""
for i in {0..11}; do
  echo -n "${lin[$i]}, "
done
echo ""
for i in {0..11}; do
  echo -n "${blin[$i]}, "
done
echo ""
for i in {0..11}; do
  echo -n "${tree[$i]}, "
done

echo "##################################"
echo "##################################"
echo ""

./executeSim.sh -f GreenHouseAgents/randomAgent.py -a 33.25 -o -83.44 -m a >>/dev/null 2>&1
./executeSim.sh -f GreenHouseAgents/randomAgent.py -a 33.25 -o -83.44 -m z >>/dev/null 2>&1
./executeSim.sh -f GreenHouseAgents/randomAgent.py -a 33.25 -o -83.44 -m l >>/dev/null 2>&1
./executeSim.sh -f GreenHouseAgents/randomAgent.py -a 33.25 -o -83.44 -m e >>/dev/null 2>&1
./executeSim.sh -f GreenHouseAgents/randomAgent.py -a 33.25 -o -83.44 -m b >>/dev/null 2>&1
ada=()
tree=()
lin=()
ensem=()
blin=()
ada+=($(head -n1 -q "SimResults/randomAgent-1960-a-0-0-0/Jan/MSE.txt"))
ada+=($(head -n1 -q "SimResults/randomAgent-1960-a-0-0-0/Feb/MSE.txt"))
ada+=($(head -n1 -q "SimResults/randomAgent-1960-a-0-0-0/Mar/MSE.txt"))
ada+=($(head -n1 -q "SimResults/randomAgent-1960-a-0-0-0/Apr/MSE.txt"))
ada+=($(head -n1 -q "SimResults/randomAgent-1960-a-0-0-0/May/MSE.txt"))
ada+=($(head -n1 -q "SimResults/randomAgent-1960-a-0-0-0/Jun/MSE.txt"))
ada+=($(head -n1 -q "SimResults/randomAgent-1960-a-0-0-0/Jul/MSE.txt"))
ada+=($(head -n1 -q "SimResults/randomAgent-1960-a-0-0-0/Aug/MSE.txt"))
ada+=($(head -n1 -q "SimResults/randomAgent-1960-a-0-0-0/Sep/MSE.txt"))
ada+=($(head -n1 -q "SimResults/randomAgent-1960-a-0-0-0/Oct/MSE.txt"))
ada+=($(head -n1 -q "SimResults/randomAgent-1960-a-0-0-0/Nov/MSE.txt"))
ada+=($(head -n1 -q "SimResults/randomAgent-1960-a-0-0-0/Dec/MSE.txt"))

tree+=($(head -n1 -q "SimResults/randomAgent-1960-z-0-0-0/Jan/MSE.txt"))
tree+=($(head -n1 -q "SimResults/randomAgent-1960-z-0-0-0/Feb/MSE.txt"))
tree+=($(head -n1 -q "SimResults/randomAgent-1960-z-0-0-0/Mar/MSE.txt"))
tree+=($(head -n1 -q "SimResults/randomAgent-1960-z-0-0-0/Apr/MSE.txt"))
tree+=($(head -n1 -q "SimResults/randomAgent-1960-z-0-0-0/May/MSE.txt"))
tree+=($(head -n1 -q "SimResults/randomAgent-1960-z-0-0-0/Jun/MSE.txt"))
tree+=($(head -n1 -q "SimResults/randomAgent-1960-z-0-0-0/Jul/MSE.txt"))
tree+=($(head -n1 -q "SimResults/randomAgent-1960-z-0-0-0/Aug/MSE.txt"))
tree+=($(head -n1 -q "SimResults/randomAgent-1960-z-0-0-0/Sep/MSE.txt"))
tree+=($(head -n1 -q "SimResults/randomAgent-1960-z-0-0-0/Oct/MSE.txt"))
tree+=($(head -n1 -q "SimResults/randomAgent-1960-z-0-0-0/Nov/MSE.txt"))
tree+=($(head -n1 -q "SimResults/randomAgent-1960-z-0-0-0/Dec/MSE.txt"))

lin+=($(head -n1 -q "SimResults/randomAgent-1960-l-0-0-0/Jan/MSE.txt"))
lin+=($(head -n1 -q "SimResults/randomAgent-1960-l-0-0-0/Feb/MSE.txt"))
lin+=($(head -n1 -q "SimResults/randomAgent-1960-l-0-0-0/Mar/MSE.txt"))
lin+=($(head -n1 -q "SimResults/randomAgent-1960-l-0-0-0/Apr/MSE.txt"))
lin+=($(head -n1 -q "SimResults/randomAgent-1960-l-0-0-0/May/MSE.txt"))
lin+=($(head -n1 -q "SimResults/randomAgent-1960-l-0-0-0/Jun/MSE.txt"))
lin+=($(head -n1 -q "SimResults/randomAgent-1960-l-0-0-0/Jul/MSE.txt"))
lin+=($(head -n1 -q "SimResults/randomAgent-1960-l-0-0-0/Aug/MSE.txt"))
lin+=($(head -n1 -q "SimResults/randomAgent-1960-l-0-0-0/Sep/MSE.txt"))
lin+=($(head -n1 -q "SimResults/randomAgent-1960-l-0-0-0/Oct/MSE.txt"))
lin+=($(head -n1 -q "SimResults/randomAgent-1960-l-0-0-0/Nov/MSE.txt"))
lin+=($(head -n1 -q "SimResults/randomAgent-1960-l-0-0-0/Dec/MSE.txt"))

ensem+=($(head -n1 -q "SimResults/randomAgent-1960-e-0-0-0/Jan/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/randomAgent-1960-e-0-0-0/Feb/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/randomAgent-1960-e-0-0-0/Mar/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/randomAgent-1960-e-0-0-0/Apr/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/randomAgent-1960-e-0-0-0/May/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/randomAgent-1960-e-0-0-0/Jun/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/randomAgent-1960-e-0-0-0/Jul/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/randomAgent-1960-e-0-0-0/Aug/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/randomAgent-1960-e-0-0-0/Sep/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/randomAgent-1960-e-0-0-0/Oct/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/randomAgent-1960-e-0-0-0/Nov/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/randomAgent-1960-e-0-0-0/Dec/MSE.txt"))

blin+=($(head -n1 -q "SimResults/randomAgent-1960-b-0-0-0/Jan/MSE.txt"))
blin+=($(head -n1 -q "SimResults/randomAgent-1960-b-0-0-0/Feb/MSE.txt"))
blin+=($(head -n1 -q "SimResults/randomAgent-1960-b-0-0-0/Mar/MSE.txt"))
blin+=($(head -n1 -q "SimResults/randomAgent-1960-b-0-0-0/Apr/MSE.txt"))
blin+=($(head -n1 -q "SimResults/randomAgent-1960-b-0-0-0/May/MSE.txt"))
blin+=($(head -n1 -q "SimResults/randomAgent-1960-b-0-0-0/Jun/MSE.txt"))
blin+=($(head -n1 -q "SimResults/randomAgent-1960-b-0-0-0/Jul/MSE.txt"))
blin+=($(head -n1 -q "SimResults/randomAgent-1960-b-0-0-0/Aug/MSE.txt"))
blin+=($(head -n1 -q "SimResults/randomAgent-1960-b-0-0-0/Sep/MSE.txt"))
blin+=($(head -n1 -q "SimResults/randomAgent-1960-b-0-0-0/Oct/MSE.txt"))
blin+=($(head -n1 -q "SimResults/randomAgent-1960-b-0-0-0/Nov/MSE.txt"))
blin+=($(head -n1 -q "SimResults/randomAgent-1960-b-0-0-0/Dec/MSE.txt"))

len=${#month[@]}
for i in {0..11}; do
  echo -n "${ada[$i]}, "
done
echo ""
for i in {0..11}; do
  echo -n "${ensem[$i]}, "
done
echo ""
for i in {0..11}; do
  echo -n "${lin[$i]}, "
done
echo ""
for i in {0..11}; do
  echo -n "${blin[$i]}, "
done
echo ""
for i in {0..11}; do
  echo -n "${tree[$i]}, "
done

echo "##################################"
echo "##################################"
echo ""


./executeSim.sh -f GreenHouseAgents/AccurateAgent.py -a 33.25 -o -83.44 -m a >>/dev/null 2>&1
./executeSim.sh -f GreenHouseAgents/AccurateAgent.py -a 33.25 -o -83.44 -m z >>/dev/null 2>&1
./executeSim.sh -f GreenHouseAgents/AccurateAgent.py -a 33.25 -o -83.44 -m l >>/dev/null 2>&1
./executeSim.sh -f GreenHouseAgents/AccurateAgent.py -a 33.25 -o -83.44 -m e >>/dev/null 2>&1
./executeSim.sh -f GreenHouseAgents/AccurateAgent.py -a 33.25 -o -83.44 -m b >>/dev/null 2>&1
ada=()
tree=()
lin=()
ensem=()
blin=()
ada+=($(head -n1 -q "SimResults/AccurateAgent-1960-a-0-0-0/Jan/MSE.txt"))
ada+=($(head -n1 -q "SimResults/AccurateAgent-1960-a-0-0-0/Feb/MSE.txt"))
ada+=($(head -n1 -q "SimResults/AccurateAgent-1960-a-0-0-0/Mar/MSE.txt"))
ada+=($(head -n1 -q "SimResults/AccurateAgent-1960-a-0-0-0/Apr/MSE.txt"))
ada+=($(head -n1 -q "SimResults/AccurateAgent-1960-a-0-0-0/May/MSE.txt"))
ada+=($(head -n1 -q "SimResults/AccurateAgent-1960-a-0-0-0/Jun/MSE.txt"))
ada+=($(head -n1 -q "SimResults/AccurateAgent-1960-a-0-0-0/Jul/MSE.txt"))
ada+=($(head -n1 -q "SimResults/AccurateAgent-1960-a-0-0-0/Aug/MSE.txt"))
ada+=($(head -n1 -q "SimResults/AccurateAgent-1960-a-0-0-0/Sep/MSE.txt"))
ada+=($(head -n1 -q "SimResults/AccurateAgent-1960-a-0-0-0/Oct/MSE.txt"))
ada+=($(head -n1 -q "SimResults/AccurateAgent-1960-a-0-0-0/Nov/MSE.txt"))
ada+=($(head -n1 -q "SimResults/AccurateAgent-1960-a-0-0-0/Dec/MSE.txt"))

tree+=($(head -n1 -q "SimResults/AccurateAgent-1960-z-0-0-0/Jan/MSE.txt"))
tree+=($(head -n1 -q "SimResults/AccurateAgent-1960-z-0-0-0/Feb/MSE.txt"))
tree+=($(head -n1 -q "SimResults/AccurateAgent-1960-z-0-0-0/Mar/MSE.txt"))
tree+=($(head -n1 -q "SimResults/AccurateAgent-1960-z-0-0-0/Apr/MSE.txt"))
tree+=($(head -n1 -q "SimResults/AccurateAgent-1960-z-0-0-0/May/MSE.txt"))
tree+=($(head -n1 -q "SimResults/AccurateAgent-1960-z-0-0-0/Jun/MSE.txt"))
tree+=($(head -n1 -q "SimResults/AccurateAgent-1960-z-0-0-0/Jul/MSE.txt"))
tree+=($(head -n1 -q "SimResults/AccurateAgent-1960-z-0-0-0/Aug/MSE.txt"))
tree+=($(head -n1 -q "SimResults/AccurateAgent-1960-z-0-0-0/Sep/MSE.txt"))
tree+=($(head -n1 -q "SimResults/AccurateAgent-1960-z-0-0-0/Oct/MSE.txt"))
tree+=($(head -n1 -q "SimResults/AccurateAgent-1960-z-0-0-0/Nov/MSE.txt"))
tree+=($(head -n1 -q "SimResults/AccurateAgent-1960-z-0-0-0/Dec/MSE.txt"))

lin+=($(head -n1 -q "SimResults/AccurateAgent-1960-l-0-0-0/Jan/MSE.txt"))
lin+=($(head -n1 -q "SimResults/AccurateAgent-1960-l-0-0-0/Feb/MSE.txt"))
lin+=($(head -n1 -q "SimResults/AccurateAgent-1960-l-0-0-0/Mar/MSE.txt"))
lin+=($(head -n1 -q "SimResults/AccurateAgent-1960-l-0-0-0/Apr/MSE.txt"))
lin+=($(head -n1 -q "SimResults/AccurateAgent-1960-l-0-0-0/May/MSE.txt"))
lin+=($(head -n1 -q "SimResults/AccurateAgent-1960-l-0-0-0/Jun/MSE.txt"))
lin+=($(head -n1 -q "SimResults/AccurateAgent-1960-l-0-0-0/Jul/MSE.txt"))
lin+=($(head -n1 -q "SimResults/AccurateAgent-1960-l-0-0-0/Aug/MSE.txt"))
lin+=($(head -n1 -q "SimResults/AccurateAgent-1960-l-0-0-0/Sep/MSE.txt"))
lin+=($(head -n1 -q "SimResults/AccurateAgent-1960-l-0-0-0/Oct/MSE.txt"))
lin+=($(head -n1 -q "SimResults/AccurateAgent-1960-l-0-0-0/Nov/MSE.txt"))
lin+=($(head -n1 -q "SimResults/AccurateAgent-1960-l-0-0-0/Dec/MSE.txt"))

ensem+=($(head -n1 -q "SimResults/AccurateAgent-1960-e-0-0-0/Jan/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/AccurateAgent-1960-e-0-0-0/Feb/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/AccurateAgent-1960-e-0-0-0/Mar/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/AccurateAgent-1960-e-0-0-0/Apr/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/AccurateAgent-1960-e-0-0-0/May/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/AccurateAgent-1960-e-0-0-0/Jun/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/AccurateAgent-1960-e-0-0-0/Jul/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/AccurateAgent-1960-e-0-0-0/Aug/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/AccurateAgent-1960-e-0-0-0/Sep/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/AccurateAgent-1960-e-0-0-0/Oct/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/AccurateAgent-1960-e-0-0-0/Nov/MSE.txt"))
ensem+=($(head -n1 -q "SimResults/AccurateAgent-1960-e-0-0-0/Dec/MSE.txt"))

blin+=($(head -n1 -q "SimResults/AccurateAgent-1960-b-0-0-0/Jan/MSE.txt"))
blin+=($(head -n1 -q "SimResults/AccurateAgent-1960-b-0-0-0/Feb/MSE.txt"))
blin+=($(head -n1 -q "SimResults/AccurateAgent-1960-b-0-0-0/Mar/MSE.txt"))
blin+=($(head -n1 -q "SimResults/AccurateAgent-1960-b-0-0-0/Apr/MSE.txt"))
blin+=($(head -n1 -q "SimResults/AccurateAgent-1960-b-0-0-0/May/MSE.txt"))
blin+=($(head -n1 -q "SimResults/AccurateAgent-1960-b-0-0-0/Jun/MSE.txt"))
blin+=($(head -n1 -q "SimResults/AccurateAgent-1960-b-0-0-0/Jul/MSE.txt"))
blin+=($(head -n1 -q "SimResults/AccurateAgent-1960-b-0-0-0/Aug/MSE.txt"))
blin+=($(head -n1 -q "SimResults/AccurateAgent-1960-b-0-0-0/Sep/MSE.txt"))
blin+=($(head -n1 -q "SimResults/AccurateAgent-1960-b-0-0-0/Oct/MSE.txt"))
blin+=($(head -n1 -q "SimResults/AccurateAgent-1960-b-0-0-0/Nov/MSE.txt"))
blin+=($(head -n1 -q "SimResults/AccurateAgent-1960-b-0-0-0/Dec/MSE.txt"))

len=${#month[@]}
for i in {0..11}; do
  echo -n "${ada[$i]}, "
done
echo ""
for i in {0..11}; do
  echo -n "${ensem[$i]}, "
done
echo ""
for i in {0..11}; do
  echo -n "${lin[$i]}, "
done
echo ""
for i in {0..11}; do
  echo -n "${blin[$i]}, "
done
echo ""
for i in {0..11}; do
  echo -n "${tree[$i]}, "
done

echo "##################################"
echo "##################################"
echo ""

