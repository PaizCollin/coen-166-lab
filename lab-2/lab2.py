import unittest

class Agent:

    def __init__(self, state, sequence):
        self.state = state
        self.sequence = sequence
        self.cost = 0

    def goal(self, state):
        if(state[0] == "Clean" and state[1] == "Clean"):
            return True
        else:
            return False

    def action(self):
        location = self.state[2]
        
        if(self.state[location] == "Dirty"):
            action = "Suck"
        elif(location == 0):
            action = "Right"
        elif(location == 1):
            action = "Left"
        
        return action

    def changeState(self, state, action):
        location = state[2]

        if(action == "Suck"):
            state[location] = "Clean"
        elif(action == "Right"):
            state[2] = 1
        elif(action == "Left"):
            state[2] = 0

        return state

    def getSequence(self):
        while True:
            if(self.goal(self.state)):
                return self.sequence
            self.cost += 1
            action = self.action()
            self.sequence.append(action)
            self.state = self.changeState(self.state, action)

    def getCost(self):
        return self.cost



class TestLab2(unittest.TestCase):
    def test1(self):
        agent1 = Agent(["Clean", "Clean", 0], [])
        seq1 = agent1.getSequence()
        cost1 = agent1.getCost()
        seq1_exp = []
        cost1_exp = 0
        self.assertEqual(seq1, seq1_exp)
        self.assertEqual(cost1, cost1_exp)

    def test2(self):
        agent2 = Agent(["Clean", "Clean", 1], [])
        seq2 = agent2.getSequence()
        cost2 = agent2.getCost()
        seq2_exp = []
        cost2_exp = 0
        self.assertEqual(seq2, seq2_exp)
        self.assertEqual(cost2, cost2_exp)

    def test3(self):
        agent3 = Agent(["Clean", "Dirty", 0], [])
        seq3 = agent3.getSequence()
        cost3 = agent3.getCost()
        seq3_exp = ["Right", "Suck"]
        cost3_exp = 2
        self.assertEqual(seq3, seq3_exp)
        self.assertEqual(cost3, cost3_exp)

    def test4(self):
        agent4 = Agent(["Clean", "Dirty", 1], [])
        seq4 = agent4.getSequence()
        cost4 = agent4.getCost()
        seq4_exp = ["Suck"]
        cost4_exp = 1
        self.assertEqual(seq4, seq4_exp)
        self.assertEqual(cost4, cost4_exp)

    def test5(self):
        agent5 = Agent(["Dirty", "Clean", 0], [])
        seq5 = agent5.getSequence()
        cost5 = agent5.getCost()
        seq5_exp = ["Suck"]
        cost5_exp = 1
        self.assertEqual(seq5, seq5_exp)
        self.assertEqual(cost5, cost5_exp)

    def test6(self):
        agent6 = Agent(["Dirty", "Clean", 1], [])
        seq6 = agent6.getSequence()
        cost6 = agent6.getCost()
        seq6_exp = ["Left", "Suck"]
        cost6_exp = 2
        self.assertEqual(seq6, seq6_exp)
        self.assertEqual(cost6, cost6_exp)

    def test7(self):
        agent7 = Agent(["Dirty", "Dirty", 0], [])
        seq7 = agent7.getSequence()
        cost7 = agent7.getCost()
        seq7_exp = ["Suck", "Right", "Suck"]
        cost7_exp = 3
        self.assertEqual(seq7, seq7_exp)
        self.assertEqual(cost7, cost7_exp)

    def test8(self):
        agent8 = Agent(["Dirty", "Dirty", 1], [])
        seq8 = agent8.getSequence()
        cost8 = agent8.getCost()
        seq8_exp = ["Suck", "Left", "Suck"]
        cost8_exp = 3
        self.assertEqual(seq8, seq8_exp)
        self.assertEqual(cost8, cost8_exp)


if __name__ == '__main__':
    unittest.main()