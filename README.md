# LambdaMirror
Use aws lambda to mirror a git repo.


### Usage

1. create a new lambda function with a role with basic execution priviliges and set the runtime to python 3.6.

2. add a "cloudwatch events" trigger to your function

3. click "configuration required" on the trigger

4. Create a rule with type set to "schedule expression" and the expression to "rate(3 hours)" (or your desired rate/cron)

5. click "add" and then the orange "save" button at the top

6. click your lambda function above the trigger you just added

7. download/clone and zip this entire repo, then upload to your lambda function. 

8. scroll down to the Environment variables section and input the following

|Key|value description|example|
|---|---|---|
|GH_TOKEN|github token, required to push (SSH keys not supported)|abc1243...|
|SOURCE_REPO|the origin (source) github repo|judge2020/lambdaMirror|
|TARGET_REPO|the target github repo|judge2020/MirrorOfLambdaMirror|

9. Under that, go to "basic settings" and configure memory to what you expect is the minimum. Large repositories will require more memory and often much longer execution time.

Stats:

This repo, mirrored to [MirrorOfLambdaMirror](https://github.com/judge2020/MirrorOfLambdaMirror) costs 100 MB and took 10 seconds to execute on first run, but only 800 ms on sequential runs (as long as the [container is reused](https://aws.amazon.com/blogs/compute/container-reuse-in-lambda/), also see [The Occasional Chaos of AWS Lambda Runtime Performance](https://blog.symphonia.io/the-occasional-chaos-of-aws-lambda-runtime-performance-880773620a7e)). Keep this in mind for larer repositories, and adjust your cron/rate accordingly.
