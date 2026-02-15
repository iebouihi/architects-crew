# ArchitectsCrew Crew
Welcome to ArchitectsCrew

## Goal of the Project

ArchitectsCrew is a CrewAI crew that turns your system or architecture requirements into cloud architecture designs. It uses multiple AI agents:

- **Azure, AWS, and GCP architects** — Each produces a detailed architecture for your requirements (cost, scalability, security, etc.).
- **Head architect** — Compares the three designs and chooses the best one with a justification.

You provide a single set of requirements (e.g. microservices, constraints, budget, tech stack). The crew outputs architecture documents for each cloud and a final recommendation in the `outputs/` folder.

## Input: requirements

Requirements are read from **`input/requirements.md`** at runtime. Edit that file with your business and technical requirements (tables, bullet points, or prose), then run the crew; the same content is passed to all tasks and agents.

Example: use the provided `input/requirements.md` as a template (business requirements, technical requirements, budget, throughput, compliance, etc.). To change what the crew does (agents, tasks, flow), see **Customizing** below.

## Agents used

The crew uses four agents defined in `src/architects_crew/config/agents.yaml`:

| Agent | Role | Purpose |
|-------|------|--------|
| **azure_architect** | Azure Senior Architect | Designs a detailed Azure architecture from the requirements (efficiency, security, scalability). Uses `openai/gpt-5-mini`. |
| **aws_architect** | AWS Senior Architect | Designs a detailed AWS architecture from the requirements (efficiency, security, scalability). Uses `openai/gpt-5-mini`. |
| **gcp_architect** | GCP Senior Architect | Designs a detailed GCP architecture from the requirements (efficiency, security, scalability). Uses `google/gemini-2.5-flash`. |
| **head_architect** | Head Architect | Compares the three cloud designs and selects **one** best architecture, with justification based on cost, performance, scalability, and security. Uses `openai/gpt-5.1`. |

The three cloud architects run in parallel; the head architect runs after them to produce the final recommendation.

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

**API keys (`.env`)**  
Add the following to your `.env` file. Which keys you need depends on the LLMs set in `config/agents.yaml`:

| Variable | Used by | Required for |
|----------|--------|--------------|
| `OPENAI_API_KEY` | Azure architect, AWS architect, Head architect | `openai/*` models (e.g. gpt-5-mini, gpt-5.1) |
| `GEMINI_API_KEY` | GCP architect | `google/*` models (e.g. gemini-2.5-flash) |

If you switch agents to other providers (Anthropic, Groq, etc.), add the corresponding API key (e.g. `ANTHROPIC_API_KEY`, `GROQ_API_KEY`) to `.env` as needed.

- **Change requirements** — Edit `input/requirements.md` (see [Input: requirements](#input-requirements) above).
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

With the requirements in `input/requirements.md`, the crew produces Azure, AWS, and GCP architecture designs in `outputs/` (`azure_architecture.md`, `aws_architecture.md`, `gcp_architecture.md`) and a final recommendation in `outputs/architecture_decision.md`.

## Understanding Your Crew

The architects-crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the ArchitectsCrew Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
