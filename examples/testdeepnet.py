from deepnet.deepnetclassfy import JppbrbsNet

obj = JppbrbsNet(img="golden_cat.jpg")
obj.eval()
print("Object is {} and has a percentage of {} certainty.".format(obj.getName(), obj.getPercentage()))