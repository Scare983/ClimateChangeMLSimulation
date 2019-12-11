helpFunction() {
    echo ""
    echo "Usage: "
    echo "This shell script dynamically changes which agent to look at during run time."
    echo "Pass in path to file that you want to use as the agent to test"
    echo "ei: GHsamples/fileToTest.py"
    echo "ei: GHsamples/otherFolder/fileToTest.py "
    echo ""
    exit 1 
}
## Add functionaility to take in arguments for longitude and latitude.
if  [ $1 ] 
then 
    filePath=$1
else
    helpFunction
fi 

if [ -e  $filePath ]
then 
# Here is where we change things.  
    cp main.py mainCp.py
    #module="$(echo "$filePath" | sed  "s/\//./g")"
    module="$(echo $filePath | sed -r 's/(.*)\/+.*.py/\1/')"
    module="$(echo $module | sed -r 's/\//\./g')"
    echo "$module"
    #module="$(echo $filePath | sed  "s/\//./g")" 
    fName="$(echo $filePath |  sed -r 's/([A-z]+\/)+(.*).py/\2/')"
    sed -i "1 i\from $module import $fName" mainCp.py

    #`python mainCp.py -l -o `


else 
    helpFunction
fi 
