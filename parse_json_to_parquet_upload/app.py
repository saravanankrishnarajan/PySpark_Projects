#import sys
import os
from util import get_spark_session
from read import from_files
from process import transform
from write import to_files

from dotenv import load_dotenv
from pathlib import Path

def main():
    
    dotenv_path = Path('.env')
    load_dotenv(dotenv_path=dotenv_path)

    env = os.environ.get('ENVIRON')
    src_dir = os.environ.get('SRC_DIR')
    src_file_pattern = f'{os.environ.get("SRC_FILE_PATTERN")}*-*'
    src_file_format = os.environ.get('SRC_FILE_FORMAT')
    tgt_dir = os.environ.get('TGT_DIR')
    tgt_file_format = os.environ.get('TGT_FILE_FORMAT')
    
    spark = get_spark_session(env, 'Github Activity - Getting Started')
    
    df = from_files(spark, src_dir, src_file_pattern, src_file_format)    
    #df.printSchema()
    #df.select('repo.*').show()
    
    df_transformed = transform(df)
    #df_transformed.printSchema()
    #df_transformed.show()
    to_files(df_transformed,tgt_dir,tgt_file_format)


if __name__ == '__main__':
    main()
