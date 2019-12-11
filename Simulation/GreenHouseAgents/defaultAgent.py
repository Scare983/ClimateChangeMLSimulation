import GreenHouseAgents.ghgControl as ghgControl


class sf6Control(ghgControl.ghgControl):
    def __init__(self, sf6RateFName, initialSf6):
        super().__init__(sf6RateFName, initialSf6)
        self.policyCount = 0
        #policies is minimum values, they are created and removed based on chaos and diplomatic levels set random in parent class.
        self.policies = []
        # only one policy allowed to be created for a GH gas.
        self.policyInProgress = False
        self.policyComplete = False
    #gets next GHRate we will be using as base.
    def getGHRate(self):
        return super().popNextRate()
    # calculate is called from main simulation.
    def calculateNextGh(self):
        rate = self.getGHRate()
        myCumVal = super().getCumValue()
        #multiply by initial value
        #print(super().getCumValue())
        GHval = (myCumVal * rate) + myCumVal
        super().addToCumSum(GHval)
        return GHval

    # create a GH diminishing policy to take effect in a time period (checks within this method, helper).  One the "grace period" is over, the rates are maintained.
    def createPolicy(self):
        #check conditions if policy needs to be created.
        #if it needs to be created (the policy can be desired minimum average increase in a greenhouse gas), then set the minimum
        # if it is in progress, attempt to lower the rates.
        #once policy is complete.  The gas cannot exceed the policy, but can be redacted
        if self.policyInProgress:
            pass
        else:
            pass

class ch4Control(ghgControl.ghgControl):
    def __init__(self, ch4RateFName, initialCh4):
        super().__init__(ch4RateFName, initialCh4)
        self.policyCount = 0
        #policies is minimum values, they are created and removed based on chaos and diplomatic levels set random in parent class.
        self.policies = []
        # only one policy allowed to be created for a GH gas.
        self.policyInProgress = False
        self.policyComplete = False
    #gets next GHRate we will be using as base.
    def getGHRate(self):
        return super().popNextRate()
    # calculate is called from main simulation.
    def calculateNextGh(self):
        rate = self.getGHRate()
        cumValue = super().getCumValue()
        #multiply by initial value
        GHval = (cumValue * rate) + cumValue
        super().addToCumSum(GHval)
        return GHval


    # create a GH diminishing policy to take effect in a time period (checks within this method, helper).  One the "grace period" is over, the rates are maintained.
    def createPolicy(self):
        #check conditions if policy needs to be created.
        #if it needs to be created (the policy can be desired minimum average increase in a greenhouse gas), then set the minimum
        # if it is in progress, attempt to lower the rates.
        #once policy is complete.  The gas cannot exceed the policy, but can be redacted

        if self.policyInProgress:
            pass
        else:
            pass

class co2Control(ghgControl.ghgControl):
    def __init__(self, co2RateFName, initialCo2):
        super().__init__(co2RateFName, initialCo2)
        self.policyCount = 0
        #policies is minimum values, they are created and removed based on chaos and diplomatic levels set random in parent class.
        self.policies = []
        # only one policy allowed to be created for a GH gas.
        self.policyInProgress = False
        self.policyComplete = False
    #gets next GHRate we will be using as base.
    def getGHRate(self):
        return super().popNextRate()
    # calculate is called from main simulation.
    def calculateNextGh(self):
        rate = self.getGHRate()
        cumValue = super().getCumValue()
        #multiply by initial value
        GHval = (cumValue * rate) + cumValue
        super().addToCumSum(GHval)
        return GHval

    # create a GH diminishing policy to take effect in a time period (checks within this method, helper).  One the "grace period" is over, the rates are maintained.
    def createPolicy(self):
        #check conditions if policy needs to be created.
        #if it needs to be created (the policy can be desired minimum average increase in a greenhouse gas), then set the minimum
        # if it is in progress, attempt to lower the rates.
        #once policy is complete.  The gas cannot exceed the policy, but can be redacted

        if self.policyInProgress:
            pass
        else:
            pass



class n2oControl(ghgControl.ghgControl):
    def __init__(self, n2oRateFName, initialN2o):
        super().__init__(n2oRateFName, initialN2o)
        self.policyCount = 0
        #policies is minimum values, they are created and removed based on chaos and diplomatic levels set random in parent class.
        self.policies = []
        # only one policy allowed to be created for a GH gas.
        self.policyInProgress = False
        self.policyComplete = False
    #gets next GHRate we will be using as base, helper.
    def getGHRate(self):
        return super().popNextRate()
    # calculate is called from main simulation.
    def calculateNextGh(self):
        rate = self.getGHRate()
        cumValue = super().getCumValue()
        #multiply by initial value
        GHval = (cumValue * rate) + cumValue
        super().addToCumSum(GHval)
        return GHval




    # create a GH diminishing policy to take effect in a time period (checks within this method, helper).  One the "grace period" is over, the rates are maintained.
    def createPolicy(self):
        #check conditions if policy needs to be created.
        #if it needs to be created (the policy can be desired minimum average increase in a greenhouse gas), then set the minimum
        # if it is in progress, attempt to lower the rates.
        #once policy is complete.  The gas cannot exceed the policy, but can be redacted

        if self.policyInProgress:
            pass
        else:
            pass

