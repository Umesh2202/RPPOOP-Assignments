import time


class Time:
    def test_time(self):
        str1 = str(input("Press any key and press ENTER to begin test"))
        if str1:
            print("What is the capital of India? (Answer in all lower cases)")
            ans1 = str(input("Answer:"))
            while(1):
                if(ans1 == "dehli"):
                    print("Correct!")
                    break
                else:
                    print("Incorrect,try again!")
                    ans1 = str(input("Answer:"))

            print("What is the National Animal of India? (Answer in all lower cases)")
            ans1 = str(input("Answer:"))
            while(1):
                if(ans1 == "tiger"):
                    print("Correct!")
                    break
                else:
                    print("Incorrect,try again!")
                    ans1 = str(input("Answer:"))

            print("What is the National flower of India? (Answer in all lower cases)")
            ans1 = str(input("Answer:"))
            while(1):
                if(ans1 == "lotus"):
                    print("Correct!")
                    break
                else:
                    print("Incorrect,try again!")
                    ans1 = str(input("Answer:"))
            return
            # while(str1 != "end"):
            # str1 = str(input())


start_time = time.time()
student = Time()
time1 = student.test_time()
end_time = time.time()
print("Time taken to complete the test: ", end_time - start_time)
