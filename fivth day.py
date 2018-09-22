class mynewclass():
    name = "yangqiang"
    def showname(self):
        print(self.name)

test = mynewclass()
test.showname()
print(test.__dir__())
