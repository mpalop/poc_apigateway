#!/bin/bash

the_api_base="https://czxdinv8j8.execute-api.us-east-1.amazonaws.com/Development"

curl -X POST -d "{\"sortoption\":\"ASCENDING\",\"text\":\"mas esdrújulo texto, ínclito eñe àcido.df\"}" $the_api_base/sort
curl -X POST -d "{\"text\":\"mas fff esdrújulo texto, ínclito eñe àcido.df\"}" $the_api_base/statistics

