import os
import subprocess

MainPath = "<Main path which contain analyzer main execution file"
inputListMC = os.path.join(MainPath, "input/InputList_MC")
inputListData = os.path.join(MainPath, "input/InputList_Data")
logDir = os.path.join(os.getcwd(), "condorLog")
submitDir = os.path.join(os.getcwd(), "condorSubmit")
runScriptPath = os.path.join(os.getcwd(), "run_analysis.sh")
outputPath = "/pnfs/knu.ac.kr/data/cms/store/user/<user name>/<your own path to store result>"

# Create the necessary directories if they don't exist
os.makedirs(logDir, exist_ok=True)
os.makedirs(submitDir, exist_ok=True)

def submit_jobs(sampleType, inputListPath):

    for sampleDir in os.listdir(inputListPath):
        if(sampleType == "MC"):
            inputDir = f"InputList_MC"
            outputDir = f"MC/{sampleDir}"
        elif(sampleType == "Data"):
            inputDir = f"InputList_Data"
            outputDir = f"Data/{sampleDir}"
        
        submit_file_content = f"""Universe   = vanilla
Executable = {runScriptPath}
Log        = {logDir}/{sampleDir}.log
Output     = {logDir}/{sampleDir}.out
Error      = {logDir}/{sampleDir}.err
RequestMemory = 16 GB
RequestCpus = 1
Arguments  = {MainPath} {inputDir}/{sampleDir} $(InputListName) {outputDir} $(OutputName) {outputPath}
Queue InputListName, OutputName from (
"""
        for listFile in os.listdir(os.path.join(inputListPath, sampleDir)):
            if listFile.endswith(".list"):
                listFileName = os.path.splitext(listFile)[0]
                outputName = f"{listFileName}.root"
                submit_file_content += f"{listFileName} {outputName}\n"

        submit_file_content += ")\n"
        
        submit_file_path = os.path.join(submitDir, f"submit_{sampleDir}.sub")
        with open(submit_file_path, "w") as submit_file:
            submit_file.write(submit_file_content)
        
        subprocess.run(["condor_submit", submit_file_path])

#####################################################

# Submit jobs for MC samples
submit_jobs("MC", inputListMC)

# Submit jobs for Data samples
submit_jobs("Data", inputListData)

#####################################################

