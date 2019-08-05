import logging

import azure.functions as func

import random
import statistics

def rand1k():
    my_dict = {}
    rand_list = []
    for i in range(1000):
        rand_no = random.randint(1,101)
        rand_list.append(rand_no)

    my_dict['random_list'] = rand_list
    my_dict['std'] = statistics.stdev(rand_list)
    my_dict['var'] = statistics.variance(rand_list)

    return str(my_dict)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('myfunc HTTP trigger function processed a request.')

    name = req.params.get('flag')
    if name == 'start':
        return func.HttpResponse(rand1k())

    return func.HttpResponse(
            "Please append ?flag=start in the URL to execute the function",
            status_code=400
    )
