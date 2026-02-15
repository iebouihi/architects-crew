#!/usr/bin/env python
import sys
import warnings
from pathlib import Path

from datetime import datetime

from architects_crew.crew import ArchitectsCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Load requirements from input/requirements.md (relative to project root)
_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
REQUIREMENTS = (_PROJECT_ROOT / "input" / "requirements.md").read_text(encoding="utf-8")

def run():
    """
    Run the crew.
    """
    print(REQUIREMENTS)
    inputs = {
        'requirements': REQUIREMENTS,
    }

    try:
        ArchitectsCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


