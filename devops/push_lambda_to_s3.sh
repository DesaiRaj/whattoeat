#!/bin/bash

function create_zip_with_dependencies {
  LAMBDA="$1"
  echo "$LAMBDA"
  TARGET_LAMBDA="$2"
  ROOT=$PWD
  echo "$ROOT"
  cd "$ROOT"/"$LAMBDA" || exit
  pip3 install --target .package -r requirements.txt
  echo "Successfully Installed Python Dependencies"
  zip "$LAMBDA".zip -r * -x .* -x __pycache__
  cd .package || exit
  zip -g ../"$LAMBDA".zip -r .
  echo "Successfully created ZIP"
  cd "$ROOT" || exit
  cp "$ROOT"/"$LAMBDA"/"$LAMBDA".zip "$TARGET_LAMBDA"-"$CI_COMMIT_REF_NAME"-"$COMMIT_SHA".zip
  echo "Successfully created ZIP file $TARGET_LAMBDA-$CI_COMMIT_REF_NAME-$COMMIT_SHA.zip"
}


function push_zip_to_s3 {
  aws s3 cp "$1"-"$CI_COMMIT_REF_NAME"-"$COMMIT_SHA".zip s3://"$AWS_S3_BUCKET"/"$1"/"$1"-"$CI_COMMIT_REF_NAME"-"$CI_COMMIT_SHA".zip --acl bucket-owner-full-control
  echo "Successfully pushed ZIP to s3://$AWS_S3_BUCKET/$1/$1-$CI_COMMIT_REF_NAME-$CI_COMMIT_SHA.zip"
  sleep 5
  aws lambda update-function-code --function-name "$1" --s3-bucket "$AWS_S3_BUCKET" --s3-key "$1"/"$1"-"$CI_COMMIT_REF_NAME"-"$CI_COMMIT_SHA".zip
}

AWSCLI_VERSION='1.18.14'
create_zip_with_dependencies suggestion suggestion


pip install --quiet --no-cache-dir awscli==${AWSCLI_VERSION}
push_zip_to_s3 suggestion