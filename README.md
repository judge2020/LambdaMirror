# LambdaMirror
Use aws lambda to mirror a git repo.


### Usage

1. create a new lambda function with a role with basic execution priviliges and set the runtime to python 3.6.

2. add a "cloudwatch events" trigger to your function

3. click "configuration required" on the trigger

4. Create a rule with type set to "schedule expression" and the expression to "rate(3 hours)" (or change to your desire)

5. click "add" and then the orange "save" button at the top

6. click your lambda function above the trigger you just added

7. replace the contents of the function in the web-IDE with [lambda_function.py](lambda_function.py) 

8. scroll down to the Environment variables section and input the following

|Key|value description|example|
|---|---|---|
|GH_TOKEN|github token, required to push (SSH keys not supported)|abc1243...|
|SOURCE_REPO|the origin (source) github repo|judge2020/lambdaMirror|
|TARGET_REPO|the target github repo|judge2020/MirrorOfLambdaMirror|

9. Under that, go to "basic settings" and configure memory to what you expect is the minimum. Large repositories will require more memory and often much longer execution time. A basic execution costs about 

Stats:

This repo, mirrored to [MirrorOfLambdaMirror](https://github.com/judge2020/MirrorOfLambdaMirror) costs 100 MB and took 25 seconds to execute. Keep this in mind for larer repositories, and adjust your cron/rate accordingly.
