# Codes for CPV Analysis

## Structure
- **Execution script:** `run_analysis.sh`
- **Script for job submission:** `submit_jobs.py`

## Instructions
- Modify the environment variables in `run_analysis.sh`.
- Several paths that need to be changed are globally declared at the top of `submit_jobs.py`.
- Create a separate directory for these Git codes. When the job starts, `Log` and `submit` directories will be created.
- Set the location of the executable files for the analysis code to the main path and specify the output path.

## Sample List Structure
- Create directories for MC and Data under the input directory of the main path.
- Create directories for various samples.
- Place the `.list` files under these directories.

### Example Sample List Structure
input/
└── input_MC/
├── TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/
└── ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_7.list
