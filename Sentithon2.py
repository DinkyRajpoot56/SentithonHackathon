import matplotlib.pyplot as plt
Info=[50,110,190,230,290,300,310,320,310,320,340,400]
follower=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
plt.bar(Info,follower,color=['red'])
plt.xlabel("Twitter User growth")
plt.ylabel("Year")
plt.show()