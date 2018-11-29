#!/bin/bash

the_api_base="https://nxxjjtbse3.execute-api.us-east-1.amazonaws.com/test"

curl -X POST -d "{\"sortoption\":\"ASCENDING\",\"text\":\"mas esdrújulo texto 2, ínclito eñe àcido.df\"}" $the_api_base/sort
curl -X POST -d "{\"text\":\"mas esdrújulo texto 2, ínclito eñe àcido.df\"}" $the_api_base/statistics



