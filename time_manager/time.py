import time
class Time:
    def start(self):
        self.start = time.time()
    def end(self):
        return str("{0:.2f}".format(time.time() - self.start)) + " seconds"

if __name__ == "__main__":
    t = Time()
    t.start()
    for i in range(100):
        print(i, end= " ")
    print()
    print(t.end())