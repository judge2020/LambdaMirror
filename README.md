### Lambda Mirror

a tool for AWS Lambda to mirror (backup) a GitHub repository to another repository. 

This currently is limited to GitHub and personal access tokens. Support for SSH and non-GitHub may be added in the future.


#### Requirements

* AWS cli
* [serverless](https://serverless.com/framework/docs/providers/aws/guide/installation/)


#### USAGE

1. `yarn install`
2. copy `.env.example` to `.env` and fill in the parameters
3. `serverless deploy`

The format of the source and target repo is `github_username/repo_name`, eg `judge2020/lambdamirror` (capitalization does not matter)
