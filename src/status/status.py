import time


class Status(object):
    counter = 0
    start = time.time()

    def status(self) -> str:
        try:
            self.counter += 1
            print("router: get")
            res = "Server Status\nServer uptime: " + str(int(time.time() - self.start)) + " s.\nvisitors counter: " + str(
                self.counter)
            return res
        except (Exception) as error:
            print("Error:", error)
            return "errror"
