import numpy as np
import torch
import random
from scipy import sparse

class ContextualMAB:

    def sigmoid_activation(self, x):

        1 / (1 + np.exp(-x))

    def newtonRaphson(self, function, function_derivative, myGuess, epsilon, max_iterations):

        possibleSolution = myGuess
        for i in range(0, max_iterations):

            fguess = function(possibleSolution)
            if (abs(fguess) < epsilon):
                print("Convergence after ", i, " Iterations")
                return possibleSolution
            function_derivative_guess = function_derivative(possibleSolution)
            if function_derivative_guess == 0:
                print("Zero Derivative, No Solution")
                return None
            possibleSolution = possibleSolution - fguess/function_derivative_guess
        print("Maximum Iterations Exceeded without Convergence")
        return None

    """
    Using the Bayesian Logistic Regression to Update the Training Model
    """
    def bayesianUpdateOfLogisticRegression(self, meansVector, varianceVector, observedRewardsBatch, featureVectorsBatch):

        Q_value = [len(meansVector)]
        prob = []
    
        for i in range(meansVector):

            Q_value[i] = np.linalg.inv(varianceVector[i])

        """
        Updating the Means and Variances for Each Input Dimension
        """
        for i in range(featureVectorsBatch):

            for j in range(meansVector):

                meansVector[j] = np.argmin(1/2 * Q_value(torch.optim.Adam(meansVector[j], lr = 0.001) - meansVector[j]) ** 2) - observedRewardsBatch[i] * np.log(self.sigmoid_activation(torch.optim.Adam(meansVector[j], lr = 0.001) * featureVectorsBatch[i])) + (1 - observedRewardsBatch[i]) * np.log(1 - Q_value(self.sigmoid_activation(torch.optim.Adam(meansVector[j], lr = 0.001) * featureVectorsBatch[i])))


                prob[i] = np.linalg.inv(1 + np.exp(-meansVector[j] * featureVectorsBatch[i]))
                Q_value[j] = Q_value[j] + np.linalg.inv((featureVectorsBatch[i], j)**2 * prob[i]*(1 - prob[i]))
                varianceVector[j] = np.linalg.inv(Q_value[j])


        return meansVector, varianceVector


    def thompsonSampling(self, meansVector, varianceVector, contexts):

        sample_weights = []
        reward = []
        length = len(contexts)
        arms = [length]

        for i in range(meansVector):

            sample_weights[i] = meansVector[i] * varianceVector[i] * np.linalg.inv(contexts[i])
            reward[i] = meansVector[i] * contexts[i]
            
            # Hill Climbing Incorporation
            pass

        

    # def greedyHillClimbing(self, climbingSteps, sample_weights, context):

    #     bernoulli_layers = [random.randrange(0, 2) for i in range(len(context))]

    #     for r in range(len(context)):
            
    #         layout = bernoulli_layers[0:r]

    #         for step in range(climbingSteps):
    #             # This will be when I add this to 
    #             optimal = np.argmax(sample_weights[step] * layout[step - 1], context)

    #             layout[step] = layout[optimal]

    #         if layout[step] == None or layout[step] > layout[r]:

    #             layout = layout[optimal]

    #     return layout

    def randomHillClimbing(self, sample_weights, contexts):

        A = []
        for step in range(len(contexts)):

            r = random.randint(0, len(contexts))
            As0 = A[r]
            for k in range(len(contexts)):
                i = random.randint(0, len(As0))
                randomWidget = As0[i]
                j = np.argmax()




if __name__ == "__main__":

    """
    Two Versions to Vertically Stack Two Ararays
    """
    A = ["Hello", "Hello", "Hello", "Hello"]
    B = [0, 1, 0, 1]
    C = [A,B]
    #print(np.vstack(C))
    #print(np.hstack(C))
    """
    Always use the Longest Array to Resize both Arrays
    """
    X = np.array((A, B))
    X1 = list(X)
    M = np.asmatrix(X1)
    M1 = np.mat(X)
    print(M1)
    print(M[0][2])
