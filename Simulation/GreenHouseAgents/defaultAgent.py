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
        self.chaosComplete =True
        self.policyInProgress = False
        self.policyComplete = True
    #gets next GHRate we will be using as base.
    def getGHRate(self):
        return super().popNextRate()
    # calculate is called from main simulation.
    def calculateNextGh(self):
        self.changePolicyChaos()
        rate = self.getGHRate()
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
        chaos = self.getChaosPercent()
        policy = self.getPolicyPercent()
        ### THESE TWO CAN BE FLIPpED IN IF STATEMENT AND IT WILL DETERMINE DIFFERENT RATES FOR THE GH GAS.  Do you want more politcally correct? swap policy first.
        if self.chaosInProgress:
            pass
        # arbitrary value, it is a threshold.
        elif chaos > .7:
            self.createChaos()
        #increase chaos
        else:
            pass
        if self.policyInProgress:
            myYear, myMonth  = ghgControl.ghgControl.getSimTime()
            # we lower rate right here...
            if self.endTime == myYear and self.startTimeMonth == myMonth:
                self.policyInProgress=False
                self.setPolicyPercent(self.initialPolicyPercent)


        # arbitrary value, it is a threshold.
        elif policy > .4:
            self.createPolicy()
        else:
            pass
            #increase policy


    # create a GH diminishing policy to take effect in a time period (checks within this method, helper).  One the "grace period" is over, the rates are maintained.
    def createPolicy(self):
        #check conditions if policy needs to be created.
        #if it needs to be created (the policy can be desired minimum average increase in a greenhouse gas), then set the minimum
        # if it is in progress, attempt to lower the rates.
        #once policy is complete.  The gas cannot exceed the policy, but can be redacted
        policyTimeSpan = random.randomrange(1, 21,1)
        #start year
        startTimeYear, self.startTimeMonth = ghgControl.ghgControl.getSimTime()
        self.endTime = startTimeYear + policyTimeSpan
        self.policyChange = np.random.normal(0,.12)

    def createChaos(self):
        self.policyTimeSpan = random.randomrange(1, 21,1)
        #start year
        self.start = ghgControl.ghgControl.getSimTime()
    def getChaosPercent(self):
        return self.chaosPercent
    def getPolicyPercent(self):
        return self.policyPercent

    def setPolicyPercent(self, percent):
        self.policyPercent = percent
    def setChaosPercent(self, percent):
        self.chaosPercent = percent


class ch4Control(ghgControl.ghgControl):
    def __init__(self, ch4RateFName, initialCh4, initialPolicyPercent=.01, initialChaosPercent=.01):
        super().__init__(ch4RateFName, initialCh4)

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
        self.changePolicyChaos()
        rate = self.getGHRate()
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
        chaos = self.getChaosPercent()
        policy = self.getPolicyPercent()
        ### THESE TWO CAN BE FLIPpED IN IF STATEMENT AND IT WILL DETERMINE DIFFERENT RATES FOR THE GH GAS.  Do you want more politcally correct? swap policy first.
        if self.chaosInProgress:
            pass
        # arbitrary value, it is a threshold.
        elif chaos > .7:
            self.createChaos()
        #increase chaos
        else:
            pass
        if self.policyInProgress:
            myYear, myMonth  = ghgControl.ghgControl.getSimTime()
            # we lower rate right here...
            if self.endTime == myYear and self.startTimeMonth == myMonth:
                self.policyInProgress=False
                self.setPolicyPercent(self.initialPolicyPercent)


        # arbitrary value, it is a threshold.
        elif policy > .4:
            self.createPolicy()
        else:
            pass
            #increase policy
    # create a GH diminishing policy to take effect in a time period (checks within this method, helper).  One the "grace period" is over, the rates are maintained.
    def createPolicy(self):
        #check conditions if policy needs to be created.
        #if it needs to be created (the policy can be desired minimum average increase in a greenhouse gas), then set the minimum
        # if it is in progress, attempt to lower the rates.
        #once policy is complete.  The gas cannot exceed the policy, but can be redacted
        policyTimeSpan = random.randomrange(1, 21,1)
        #start year
        startTimeYear, self.startTimeMonth = ghgControl.ghgControl.getSimTime()
        self.endTime = startTimeYear + policyTimeSpan
        self.policyChange = np.random.normal(0,.12)

    def createChaos(self):
        self.policyTimeSpan = random.randomrange(1, 21,1)
        #start year
        self.start = ghgControl.ghgControl.getSimTime()
    def getChaosPercent(self):
        return self.chaosPercent
    def getPolicyPercent(self):
        return self.policyPercent

    def setPolicyPercent(self, percent):
        self.policyPercent = percent
    def setChaosPercent(self, percent):
        self.chaosPercent = percent

class co2Control(ghgControl.ghgControl):
    def __init__(self, Co2RateFName, initialCo2, initialPolicyPercent=.01, initialChaosPercent=.01):
        super().__init__(Co2RateFName, initialCo2)

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
        self.changePolicyChaos()
        rate = self.getGHRate()
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
        chaos = self.getChaosPercent()
        policy = self.getPolicyPercent()
        ### THESE TWO CAN BE FLIPpED IN IF STATEMENT AND IT WILL DETERMINE DIFFERENT RATES FOR THE GH GAS.  Do you want more politcally correct? swap policy first.
        if self.chaosInProgress:
            pass
        # arbitrary value, it is a threshold.
        elif chaos > .7:
            self.createChaos()
        #increase chaos
        else:
            pass
        if self.policyInProgress:
            myYear, myMonth  = ghgControl.ghgControl.getSimTime()
            # we lower rate right here...
            if self.endTime == myYear and self.startTimeMonth == myMonth:
                self.policyInProgress=False
                self.setPolicyPercent(self.initialPolicyPercent)


        # arbitrary value, it is a threshold.
        elif policy > .4:
            self.createPolicy()
        else:
            pass
            #increase policy
    # create a GH diminishing policy to take effect in a time period (checks within this method, helper).  One the "grace period" is over, the rates are maintained.
    def createPolicy(self):
        #check conditions if policy needs to be created.
        #if it needs to be created (the policy can be desired minimum average increase in a greenhouse gas), then set the minimum
        # if it is in progress, attempt to lower the rates.
        #once policy is complete.  The gas cannot exceed the policy, but can be redacted
        policyTimeSpan = random.randomrange(1, 21,1)
        #start year
        startTimeYear, self.startTimeMonth = ghgControl.ghgControl.getSimTime()
        self.endTime = startTimeYear + policyTimeSpan
        self.policyChange = np.random.normal(0,.12)

    def createChaos(self):
        self.policyTimeSpan = random.randomrange(1, 21,1)
        #start year
        self.start = ghgControl.ghgControl.getSimTime()
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
        self.changePolicyChaos()
        rate = self.getGHRate()
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
        chaos = self.getChaosPercent()
        policy = self.getPolicyPercent()
        ### THESE TWO CAN BE FLIPpED IN IF STATEMENT AND IT WILL DETERMINE DIFFERENT RATES FOR THE GH GAS.  Do you want more politcally correct? swap policy first.
        if self.chaosInProgress:
            pass
        # arbitrary value, it is a threshold.
        elif chaos > .7:
            self.createChaos()
        #increase chaos
        else:
            pass
        if self.policyInProgress:
            myYear, myMonth  = ghgControl.ghgControl.getSimTime()
            # we lower rate right here...
            if self.endTime == myYear and self.startTimeMonth == myMonth:
                self.policyInProgress=False
                self.setPolicyPercent(self.initialPolicyPercent)


        # arbitrary value, it is a threshold.
        elif policy > .4:
            self.createPolicy()
        else:
            pass
            #increase policy
    # create a GH diminishing policy to take effect in a time period (checks within this method, helper).  One the "grace period" is over, the rates are maintained.
    def createPolicy(self):
        #check conditions if policy needs to be created.
        #if it needs to be created (the policy can be desired minimum average increase in a greenhouse gas), then set the minimum
        # if it is in progress, attempt to lower the rates.
        #once policy is complete.  The gas cannot exceed the policy, but can be redacted
        policyTimeSpan = random.randomrange(1, 21,1)
        #start year
        startTimeYear, self.startTimeMonth = ghgControl.ghgControl.getSimTime()
        self.endTime = startTimeYear + policyTimeSpan
        self.policyChange = np.random.normal(0,.12)

    def createChaos(self):
        self.policyTimeSpan = random.randomrange(1, 21,1)
        #start year
        self.start = ghgControl.ghgControl.getSimTime()
    def getChaosPercent(self):
        return self.chaosPercent
    def getPolicyPercent(self):
        return self.policyPercent

    def setPolicyPercent(self, percent):
        self.policyPercent = percent
    def setChaosPercent(self, percent):
        self.chaosPercent = percent


    # create a GH diminishing policy to take effect in a time period (checks within this method, helper).  One the "grace period" is over, the rates are maintained.
    #this is the function that should be changed in all classes to find different policies.
    def createPolicy(self):
        #check conditions if policy needs to be created.
        #if it needs to be created (the policy can be desired minimum average increase in a greenhouse gas), then set the minimum
        # if it is in progress, attempt to lower the rates.
        #once policy is complete.  The gas cannot exceed the policy, but can be redacted

        if self.policyInProgress:
            pass
        else:
            pass