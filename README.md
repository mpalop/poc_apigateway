# POC Api gateway

**NOTE**: This is an WIP README
This is the code I made for testing a api-gateway -> lambda (python) stack. The README now is just a mess. I will tidy it out.

NOTE: remember to document how to install redis package into lambdas folders  
pip3 install redis --prefix ./lambda-sort
pip3 install redis --prefix ./lambda-statistics

development environment), that accept an event like: 

- ohpen-sort-Development (because I am in Development environment), that accept an event like: 
```json
{ "sortoption": "ASCENDING|DESCENDING|NOSORT", 
  "text": "free utf-8 text"
}
```

and returns a Json list of the words orderd, aside of the persistence:

```json
{
    "Code": "edb9d70a2d3991f6844713a234c02aee",
    "Text": [
      "8",
      "a",
      "acción",
      "for",
      "is",
      "just",
      "simple",
      "some",
      "text",
      "this",
      "using",
      "utf",
      "with"
    ]
 }
```

- ohpen-statistics-Development (same reason). It accept events like: 

```json
{ 
  "text": "free utf-8 text"
}
```

and return a Json Object like the following: 
```json
{
    "Code": "c8546860c6342639dca78136ecfcab5a",
    "Text": {
      "words": 13,
      "hyphens": 3,
      "spaces": 9
}
```

* The persistence: 

  - I Calculate the hash of the text and use it as a code, in order to put together the sorting and the statistics results.
  - I save the results in S3, into a folder with the hash code. In this folder I save: 
  	- Original.json: file with the text original
	- Sorted.json: file with the Json list with the ordered words 
	- TextStatistics.json: file with the statistics 
  - I save this code and the state about the generation of both operations in a redis (Elastic Cache). Every time a new call arises, I check it on Redis to just save on S3 the necessary.
* Having the code, my idea was giving public read access to S3 bucket and, once you have your code, you can recover the files using the right URL. Not done, neither.	
* In order to do the lambdas availables I configured a API Gateway (It was the fist one I configure, I must say). It took a lot of time to configure, but I did it. Everything was well until I hit with an annoying bug that, even if Lambdas return correctly, API Gateway throws a weird Error.

As a summary, things I did: 
* VPC, because we have to persist data into a Elastic Cache, and I want to do this well
* the Persitence S3 bucket -> mpalop-ohpen-development
* Elastic Cache Redis
* IAM Roles and security groups necessaries
* Generated the lambdas that make that operations, configuring them ables to work into the VPC 
* API Gateway as a FrontEnd of the Lambdas (buggy)
* All orchestrated using Cloudformation netsted stacks to make things clear
* scripts (bin folder) to manage the deploy:
  - create-lambda-sort.sh -> to pack the sort lambda and let ir ready to deploy with cloudformation
  - create-lambda-statistics.sh -> the same as above, but with statistics lambda 
  - deploy.shclear -> to perform the deploy of the cloudformation stack. It needs some parameters:
    - IAM_Profile
	- Environment: Production|Development 
	- Action:create|update

