# APY Gateway 

**WIP**: This is heavily work in progress so don't use it for anything other than contributing at the moment :) Stability is certainly not guaranteed.

This is a simple proof of concept tool for creating APIs based on AWS API Gateway and Lambdas using pure python. The main reason for that is to avoid maintaining multiple technology stack yml or json files. For simple APIs this concept seems very viable but for larger projects its effectiveness is questionable (One more reason to test that with this project).  

The main concept is to build a translator for cloudformation templates that essentially defined appropriate resources for building a fully fledged API using only python decorators.

