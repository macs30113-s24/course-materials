# Lab - Week 4 - Introduction to AWS Compute Resources

## Ex1. `EC2` Basics

In this exercise, we'll launch an EC2 instance, practice running a Python script on it, as well as copying data back and forth between EC2 and our local machine.

1. Launch an EC2 instance via the AWS Console as we demonstrated in class. Select an Amazon Linux 2023 AMI and a t2.nano instance type. Tag your instance with the name `CNETID-lab4` and be sure to add your `vockey` key pair to enable `ssh` login.
2. Connect to your newly launched EC2 instance using SSH (if you haven't already, you will need to download `labsuser.pem` from the `AWS Details` tab in the AWS Academy Learner Lab menu -- click "Download PEM" and move the file to the location on your computer that you will be `ssh`-ing from and change the file permissions via `chmod 400 labsuser.pem`). Remember that your "PEM" file serves as a key into AWS compute instances and only needs to be downloaded and setup once.
    ```bash 
    ssh -i "/path-to-your-key/labsuser.pem" ec2-user@your-instance-public-ip
    ```
3. Type `nano ran_avg.py` and write the following Python program in your EC2 instance terminal:
    ```python
    import random

    n = 10
    ran_sum = 0
    for i in range(n):
        ran_sum += random.random()

    print("Random Average", ran_sum / n)
    ```
4. Try running the program from the EC2 instance terminal with `python3 ran_avg.py`.
5. In another terminal window, copy the script to your local machine via `scp`:
    ```bash
    scp -i "/path-to-your-key/labsuser.pem" ec2-user@your-instance-public-ip:ran_avg.py .
    ```
5. On your local machine, edit `ran_avg.py` so that you generate 100 random numbers instead of just 10. `scp` the file back to your EC2 instance and check to confirm that the script reflects the update:
    ```bash
    scp -i "/path-to-your-key/labsuser.pem" ran_avg.py ec2-user@your-instance-public-ip:.
    ```
6. When you're finished, be sure to ***terminate the instance***.

## Ex2. `Lambda` Functions

1. In the AWS Console, create and deploy an AWS Lambda function that generates a list of prime numbers up to a specified number. The function will return a JSON object containing a status code and the list of primes. The basic function to check if a number is prime is provided. Your task is to complete the lambda_handler function, deploy it to AWS Lambda, and test it.

```python
def is_prime(n):
    """Check if n is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def lambda_handler(event, context):
    # TODO

    return {
        'statusCode': 200,
        'body': list_of_primes
    }
```
- You should expect data that looks like the following as input Event JSONs. When you have written your code for `lambda_handler`, copy-paste your code to Lambda, deploy it, and test it with the following JSON data through the Lambda console:
    ```json
    {
        'number': 200
    }
    ```
2. In this question, we will practice packaging your Python code and deploying it as a Lambda function using `boto3`. Assume you have written Python code that performs a Monte Carlo simulation (a pi simulation like we performed last week) given user input of the number of simulations to perform. Fill in the blanks (and prepare your code for deployment by copying it into a Python script and zipping it up in the expected format) [for the provided `boto3` code](lab4_lambda_step.ipynb) to deploy the code as a Lambda function and invoke the function. If you haven't done so already, note that you will need to copy and paste your AWS CLI credentials into your `credentials` file on your local machine (Go to "AWS Details" in the AWS Academy Learner Lab menu and click "AWS CLI"). Remember that you will need to do this every four-hour lab session hosted through AWS Academy.
    ```python
    import random

    def lambda_handler(event, context):
        # if the user doesn't provide num_points to simulate, assume 10k
        num_points = event.get('num_points', 10000)
        points_inside_circle = 0

        for _ in range(num_points):
            x, y = random.random(), random.random()
            if x**2 + y**2 <= 1:
                points_inside_circle += 1

        pi_estimate = 4 * points_inside_circle / num_points
        return {
            'statusCode': 200,
            'body': {
                'pi_estimate': pi_estimate,
                'num_points': num_points
            }
        }
    ```