import GreenHouseAgents.ghgControl as ghgControl
from random import random
import numpy as np
with open('./RandomSeedValue.txt') as f:
    value = f.readline()
np.random.seed(int(value))
class sf6Control(ghgControl.ghgControl):
    def __init__(self, sf6RateFName, initialSf6, initialPolicyPercent=.01, initialChaosPercent=.01):
        super().__init__(sf6RateFName, initialSf6)
        self.policyCount = 0
        self.initialPolicyPercent = initialPolicyPercent
        self.initialChaosPercent = initialChaosPercent
        # only one policy allowed to be created for a GH gas.  Change this rate if wanted.
        self.chaosPercent = initialChaosPercent
        # rate at which we may create a policy each month.
        self.policyPercent = initialPolicyPercent
        self.chaosInProgress = False
        self.policyInProgress = False

    #gets next GHRate we will be using as base.
    def getGHRate(self):
        return super().popNextRate()
    # calculate is called from main simulation.
    def calculateNextGh(self):
        rate = self.changePolicyChaos()
        myCumVal = super().getCumValue()
        #multiply by initial value
        #print(super().getCumValue())
        GHval = (myCumVal * rate) + myCumVal
        super().addToCumSum(GHval)
        return GHval

    # Method to Change, checks threshold of policy and changes the percent.
    def changePolicyChaos(self):
        # If policy in progress, we slowly decrease GH gases and don't change the initial rate.
        # once policy complete, change it back to initial value
        rate = self.getGHRate()
        chaos = self.getChaosPercent()
        policy = self.getPolicyPercent()
        # print(policy)
        ### THESE TWO CAN BE FLIPpED IN IF STATEMENT AND IT WILL DETERMINE DIFFERENT RATES FOR THE GH GAS.  Do you want more politcally correct? swap policy first.
        if self.chaosInProgress:
            myYear, myMonth  = ghgControl.ghgControl.getSimTime()
            if self.endChaosTime == myYear and self.startPolicyMonth == myMonth:
                self.chaosInProgress=False
                self.setChaosPercent(self.initialPolicyPercent)
            else:
                rate = rate + abs(rate*self.chaosChange)
        # arbitrary value, it is a threshold.
        elif chaos > .6:
            self.createChaos()
            rate = rate + abs(rate*self.chaosChange)
        #increase chaos
        else:
            self.setChaosPercent(chaos + np.random.normal(.01, .03))
        if self.policyInProgress:
            myYear, myMonth  = ghgControl.ghgControl.getSimTime()
            # we lower rate right here...
            if self.endPolicyTime == myYear and self.startPolicyMonth == myMonth:
                self.policyInProgress=False
                self.setPolicyPercent(self.initialPolicyPercent)
            else:
                rate = rate - abs(rate*self.policyChange)
        # arbitrary value, it is a threshold.
        elif policy > .4:
            self.createPolicy()
            rate = rate - abs(rate*self.policyChange)
        else:
            self.setPolicyPercent(policy + np.random.normal(.01, .03))
            #increase policy

        return rate

    # create a GH diminishing policy to take effect in a time period (checks within this method, helper).  One the "grace period" is over, the rates are maintained.
    def createPolicy(self):
        #check conditions if policy needs to be created.
        #if it needs to be created (the policy can be desired minimum average increase in a greenhouse gas), then set the minimum
        # if it is in progress, attempt to lower the rates.
        #once policy is complete.  The gas cannot exceed the policy, but can be redacted
        policyTimeSpan = np.random.randint(1, 20)
        #start year
        startTimeYear, self.startPolicyMonth = ghgControl.ghgControl.getSimTime()
        self.endPolicyTime = startTimeYear + policyTimeSpan
        self.policyChange = np.random.normal(.015,.012)
        self.policyInProgress = True

    def createChaos(self):
        chaosTimeSpan = np.random.randint(1, 5)
        #start year
        startChaosYear, self.startChaosMonth = ghgControl.ghgControl.getSimTime()
        self.endChaosTime = startChaosYear + chaosTimeSpan
        self.chaosChange = .0006
        self.chaosInProgress = True

    def getChaosPercent(self):
        return self.chaosPercent
    def getPolicyPercent(self):
        return self.policyPercent

    def setPolicyPercent(self, percent):
        self.policyPercent = percent
    def setChaosPercent(self, percent):
        self.chaosPercent = percent


class ch4Control(ghgControl.ghgControl):
    def __init__(self, ch4RateFname, initialCh4, initialPolicyPercent=.01, initialChaosPercent=.01):
        super().__init__(ch4RateFname, initialCh4)

        self.policyCount = 0
        self.initialPolicyPercent = initialPolicyPercent
        self.initialChaosPercent = initialChaosPercent
        # only one policy allowed to be created for a GH gas.  Change this rate if wanted.
        self.chaosPercent = initialChaosPercent
        # rate at which we may create a policy each month.
        self.policyPercent = initialPolicyPercent
        self.chaosInProgress = False
        self.chaosComplete =True
        self.policyInProgress = False
        self.policyComplete = True
    #gets next GHRate we will be using as base.
    def getGHRate(self):
        return super().popNextRate()
    # calculate is called from main simulation.
    def calculateNextGh(self):
        rate = self.changePolicyChaos()
        myCumVal = super().getCumValue()
        #multiply by initial value
        #print(super().getCumValue())
        GHval = (myCumVal * rate) + myCumVal
        super().addToCumSum(GHval)
        return GHval

    # Method to Change, checks threshold of policy and changes the percent.
    def changePolicyChaos(self):
        # If policy in progress, we slowly decrease GH gases and don't change the initial rate.
        # once policy complete, change it back to initial value
        rate = self.getGHRate()
        chaos = self.getChaosPercent()
        policy = self.getPolicyPercent()
        ### THESE TWO CAN BE FLIPpED IN IF STATEMENT AND IT WILL DETERMINE DIFFERENT RATES FOR THE GH GAS.  Do you want more politcally correct? swap policy first.
        if self.chaosInProgress:
            myYear, myMonth  = ghgControl.ghgControl.getSimTime()
            if self.endChaosTime == myYear and self.startPolicyMonth == myMonth:
                self.chaosInProgress=False
                self.setChaosPercent(self.initialPolicyPercent)
            else:
                rate = rate + abs(rate*self.chaosChange)
        # arbitrary value, it is a threshold.
        elif chaos > .6:
            self.createChaos()
            rate = rate + abs(rate*self.chaosChange)
        #increase chaos
        else:
            self.setChaosPercent(chaos + np.random.normal(.01, .03))

        if self.policyInProgress:
            myYear, myMonth  = ghgControl.ghgControl.getSimTime()
            # we lower rate right here...
            if self.endPolicyTime == myYear and self.startPolicyMonth == myMonth:
                self.policyInProgress=False
                self.setPolicyPercent(self.initialPolicyPercent)
            else:
                rate = rate - abs(rate*self.policyChange)
        # arbitrary value, it is a threshold.
        elif policy > .4:
            self.createPolicy()
            rate = rate - abs(rate*self.policyChange)
        else:
            self.setPolicyPercent(policy + np.random.normal(.01, .03))
            #increase policy
        return rate

    # create a GH diminishing policy to take effect in a time period (checks within this method, helper).  One the "grace period" is over, the rates are maintained.
    def createPolicy(self):
        #check conditions if policy needs to be created.
        #if it needs to be created (the policy can be desired minimum average increase in a greenhouse gas), then set the minimum
        # if it is in progress, attempt to lower the rates.
        #once policy is complete.  The gas cannot exceed the policy, but can be redacted
        policyTimeSpan = np.random.randint(1, 20)
        #start year
        startTimeYear, self.startPolicyMonth = ghgControl.ghgControl.getSimTime()
        self.endPolicyTime = startTimeYear + policyTimeSpan
        self.policyChange = np.random.normal(.015,.012)
        self.policyInProgress = True

    def createChaos(self):
        chaosTimeSpan = np.random.randint(1, 5)
        #start year
        startChaosYear, self.startChaosMonth = ghgControl.ghgControl.getSimTime()
        self.endChaosTime = startChaosYear + chaosTimeSpan
        self.chaosChange = .0006
        self.chaosInProgress=True

    def getChaosPercent(self):
        return self.chaosPercent
    def getPolicyPercent(self):
        return self.policyPercent

    def setPolicyPercent(self, percent):
        self.policyPercent = percent
    def setChaosPercent(self, percent):
        self.chaosPercent = percent


class co2Control(ghgControl.ghgControl):
    def __init__(self, co2RateFName, initialCo2, initialPolicyPercent=.01, initialChaosPercent=.01):
        super().__init__(co2RateFName, initialCo2)

        self.policyCount = 0
        self.initialPolicyPercent = initialPolicyPercent
        self.initialChaosPercent = initialChaosPercent
        # only one policy allowed to be created for a GH gas.  Change this rate if wanted.
        self.chaosPercent = initialChaosPercent
        # rate at which we may create a policy each month.
        self.policyPercent = initialPolicyPercent
        self.chaosInProgress = False
        self.chaosComplete =True
        self.policyInProgress = False
        self.policyComplete = True
    #gets next GHRate we will be using as base.
    def getGHRate(self):
        return super().popNextRate()
    # calculate is called from main simulation.
    def calculateNextGh(self):
        rate = self.changePolicyChaos()
        myCumVal = super().getCumValue()
        #multiply by initial value
        #print(super().getCumValue())
        GHval = (myCumVal * rate) + myCumVal
        super().addToCumSum(GHval)
        return GHval

    # Method to Change, checks threshold of policy and changes the percent.
    def changePolicyChaos(self):
        # If policy in progress, we slowly decrease GH gases and don't change the initial rate.
        # once policy complete, change it back to initial value
        rate = self.getGHRate()
        chaos = self.getChaosPercent()
        policy = self.getPolicyPercent()
        ### THESE TWO CAN BE FLIPpED IN IF STATEMENT AND IT WILL DETERMINE DIFFERENT RATES FOR THE GH GAS.  Do you want more politcally correct? swap policy first.
        if self.chaosInProgress:
            myYear, myMonth  = ghgControl.ghgControl.getSimTime()
            if self.endChaosTime == myYear and self.startPolicyMonth == myMonth:
                self.chaosInProgress=False
                self.setChaosPercent(self.initialPolicyPercent)
            else:
                rate = rate + abs(rate*self.chaosChange)
        # arbitrary value, it is a threshold.
        elif chaos > .6:
            self.createChaos()
            rate = rate + abs(rate*self.chaosChange)
        #increase chaos
        else:
            self.setChaosPercent(chaos + np.random.normal(.01, .03))

        if self.policyInProgress:
            myYear, myMonth  = ghgControl.ghgControl.getSimTime()
            # we lower rate right here...
            if self.endPolicyTime == myYear and self.startPolicyMonth == myMonth:
                self.policyInProgress=False
                self.setPolicyPercent(self.initialPolicyPercent)
            else:
                rate = rate - abs(rate*self.policyChange)
        # arbitrary value, it is a threshold.
        elif policy > .4:
            self.createPolicy()
            rate = rate - abs(rate*self.policyChange)
        else:
            self.setPolicyPercent(policy + np.random.normal(.01, .03))
            #increase policy
        return rate

    # create a GH diminishing policy to take effect in a time period (checks within this method, helper).  One the "grace period" is over, the rates are maintained.
    def createPolicy(self):
        #check conditions if policy needs to be created.
        #if it needs to be created (the policy can be desired minimum average increase in a greenhouse gas), then set the minimum
        # if it is in progress, attempt to lower the rates.
        #once policy is complete.  The gas cannot exceed the policy, but can be redacted
        policyTimeSpan = np.random.randint(1, 20)
        #start year
        startTimeYear, self.startPolicyMonth = ghgControl.ghgControl.getSimTime()
        self.endPolicyTime = startTimeYear + policyTimeSpan
        self.policyChange = np.random.normal(.015,.012)
        self.policyInProgress=True

    def createChaos(self):
        chaosTimeSpan = np.random.randint(1, 5)
        #start year
        startChaosYear, self.startChaosMonth = ghgControl.ghgControl.getSimTime()
        self.endChaosTime = startChaosYear + chaosTimeSpan
        self.chaosChange = .0006
        self.chaosInProgress=True

    def getChaosPercent(self):
        return self.chaosPercent
    def getPolicyPercent(self):
        return self.policyPercent

    def setPolicyPercent(self, percent):
        self.policyPercent = percent
    def setChaosPercent(self, percent):
        self.chaosPercent = percent


class n2oControl(ghgControl.ghgControl):
    def __init__(self, n2oRateFName, initialN2o, initialPolicyPercent=.01, initialChaosPercent=.01):
        super().__init__(n2oRateFName, initialN2o)

        self.policyCount = 0
        self.initialPolicyPercent = initialPolicyPercent
        self.initialChaosPercent = initialChaosPercent
        # only one policy allowed to be created for a GH gas.  Change this rate if wanted.
        self.chaosPercent = initialChaosPercent
        # rate at which we may create a policy each month.
        self.policyPercent = initialPolicyPercent
        self.chaosInProgress = False
        self.chaosComplete =True
        self.policyInProgress = False
        self.policyComplete = True
    #gets next GHRate we will be using as base.
    def getGHRate(self):
        return super().popNextRate()
    # calculate is called from main simulation.
    def calculateNextGh(self):
        rate = self.changePolicyChaos()
        myCumVal = super().getCumValue()
        #multiply by initial value
        #print(super().getCumValue())
        GHval = (myCumVal * rate) + myCumVal
        super().addToCumSum(GHval)
        return GHval

    # Method to Change, checks threshold of policy and changes the percent.
    def changePolicyChaos(self):
        # If policy in progress, we slowly decrease GH gases and don't change the initial rate.
        # once policy complete, change it back to initial value
        rate = self.getGHRate()
        chaos = self.getChaosPercent()
        policy = self.getPolicyPercent()
        ### THESE TWO CAN BE FLIPpED IN IF STATEMENT AND IT WILL DETERMINE DIFFERENT RATES FOR THE GH GAS.  Do you want more politcally correct? swap policy first.
        if self.chaosInProgress:
            myYear, myMonth  = ghgControl.ghgControl.getSimTime()
            if self.endChaosTime == myYear and self.startPolicyMonth == myMonth:
                self.chaosInProgress=False
                self.setChaosPercent(self.initialPolicyPercent)
            else:
                rate = rate + abs(rate*self.chaosChange)
        # arbitrary value, it is a threshold.
        elif chaos > .6:
            self.createChaos()
            rate = rate + abs(rate*self.chaosChange)
        #increase chaos
        else:
            self.setChaosPercent(chaos + np.random.normal(.01, .03))

        if self.policyInProgress:
            myYear, myMonth  = ghgControl.ghgControl.getSimTime()
            # we lower rate right here...
            if self.endPolicyTime == myYear and self.startPolicyMonth == myMonth:
                self.policyInProgress=False
                self.setPolicyPercent(self.initialPolicyPercent)
            else:
                rate = rate - abs(rate*self.policyChange)
        # arbitrary value, it is a threshold.
        elif policy > .4:
            self.createPolicy()
            rate = rate - abs(rate*self.policyChange)
        else:
            self.setPolicyPercent(policy + np.random.normal(.01, .03))
            #increase policy
        return rate

    # create a GH diminishing policy to take effect in a time period (checks within this method, helper).  One the "grace period" is over, the rates are maintained.
    def createPolicy(self):
        #check conditions if policy needs to be created.
        #if it needs to be created (the policy can be desired minimum average increase in a greenhouse gas), then set the minimum
        # if it is in progress, attempt to lower the rates.
        #once policy is complete.  The gas cannot exceed the policy, but can be redacted
        policyTimeSpan = np.random.randint(1, 20)
        #start year
        startTimeYear, self.startPolicyMonth = ghgControl.ghgControl.getSimTime()
        self.endPolicyTime = startTimeYear + policyTimeSpan
        self.policyChange = np.random.normal(.015,.012)
        self.policyInProgress=True

    def createChaos(self):
        chaosTimeSpan = np.random.randint(1, 5)
        #start year
        startChaosYear, self.startChaosMonth = ghgControl.ghgControl.getSimTime()
        self.endChaosTime = startChaosYear + chaosTimeSpan
        self.chaosChange = .0006
        self.chaosInProgress=True

    def getChaosPercent(self):
        return self.chaosPercent
    def getPolicyPercent(self):
        return self.policyPercent

    def setPolicyPercent(self, percent):
        self.policyPercent = percent
    def setChaosPercent(self, percent):
        self.chaosPercent = percent
