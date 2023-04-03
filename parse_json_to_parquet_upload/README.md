## Pyspark project to parse json files into Parquet

Files:
.env - File contains environment variables.
app.py - Trigger the main()
process.py - Adds new columns year, month, date from created at column
read.py - SparkSession reads the data file using datadir, file pattern(json) and file format name of the file
util.py - Creates spark session
write.py - Writes the data as parquet file in the output dir

## Environment variables:
ENVIRON=DEV
SRC_DIR=/home/saravanan/Projects/DE_on_aws/activity/data/github/landing/ghactivity
SRC_FILE_PATTERN=2021-01-1
SRC_FILE_FORMAT=json
TGT_DIR=/home/saravanan/Projects/DE_on_aws/activity/data/github/raw/ghactivity
TGT_FILE_FORMAT=parquet


###How to call:

The following command starts the spark job in cluster mode and pass the environment variables 

spark-submit \
	--master yarn
	--deploy-mode cluster
	--conf "spark.yarn.appMasterEnv.ENVIRON=PROD" \
	--conf "spark.yarn.appMasterEnv.SRC_DIR=s3://itvsk-github-emr/prod/landing/ghactivity/" \
	--conf "spark.yarn.appMasterEnv.SRC_FILE_FORMAT=json" \
	--conf "spark.yarn.appMasterEnv.TGT_DIR=s3://itvsk-github-emr/prod/raw/ghactivity/" \
	--conf "spark.yarn.appMasterEnv.TGT_FILE_FORMAT=parquet" \
	--conf "spark.yarn.appMasterEnv.SRC_FILE_PATTERN=2021-01-13" \
	--py-files itv-ghactivity.zip	\
	app.py
  
### If app is stroed in s3

The following command uses the app that is stored in s3 and s3 storage is used for data handling
spark-submit \
	--master yarn \
	--deploy-mode cluster \
	--conf "spark.yarn.appMasterEnv.ENVIRON=PROD" \
	--conf "spark.yarn.appMasterEnv.SRC_DIR=s3://notavailable/prod/landing/activity/" \
	--conf "spark.yarn.appMasterEnv.SRC_FILE_FORMAT=json" \
	--conf "spark.yarn.appMasterEnv.TGT_DIR=s3://notavailable/prod/raw/activity/" \
	--conf "spark.yarn.appMasterEnv.TGT_FILE_FORMAT=parquet" \
	--conf "spark.yarn.appMasterEnv.SRC_FILE_PATTERN=2021-01-14" \
	--py-files s3://notavailable/activity-app/activity.zip \
	s3://notavailable/activity-app/app.py
	

