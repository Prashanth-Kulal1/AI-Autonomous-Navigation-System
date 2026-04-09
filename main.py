from simulation.environment import Environment
from simulation.agent import Agent
from src.path_planning.astar import astar

def main():
    env = Environment(20, 20)
    agent = Agent((0, 0), (19, 19))

    grid = env.get_grid()

    path = astar(grid, agent.start, agent.goal)

    if path:
        env.run_simulation(agent, path)
    else:
        print("No path found!")

if __name__ == "__main__":
    main()