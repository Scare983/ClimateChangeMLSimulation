helpFunction() {
    echo ""
    echo "Usage: "
    echo "============================================================="
    echo "| This shell script dynamically changes which agent to look at during before run time."
    echo "| Pass in path to file that you want to use as the agent to test"
    echo "| ei: ./executeSim.sh GHsamples/fileToTest.py"
    echo "| ei: ./executeSim.sh ./GHsamples/otherFolder/fileToTest.py "
    echo "| ----------------------------"
    echo "| Optional input -g -p -y"
    echo "| -g:  randomize values of greenhouse gases "
    echo "| -p:  randomize initial values of policy "
    echo "| -y:  year to start at b/w 1960 and 2014                           "
    echo ""
    echo "| Required Input -o (longitude) -a (latitude) -f (filename)                            "
    echo "Example: "
    echo "  ./executeSim.sh -f GHsamples/defaultAgent.py -o 33.64 -a 77.34 [-g -p-y]"
    echo "============================================================="
    exit 1 
}
## Add functionaility to take in arguments for longitude and latitude.

#f = file, o = longitude, a=latitude, g=greenHouseInitialRandom, p=policyRandomizer
filePath=""
ghr=0
pr=0
long=0
lat=0
year=1960
while getopts "f:o:a:gpy:" opt; do
  case "$opt" in
  f) filePath=$OPTARG
    ;;
  o) long=$OPTARG
    ;;
  a) lat=$OPTARG
    ;;
  g) ghr=1
    ;;
  p) pr=1
    ;;
  y) year=$OPTARG
    ;;
  esac
done
if [ -z "$filePath" ]; then
  helpFunction
fi

if [ $long == "0" ]; then
  helpFunction
fi
if [ $lat == "0" ]; then
  helpFunction
fi
if (("$year" > 1959 )) && (("$year" <= 2014 )); then
  okay=1
else
  helpFunction
fi
if [ -e  $filePath ];then
# Here is where we change things.  
    cp main.py mainCp.py
    #module="$(echo "$filePath" | sed  "s/\//./g")"
    module="$(echo $filePath | sed -r 's/(.*)\/+.*.py/\1/')"
    module="$(echo $module | sed -r 's/\//\./g')"
    #module="$(echo $filePath | sed  "s/\//./g")" 
    fName="$(echo $filePath |  sed -r 's/([A-z]+\/)+(.*).py/\2/')"
    sed -i "s/import GreenHouseAgents.defaultAgent/import $module.$fName/" mainCp.py
    initialSf6=0.000005
    initialCo2=217.592896
    initialN2o=276.889729
    initialCh4=1529.14
    #TODO:  if random is added, change initial GH in main.py
    #TODO: and rates in GreenHouseAgents/ghgControl.py
    # if year not 1960, we have to calculate an initial value using default data.
    cp ../greenHouseRates/OrigGhRates/* ../greenHouseRates/
    if [ "$year" != "1960" ]; then
      diff=$((("$year"-1960)*12 + 1 ))
      echo "$diff"
    fi
    python mainCp.py -a "$lat" -o "$long"


else 
    helpFunction
fi 
