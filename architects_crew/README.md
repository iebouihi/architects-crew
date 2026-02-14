# ArchitectsCrew Crew
Welcome to ArchitectsCrew

## Goal of the Project

ArchitectsCrew is a CrewAI crew that turns your system or architecture requirements into cloud architecture designs. It uses multiple AI agents:

- **Azure, AWS, and GCP architects** — Each produces a detailed architecture for your requirements (cost, scalability, security, etc.).
- **Head architect** — Compares the three designs and chooses the best one with a justification.

You provide a single set of requirements (e.g. microservices, constraints, budget, tech stack). The crew outputs architecture documents for each cloud and a final recommendation in the `outputs/` folder.

## Where to Change Requirements

Your requirements are defined in **`src/architects_crew/main.py`** in the **`REQUIREMENTS`** constant (a multi-line string). Edit that string and run the crew again; the same requirements are passed to all tasks and agents.

Example location in code:

```python
REQUIREMENTS = """
We have 2 micorservices Cart & Product.
...
"""
```

To change what the crew does (agents, tasks, flow), see **Customizing** below.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- **Change requirements** — Edit the `REQUIREMENTS` constant in `src/architects_crew/main.py` (see [Where to Change Requirements](#where-to-change-requirements) above).
- Modify `src/architects_crew/config/agents.yaml` to define your agents
- Modify `src/architects_crew/config/tasks.yaml` to define your tasks
- Modify `src/architects_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/architects_crew/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the architects-crew Crew, assembling the agents and assigning them tasks as defined in your configuration.

With the default requirements in `main.py`, the crew produces Azure, AWS, and GCP architecture designs in `outputs/` and a final recommendation in `outputs/best_architectures.md`.

## Understanding Your Crew

The architects-crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the ArchitectsCrew Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
