import matplotlib.pyplot as plt
import datetime
import pandas as pd


def getDate(DateString):
    date = DateString.split("-")[0]
    return datetime.datetime.strptime(date, '%Y %b %d')


def graph():
    # Plot from CSv file
    df = pd.read_csv('party.csv')
    df.columns = ["Date", "Republican", "Independent", "Democrat"]
    df["Date"] = df["Date"].apply(getDate)
    df.plot(x="Date", y=["Republican", "Independent", "Democrat"], color=["red", "orange", "blue"])
    # Annotate latest points
    np = df.to_numpy()
    li = (list(np[0]))
    plt.annotate(str(li[1]) + "%", (li[0], li[1]))
    plt.annotate(str(li[2]) + "%", (li[0], li[2]))
    plt.annotate(str(li[3]) + "%", (li[0], li[3]))
    plt.annotate("Point 1", (df["Date"][0], 4))
    # Configure Plot
    plt.legend(loc="upper left")
    plt.xlabel("Date")
    plt.ylabel("Party Affiliation %")
    plt.grid()

    plt.show()


if __name__ == '__main__':
    graph()
