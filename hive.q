CREATE EXTERNAL TABLE s3_popularity_ranking(
    page_title string,
    date_accessed string,
    views_by_date string,
    total_views string,
    popularity_trend string
) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n'
LOCATION 's3://hdfsoutput/step-test-2/';

CREATE EXTERNAL TABLE popularity_ranking (
    col1 string,
    col2 string,
    col3 string,
    col4 string,
    col5 string
)
STORED BY 'org.apache.hadoop.hive.dynamodb.DynamoDBStorageHandler' 
TBLPROPERTIES (
    "dynamodb.table.name" = "popularity_ranking",
    "dynamodb.region" = "us-west-2",
    "dynamodb.column.mapping" = "col1:page_title,col2:date_accessed,col3:views_by_date,col4:total_views,col5:popularity_trend");

INSERT OVERWRITE TABLE popularity_ranking SELECT * FROM s3_popularity_ranking;

INSERT OVERWRITE DIRECTORY 's3://hdfs-hive-output/hive-test-1' ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' SELECT * FROM popularity_ranking;