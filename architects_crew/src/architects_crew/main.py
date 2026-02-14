#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from architects_crew.crew import ArchitectsCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

REQUIREMENTS = """
We have 2 micorservices Cart & Product.
Cart service is a microservice that is responsible for the cart functionality.
Product service is a microservice that is responsible for the product functionality.
No direct communication between the two services is allowed and we want to use event driven architecture.
The service are writen in Sping boot.
We have limited budget of 500$ / months to supports 1000 requests /mins for Cart & 5000 requests/mins per Product
"""

def run():
    """
    Run the crew.
    """
    inputs = {
        'requirements': REQUIREMENTS,
    }

    try:
        ArchitectsCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


