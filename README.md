# 🔍 Find AWS Lambda Function Name by Function URL

This script helps you find the AWS Lambda function name that corresponds to a specific **Lambda Function URL** using the AWS SDK (`boto3`).

---

## 📌 Use Case

If you have a Lambda Function URL like:
https://XXXXXX.lambda-url.us-east-1.on.aws/


…but don’t know which Lambda function it belongs to — this script will help you find it.

---

## 📦 Requirements

- Python 3.6 or higher
- `boto3` installed:

  ```bash
  pip install boto3
  ```

## Usage
-	Replace the TARGET_URL with the Lambda Function URL you’re trying to match.
- Run the script:

  ```bash
  python find_lambda_by_url.py
  ```
