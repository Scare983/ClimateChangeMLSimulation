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
    echo "  ./executeSim.sh -f (GHsamples/defaultAgent.py) -o (33.64) -a (77.34) -t (outputFolder) [-g -p -y (year) -m (b|l|a|z|e)] "
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
model='b'
while getopts "f:o:a:gpy:hm:" opt; do
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
  h) helpFunction
    ;;
  m) model=$OPTARG
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
    #these values were calculated from Analysis.py which looks at all the greenhouse gases.
    initialSf6=0.000005
    initialCo2=217.592896
    initialN2o=276.889729
    initialCh4=1529.14
    ghArary=($initialCh4  $initialCo2  $initialN2o $initialSf6)
    #TODO:  if random is added, change initial GH in main.py
    #TODO: and rates in GreenHouseAgents/ghgControl.py
    # if year not 1960, we have to calculate an initial value using default data.
    cp ../greenHouseRates/OrigGhRates/* ../greenHouseRates/
    if [ "$year" != "1960" ]; then
      diff1=$((("$year"-1960)*12 + 1 ))
      diff=$(("diff1" -1))
      index=0
      for file in $(ls -p ../greenHouseRates | grep -v /); do
        valuesToSum=$(head -"$diff1" "../greenHouseRates/$file" | tail -"$diff" |  sed "s/.*,//")
        #remove the lines we are calculating so that calulcations done in Simulation have accurate rates to start with.
        sed -i "2,"$(($diff+1))"d" "../greenHouseRates/$file"
        sed -i "2 s/,.*/,0.0/" "../greenHouseRates/$file"
        echo "Calculating new initial GH Values because different date was given..."
        for line in $valuesToSum;do
          value=$(echo "$line")
          iVal=${ghArary[$index]}
          ouput=$(python -c "print ($iVal* $value + ${ghArary[$index]})")
          ghArary["$index"]="$ouput"
        done
        index=$(("$index"+1))
      done
    fi

    # randomize intiial values.
    if (("$ghr" == 1 )); then
      for index1 in 0 1 2 3 ; do
        ghArary["$index1"]="$(python randomNumberGen.py "${ghArary[$index1]}")"


      done
    fi
    simTime=$(((2014-"$year") * 12 + 12 ))
    #pass in SimTime.
    fName="SimResults/$fName-$year-$model-$ghr-$pr-0"
    if [[ -e "$fName" ]] ; then
    i=0
    while [[ -e "$fName-$i" ]] ; do
        let i++
    done
    fName="$fName-$i"
    fi
    mkdir "$fName" 2>/dev/null
    mkdir $fName/Jan $fName/Feb $fName/Mar $fName/Apr $fName/May $fName/Jun $fName/Jul $fName/Aug $fName/Sep $fName/Oct $fName/Nov $fName/Dec
    python mainCp.py -a $lat -o $long -s $simTime -0 ${ghArary[2]} -2 ${ghArary[1]}  -6 ${ghArary[3]} -4 ${ghArary[0]} -y $year -m $model -t $fName #2>/dev/null
    rm mainCp.py

else 
    helpFunction
fi 
