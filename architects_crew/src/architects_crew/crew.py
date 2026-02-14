from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class ArchitectsCrew():
    """ArchitectsCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def azure_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['azure_architect'], # type: ignore[index]
            verbose=True,
            tracing=True
        )

    @agent
    def aws_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['aws_architect'], # type: ignore[index]
            verbose=True,
            tracing=True
        )

    @agent
    def gcp_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['gcp_architect'], # type: ignore[index]
            verbose=True,
            tracing=True
        )

    @agent
    def head_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['head_architect'], # type: ignore[index]
            verbose=True,
            tracing=True
        )

        # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def create_azure_architecture(self) -> Task:
        return Task(
            config=self.tasks_config['create_azure_architecture'], # type: ignore[index]
        )

    @task
    def create_aws_architecture(self) -> Task:
        return Task(
            config=self.tasks_config['create_aws_architecture'], # type: ignore[index]
        )

    @task
    def create_gcp_architecture(self) -> Task:
        return Task(
            config=self.tasks_config['create_gcp_architecture'], # type: ignore[index]
        )

    @task
    def decide_best_architecture(self) -> Task:
        return Task(
            config=self.tasks_config['decide_best_architecture'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ArchitectsCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            tracing=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
