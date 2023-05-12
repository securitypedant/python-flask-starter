import json
import logging
from flask import jsonify, request

logger = logging.getLogger("myapp")

def ajax_getdata():
    logger.info("Calling ajax function")

    returnResult = jsonify(data)
    
    return returnResult